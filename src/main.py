"""Weather Intelligence Actor — Main entry point.

Fetches 3-day weather forecasts and alerts from WeatherAPI.com
for all 4,468 South African wards and upserts to Supabase.
"""

from __future__ import annotations

import asyncio
import os
import time

import aiohttp
from apify import Actor

from .weather_client import fetch_ward_weather
from .supabase_client import get_supabase_client, get_all_wards, upsert_weather_batch, upsert_alerts


async def main() -> None:
    """Main entry point for the Apify Actor."""
    async with Actor:
        # ── Read input ──────────────────────────────────────────────
        raw_input = await Actor.get_input() or {}
        batch_size = raw_input.get("batchSize", 50)
        delay_ms = raw_input.get("delayBetweenBatchesMs", 200)
        max_wards = raw_input.get("maxWardsToProcess", 0)
        test_mode = raw_input.get("runTestMode", False)

        if test_mode:
            max_wards = 5
            Actor.log.info("🧪 TEST MODE: Processing only 5 wards.")

        # ── Validate env vars ───────────────────────────────────────
        api_key = os.getenv("WEATHER_API_KEY")
        if not api_key:
            Actor.log.error("❌ WEATHER_API_KEY environment variable is not set.")
            await Actor.exit(exit_code=1)
            return

        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
        if not supabase_url or not supabase_key:
            Actor.log.error("❌ SUPABASE_URL and SUPABASE_SERVICE_KEY environment variables are required.")
            await Actor.exit(exit_code=1)
            return

        Actor.log.info(f"⚙️ Config: batchSize={batch_size}, delay={delay_ms}ms, maxWards={max_wards}")

        # ── Fetch ward coordinates from Supabase ────────────────────
        sb = get_supabase_client()
        wards = await get_all_wards(sb, limit=max_wards)

        if not wards:
            Actor.log.error("❌ No wards found in weather_cache table.")
            await Actor.exit(exit_code=1)
            return

        total_wards = len(wards)
        Actor.log.info(f"🌍 Processing {total_wards} wards...")

        # ── Batch fetch weather data ────────────────────────────────
        semaphore = asyncio.Semaphore(batch_size)
        all_results = []
        failed_count = 0
        start_time = time.time()

        async with aiohttp.ClientSession() as session:
            # Process in batches for progress logging
            for batch_start in range(0, total_wards, batch_size):
                batch_end = min(batch_start + batch_size, total_wards)
                batch = wards[batch_start:batch_end]
                batch_num = (batch_start // batch_size) + 1
                total_batches = (total_wards + batch_size - 1) // batch_size

                Actor.log.info(f"📦 Batch {batch_num}/{total_batches} ({batch_start+1}-{batch_end}/{total_wards})")

                tasks = [
                    fetch_ward_weather(
                        session=session,
                        api_key=api_key,
                        lat=float(ward["latitude"]),
                        lng=float(ward["longitude"]),
                        ward_code=ward["ward_code"],
                        semaphore=semaphore,
                    )
                    for ward in batch
                ]

                results = await asyncio.gather(*tasks)

                # Collect successful results
                batch_results = [r for r in results if r is not None]
                batch_failed = len(results) - len(batch_results)
                failed_count += batch_failed
                all_results.extend(batch_results)

                if batch_failed > 0:
                    Actor.log.warning(f"⚠️ {batch_failed} failed in batch {batch_num}")

                # ── Upsert batch to Supabase immediately ────────────
                if batch_results:
                    upserted = await upsert_weather_batch(sb, batch_results)
                    alerts_count = await upsert_alerts(sb, batch_results)
                    Actor.log.info(f"✅ Upserted {upserted} weather rows, {alerts_count} alerts")

                # Throttle between batches
                if delay_ms > 0 and batch_end < total_wards:
                    await asyncio.sleep(delay_ms / 1000)

        # ── Summary ─────────────────────────────────────────────────
        elapsed = time.time() - start_time
        summary = {
            "total_wards": total_wards,
            "successful": len(all_results),
            "failed": failed_count,
            "elapsed_seconds": round(elapsed, 1),
            "wards_per_second": round(total_wards / elapsed, 1) if elapsed > 0 else 0,
        }

        Actor.log.info(f"🏁 Complete: {summary['successful']}/{total_wards} wards updated in {summary['elapsed_seconds']}s")

        # Push summary to Apify dataset
        await Actor.push_data(summary)
        Actor.log.info("📊 Summary pushed to dataset.")
