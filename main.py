from datetime import datetime
from pathlib import Path
from textwrap import dedent

import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.web.blog import router as blog_router

app = FastAPI()

templates = Jinja2Templates(directory="src/template")

top = Path(__file__).resolve().parent

app.mount("/static/css", StaticFiles(directory=top / "src" / "style"), name="static")
app.mount("/static/images", StaticFiles(directory=top / "src" / "image"), name="static")

app.include_router(blog_router)

cosie_dob = datetime(2022, 6, 22)
today = datetime.now()
# calculate the age of Cosie in months
cosie_age_in_month = (today.year - cosie_dob.year) * 12 + (today.month - cosie_dob.month)
cosie_age_str = f"{cosie_age_in_month // 12} years and {cosie_age_in_month % 12} months"


@app.get("/")
def root(request: Request):
    self_introduction = dedent(
        f"""
        Greetings 👋👋🐾 (also from cool Ellen 😎 and handsome Cosie/Zz, {cosie_age_str} old).
        Ellen, Cosie and I all love hiking 🥾 (yes, we enjoy the bush capital!)
        We are an army of three, building a better world, one line of code at a time / one bark at a time.
        """
    )

    return templates.TemplateResponse(
        "home.html", {"request": request, "self_introduction": self_introduction}
    )


@app.get("/hi")
def say_hi():
    return {"message": "Hello, world!"}


@app.get("/hi/{name}")
def say_hi_to(name: str):
    if name.lower() == "ellen":
        return "Hi Ellen, I'm your boyfriend Phillip! Shall we play some tennis?"
    return "Hi, {name}"


if __name__ == "__main__":
    uvicorn.run("hello:app", port=8000, reload=True)
