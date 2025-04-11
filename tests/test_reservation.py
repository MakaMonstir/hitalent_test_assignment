from datetime import datetime, timedelta, timezone

import pytest


@pytest.mark.asyncio
async def test_create_table(client):
    res = await client.post("/tables/", json={
        "name": "Test Table",
        "seats": 4,
        "location": "Corner"
    })
    assert res.status_code == 200
    assert res.json()["name"] == "Test Table"


@pytest.mark.asyncio
async def test_create_reservation(client):
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    res = await client.post("/reservations/", json={
        "customer_name": "Alice",
        "table_id": 1,
        "reservation_time": now,
        "duration_minutes": 60
    })
    assert res.status_code == 200
    assert res.json()["customer_name"] == "Alice"


@pytest.mark.asyncio
async def test_conflict_reservation(client):
    now = datetime.now(timezone.utc).replace(microsecond=0)
    res = await client.post("/reservations/", json={
        "customer_name": "Bob",
        "table_id": 1,
        "reservation_time": (now + timedelta(minutes=30)).isoformat(),
        "duration_minutes": 30
    })
    assert res.status_code == 400
    assert res.json()["detail"] == "Time slot is already booked"
