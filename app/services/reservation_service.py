from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models import Reservation


def has_conflict(
    db: Session, table_id: int, start: datetime, duration_minutes: int
) -> bool:
    start = start.replace(tzinfo=None)
    end = (start + timedelta(minutes=duration_minutes)).replace(tzinfo=None)

    reservations = (
        db.query(Reservation)
        .filter(Reservation.table_id == table_id)
        .all()
    )

    for r in reservations:
        r_start = r.reservation_time
        r_end = r_start + timedelta(minutes=r.duration_minutes)

        if start < r_end and end > r_start:
            return True
    return False
