import asyncio
import os
import random
import socket
import time
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List

from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse

from app.colors import get_random_color, get_color_by_spec, get_all_colors

app = FastAPI(title="color", docs_url=None, redoc_url=None)

# Counter n tracking non-favicon requests
n_counter: int = 0

# Configurable sleep range (milliseconds)
SLEEP_MIN_MS: float = float(os.getenv("SLEEP_MIN_MS", "2"))
SLEEP_MAX_MS: float = float(os.getenv("SLEEP_MAX_MS", "200"))

HEADERS_TO_CAPTURE: List[str] = [
    "X-Real-IP",
    "X-Forwarded-For",
    "X-Auth-Request-User",
    "X-Auth-Request-Email",
    "X-Forwarded-Email",
    "X-Forwarded-User",
    "X-Forwarded-Proto",
    "X-Forwarded-Host",
    "User-Agent",
]


@app.middleware("http")
async def process_request(request: Request, call_next):
    global n_counter
    # Calls to /favicon.ico do not count
    if request.url.path != "/favicon.ico":
        n_counter += 1

    response = await call_next(request)
    return response


@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)


async def simulate_delay() -> int:
    """Simulate CPU/network delay and return sleep time in milliseconds."""
    if SLEEP_MAX_MS > SLEEP_MIN_MS:
        sleep_ms = random.randint(int(SLEEP_MIN_MS), int(SLEEP_MAX_MS))
    else:
        sleep_ms = int(SLEEP_MIN_MS)

    if sleep_ms > 0:
        await asyncio.sleep(sleep_ms / 1000.0)
    return sleep_ms


def build_response_data(request: Request, color_obj: Any, sleep_ms: int) -> Dict[str, Any]:
    now = datetime.now(timezone.utc)
    host = socket.gethostname()

    # Capture specified headers, default to "" if absent
    captured_headers = {}
    for header_name in HEADERS_TO_CAPTURE:
        captured_headers[header_name] = request.headers.get(header_name, "")

    data = {
        "n": n_counter,
        "sleep": sleep_ms,
        "host": host,
        "date": now.isoformat(),
        "timestamp": int(now.timestamp()),
        "color": color_obj,
    }
    data.update(captured_headers)
    return data


@app.get("/color/random")
async def get_random_color_endpoint(request: Request):
    sleep_ms = await simulate_delay()
    color_obj = get_random_color()
    return JSONResponse(build_response_data(request, color_obj, sleep_ms))


@app.get("/color/{color_spec}")
async def get_specific_color_endpoint(color_spec: str, request: Request):
    sleep_ms = await simulate_delay()
    color_obj = get_color_by_spec(color_spec)
    if not color_obj:
        raise HTTPException(status_code=404, detail=f"Color '{color_spec}' not found")
    return JSONResponse(build_response_data(request, color_obj, sleep_ms))


@app.get("/colors")
async def get_colors_endpoint(request: Request):
    sleep_ms = await simulate_delay()
    all_colors = get_all_colors()
    return JSONResponse(build_response_data(request, all_colors, sleep_ms))


@app.get("/")
async def root_endpoint(request: Request):
    return await get_random_color_endpoint(request)
