from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql.sqltypes import DateTime as SQLAlchemyDateTime

from app.db import Base


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    table_id = Column(Integer, ForeignKey('tables.id'), nullable=False)
    reservation_time = Column(
        SQLAlchemyDateTime(timezone=True), nullable=False
    )
    duration_minutes = Column(Integer, nullable=False)
