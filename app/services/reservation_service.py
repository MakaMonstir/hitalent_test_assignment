from datetime import datetime, timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session

from app import models


def has_conflict(
    db: Session, table_id: int, start: datetime, duration_minutes: int
) -> bool:
    end = start + timedelta(minutes=duration_minutes)

    reservations = models.Reservation
    conflict = db.query(reservations).filter(
        reservations.table_id == table_id,
        reservations.reservation_time < end,
        (
            reservations.reservation_time
            + func.make_interval(mins=reservations.duration_minutes)
        ) > start
    ).first()

    return conflict is not None
