from fastapi import APIRouter, Request
import db

router = APIRouter()


@router.post("/counter")
async def counters(request: Request):
    db.session["counter"] += 1
    return db.session["counter"]
