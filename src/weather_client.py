"""WeatherAPI.com client for fetching forecast + alerts."""

from __future__ import annotations

import asyncio
from typing import Any

import aiohttp
from apify import Actor

WEATHER_API_BASE = "http://api.weatherapi.com/v1"


async def fetch_ward_weather(
    session: aiohttp.ClientSession,
    api_key: str,
    lat: float,
    lng: float,
    ward_code: str,
    semaphore: asyncio.Semaphore,
) -> dict[str, Any] | None:
    """Fetch 3-day forecast + alerts for a single ward coordinate.

    Returns parsed dict with keys: current, forecast_days, alerts, raw
    or None on failure.
    """
    url = f"{WEATHER_API_BASE}/forecast.json"
    params = {
        "key": api_key,
        "q": f"{lat},{lng}",
        "days": 3,
        "alerts": "yes",
        "aqi": "no",
    }

    async with semaphore:
        for attempt in range(3):
            try:
                async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=30)) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return _parse_response(data, ward_code)

                    if resp.status == 429:
                        wait = 2 ** (attempt + 1)
                        Actor.log.warning(f"⏳ Rate limited for {ward_code}, retrying in {wait}s...")
                        await asyncio.sleep(wait)
                        continue

                    error_text = await resp.text()
                    Actor.log.error(f"❌ API error {resp.status} for {ward_code}: {error_text[:200]}")
                    return None

            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                if attempt < 2:
                    wait = 2 ** (attempt + 1)
                    Actor.log.warning(f"⚠️ Retry {attempt+1}/3 for {ward_code}: {e}")
                    await asyncio.sleep(wait)
                else:
                    Actor.log.error(f"❌ Failed after 3 retries for {ward_code}: {e}")
                    return None

    return None


def _parse_response(data: dict, ward_code: str) -> dict[str, Any]:
    """Extract structured weather data from API response."""
    current = data.get("current", {})
    forecast = data.get("forecast", {})
    alerts_data = data.get("alerts", {})
    condition = current.get("condition", {})

    # Build daily forecast array
    forecast_days = []
    for day_data in forecast.get("forecastday", []):
        day_info = day_data.get("day", {})
        astro = day_data.get("astro", {})
        day_condition = day_info.get("condition", {})

        forecast_days.append({
            "date": day_data.get("date"),
            "maxtemp_c": day_info.get("maxtemp_c"),
            "mintemp_c": day_info.get("mintemp_c"),
            "avgtemp_c": day_info.get("avgtemp_c"),
            "maxwind_kph": day_info.get("maxwind_kph"),
            "totalprecip_mm": day_info.get("totalprecip_mm"),
            "avghumidity": day_info.get("avghumidity"),
            "condition_text": day_condition.get("text"),
            "condition_icon": day_condition.get("icon"),
            "daily_chance_of_rain": day_info.get("daily_chance_of_rain"),
            "daily_chance_of_snow": day_info.get("daily_chance_of_snow"),
            "uv": day_info.get("uv"),
            "sunrise": astro.get("sunrise"),
            "sunset": astro.get("sunset"),
        })

    # Parse alerts
    alerts = []
    for alert in alerts_data.get("alert", []):
        alerts.append({
            "event": alert.get("event"),
            "headline": alert.get("headline"),
            "description": alert.get("desc"),
            "severity": alert.get("severity"),
            "urgency": alert.get("urgency"),
            "areas": alert.get("areas"),
            "category": alert.get("category"),
            "certainty": alert.get("certainty"),
            "instruction": alert.get("instruction"),
            "effective": alert.get("effective"),
            "expires": alert.get("expires"),
        })

    return {
        "ward_code": ward_code,
        "temperature_c": current.get("temp_c"),
        "condition_text": condition.get("text"),
        "condition_icon": condition.get("icon"),
        "wind_kph": current.get("wind_kph"),
        "humidity": current.get("humidity"),
        "is_day": current.get("is_day") == 1,
        "precip_mm": current.get("precip_mm"),
        "forecast_days": forecast_days,
        "alerts": alerts,
        "alerts_summary": alerts if alerts else None,
        "raw": data,
    }
