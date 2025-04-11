from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import SessionLocal

router = APIRouter(prefix="/reservations", tags=["Reservations"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.reservation.ReservationOut])
def get_reservations(db: Session = Depends(get_db)):
    return db.query(models.Reservation).all()


@router.post("/", response_model=schemas.reservation.ReservationOut)
def create_reservation(
    reservation: schemas.reservation.ReservationCreate,
    db: Session = Depends(get_db)
):
    start = reservation.reservation_time
    end = start + timedelta(minutes=reservation.duration_minutes)

    conflict = db.query(models.Reservation).filter(
        models.Reservation.table_id == reservation.table_id,
        models.Reservation.reservation_time < end,
        (
            models.Reservation.reservation_time
            + timedelta(minutes=models.Reservation.duration_minutes)
        ) > start
    ).first()

    if conflict:
        raise HTTPException(
            status_code=400, detail="Time slot is already booked"
        )

    db_res = models.Reservation(**reservation.dict())
    db.add(db_res)
    db.commit()
    db.refresh(db_res)
    return db_res


@router.delete("/{reservation_id}", status_code=204)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = (
        db.query(models.Reservation)
        .filter(models.Reservation.id == reservation_id)
        .first()
    )
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    db.delete(reservation)
    db.commit()
