# color

A lightweight FastAPI application that returns color definitions along with request metadata, timestamps, and forward headers.

## Endpoints

- `GET /color/random`: Returns a random color from the dataset along with request metadata.
- `GET /color/{color_spec}`: Returns a specific color by English name (e.g., `khaki`) or hex code (e.g., `F0E68C` or `#F0E68C`).
- `GET /colors`: Returns the full dictionary of CSS3 named colors.
- `GET /favicon.ico`: Returns `204 No Content` without incrementing the request counter.

## Response Format

```json
{
  "n": 1,
  "sleep": 160,
  "host": "color-58bd6f6547-smfmm",
  "date": "2026-03-31T14:30:00.000000+00:00",
  "timestamp": 1774967400,
  "color": {
    "khaki": {
      "hex": "#F0E68C",
      "rgb": "(240,230,140)",
      "name": "khaki"
    }
  },
  "X-Real-IP": "172.31.18.68",
  "X-Forwarded-For": "172.31.18.68, 10.1.167.46",
  "X-Auth-Request-User": "",
  "X-Auth-Request-Email": "",
  "X-Auth-Request-Access-Token": "",
  "X-Auth-Request-Groups": "",
  "X-Auth-Request-Preferred-Username": "",
  "X-Auth-Request-Token": "",
  "X-Auth-Request-Redirect": "",
  "X-Forwarded-Email": "user@example.com",
  "X-Forwarded-User": "",
  "X-Forwarded-Groups": "",
  "X-Forwarded-Preferred-Username": "",
  "X-Forwarded-Access-Token": "",
  "X-Forwarded-Id-Token": "",
  "X-Forwarded-Roles": "",
  "X-Forwarded-Proto": "",
  "X-Forwarded-Host": "",
  "Authorization": "",
  "User-Agent": ""
}
```

## Configuration

- `SLEEP_MIN_MS`: Minimum simulated CPU delay in milliseconds (default: `2`).
- `SLEEP_MAX_MS`: Maximum simulated CPU delay in milliseconds (default: `200`).

## Running locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Running with Docker

Build and run as a rootless container:

```bash
docker build -t color .
docker run -p 8000:8000 color
```
