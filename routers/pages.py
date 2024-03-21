from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import db

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.jinja",
        context={"page_title": "Home", "outfits": db.outfits},
    )


@router.get("/cart", response_class=HTMLResponse)
def cart(request: Request):
    db.session["counter"]
    return templates.TemplateResponse(
        request=request,
        name="cart.jinja",
        context={"session": db.session, "page_title": "Cart"},
    )
