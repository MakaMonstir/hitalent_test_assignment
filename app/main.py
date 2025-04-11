from fastapi import FastAPI
from app.routers import table, reservation

app = FastAPI()

app.include_router(table.router)
app.include_router(reservation.router)
