# Weather Intelligence Actor

This actor fetches weather forecasts and alerts from [WeatherAPI.com](https://weatherapi.com) for 4,468 South African wards and upserts the data into Supabase.

## Overview

- **Source**: WeatherAPI.com `/forecast.json` (3-day forecast + alerts)
- **Target**: Supabase tables: `ai_intelligence.weather_cache` and `ai_intelligence.weather_alerts`
- **Schedule**: Designed to run **6 times daily** (every 4 hours)
- **Budget**: Uses individual API calls (throttled) to stay within the **Free Tier (1M calls/month)** limit.
  - 4,468 wards × 6 runs/day × 30 days ≈ 804,240 calls/month.

## Architecture

1. **Fetch Wards**: Reads all ward coordinates (`ward_code`, `latitude`, `longitude`) from Supabase `weather_cache`.
2. **Batch Processing**: Groups wards into batches (default 50) to process concurrently.
3. **Fetch Weather**: Calls WeatherAPI for each ward with 3-retry backoff and rate limit handling.
4. **Upsert**: Writes results back to Supabase in chunks (500 rows/chunk).
   - Updates `weather_cache` with current weather + 3-day forecast JSON.
   - Replaces rows in `weather_alerts` for any active alerts.

## Configuration

### Environment Variables

Required Apify environment variables:

| Variable | Description |
|---|---|
| `WEATHER_API_KEY` | API Key from WeatherAPI.com |
| `SUPABASE_URL` | Supabase project URL (e.g., `https://xyz.supabase.co`) |
| `SUPABASE_SERVICE_KEY` | Supabase **Service Role** key (for write access) |

### Input Schema

| Field | Type | Default | Description |
|---|---|---|---|
| `batchSize` | Integer | `50` | Number of concurrent API requests per batch. |
| `delayBetweenBatchesMs` | Integer | `200` | Throttle time (ms) between batches. |
| `maxWardsToProcess` | Integer | `0` | Limit wards to process (0 = all). |
| `runTestMode` | Boolean | `false` | If true, processes only 5 wards for testing. |

## Data Schema

### `ai_intelligence.weather_cache`

| Column | Type | Description |
|---|---|---|
| `ward_code` | text (PK) | Unique ward identifier |
| `latitude` | numeric | Ward latitude |
| `longitude` | numeric | Ward longitude |
| `temperature_c` | numeric | Current temperature (°C) |
| `condition_text` | text | Current weather condition (e.g., "Sunny") |
| `condition_icon` | text | Icon URL |
| `wind_kph` | numeric | Wind speed (km/h) |
| `humidity` | integer | Humidity % |
| `is_day` | boolean | True if day, False if night |
| `precip_mm` | numeric | Precipitation (mm) |
| `daily_forecast` | jsonb | Array of 3-day forecast objects |
| `alerts_summary` | jsonb | Array of active alerts (JSON summary) |
| `raw_response` | jsonb | Full raw API response |
| `fetched_at` | timestamptz | Timestamp of last successful fetch |

### `ai_intelligence.weather_alerts`

Stores individual alerts linked to wards. Tables are cleared for a ward before inserting new alerts.

| Column | Type | Description |
|---|---|---|
| `id` | uuid (PK) | Unique alert ID |
| `ward_code` | varchar (FK) | Links to `weather_cache` |
| `event` | varchar | Event name (e.g., "Flood Warning") |
| `headline` | text | Headline text |
| `severity` | varchar | Severity level |
| `urgency` | varchar | Urgency level |
| `areas` | text | Affected areas description |
| `effective` | timestamptz | Effective start time |
| `expires` | timestamptz | Expiration time |

## Deployment

1. **Push to Apify**:
   ```bash
   apify push
   ```
2. **Set Environment Variables** in Apify Console (Settings page).
3. **Schedule**: Create a schedule to run every 4 hours.

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create `.env` file with required variables (or set in shell).
3. Run with test input:
   ```bash
   apify run -i '{"runTestMode": true}'
   ```
