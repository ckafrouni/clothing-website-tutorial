# After downloading the python requirements:
# `pip install -r requirements.txt`
#
# Run the project with:
# `uvicorn main:app --reload --reload-include static/ --reload-include templates/`

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import api, pages

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(pages.router, prefix="")
app.include_router(api.router, prefix="/api")
