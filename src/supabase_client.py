"""Supabase client for reading ward data and upserting weather results."""

from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Any

from apify import Actor
from supabase import create_client, Client


def get_supabase_client() -> Client:
    """Create and return a Supabase client from env vars."""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_KEY")
    if not url or not key:
        raise RuntimeError("SUPABASE_URL and SUPABASE_SERVICE_KEY env vars are required.")
    return create_client(url, key)


async def get_all_wards(client: Client, limit: int = 0) -> list[dict[str, Any]]:
    """Fetch all ward codes with their coordinates from weather_cache.

    Args:
        client: Supabase client instance
        limit: Max wards to return (0 = all, defaults to 10000 to cover all 4468 wards)

    Returns:
        List of dicts with ward_code, latitude, longitude
    """
    if limit > 0:
        # Standard query with limit
        query = client.schema("ai_intelligence").table("weather_cache").select("ward_code, latitude, longitude")
        result = query.limit(limit).execute()
        Actor.log.info(f"📍 Fetched {len(result.data)} ward coordinates from Supabase (Limit: {limit}).")
        return result.data
    
    # Pagination loop for limit=0 (fetchAll)
    all_wards = []
    page_size = 1000
    start = 0
    
    while True:
        query = client.schema("ai_intelligence").table("weather_cache").select("ward_code, latitude, longitude")
        result = query.range(start, start + page_size - 1).execute()
        
        batch = result.data
        if not batch:
            break
            
        all_wards.extend(batch)
        Actor.log.info(f"📍 Fetched page {start}-{start + len(batch) - 1} from Supabase. Total so far: {len(all_wards)}")
        
        if len(batch) < page_size:
            break
            
        start += page_size

    Actor.log.info(f"✅ Total wards fetched: {len(all_wards)}")
    return all_wards


async def upsert_weather_batch(client: Client, weather_results: list[dict[str, Any]]) -> int:
    """Upsert a batch of weather results into weather_cache.

    Returns count of successfully upserted rows.
    """
    now = datetime.now(timezone.utc).isoformat()
    rows = []

    for w in weather_results:
        rows.append({
            "ward_code": w["ward_code"],
            "latitude": w["latitude"],
            "longitude": w["longitude"],
            "temperature_c": w["temperature_c"],
            "condition_text": w["condition_text"],
            "condition_icon": w["condition_icon"],
            "wind_kph": w["wind_kph"],
            "humidity": w["humidity"],
            "is_day": w["is_day"],
            "precip_mm": w["precip_mm"],
            "daily_forecast": w["forecast_days"],
            "alerts_summary": w["alerts_summary"],
            "raw_response": w["raw"],
            "fetched_at": now,
            "updated_at": now,
        })

    if not rows:
        return 0

    # Upsert in chunks of 500 to avoid payload limits
    upserted = 0
    chunk_size = 500
    for i in range(0, len(rows), chunk_size):
        chunk = rows[i : i + chunk_size]
        try:
            client.schema("ai_intelligence").table("weather_cache").upsert(
                chunk, on_conflict="ward_code"
            ).execute()
            upserted += len(chunk)
        except Exception as e:
            Actor.log.error(f"❌ Upsert failed for chunk {i//chunk_size}: {e}")

    return upserted


async def upsert_alerts(client: Client, weather_results: list[dict[str, Any]]) -> int:
    """Insert weather alerts into weather_alerts table.

    First deletes existing alerts for these wards, then inserts fresh ones.
    Returns count of alerts inserted.
    """
    # Collect all alerts with ward_code attached
    alert_rows = []
    ward_codes_with_alerts = set()

    for w in weather_results:
        if not w.get("alerts"):
            continue
        ward_code = w["ward_code"]
        ward_codes_with_alerts.add(ward_code)
        for alert in w["alerts"]:
            alert_rows.append({
                "ward_code": ward_code,
                "event": alert.get("event"),
                "headline": alert.get("headline"),
                "description": alert.get("description"),
                "severity": alert.get("severity"),
                "urgency": alert.get("urgency"),
                "areas": alert.get("areas"),
                "category": alert.get("category"),
                "certainty": alert.get("certainty"),
                "instruction": alert.get("instruction"),
                "effective": alert.get("effective"),
                "expires": alert.get("expires"),
            })

    if not alert_rows:
        return 0

    # Delete old alerts for affected wards, then insert new ones
    try:
        for ward_code in ward_codes_with_alerts:
            client.schema("ai_intelligence").table("weather_alerts").delete().eq(
                "ward_code", ward_code
            ).execute()

        # Insert in chunks
        inserted = 0
        chunk_size = 500
        for i in range(0, len(alert_rows), chunk_size):
            chunk = alert_rows[i : i + chunk_size]
            client.schema("ai_intelligence").table("weather_alerts").insert(chunk).execute()
            inserted += len(chunk)

        return inserted

    except Exception as e:
        Actor.log.error(f"❌ Alert upsert failed: {e}")
        return 0
