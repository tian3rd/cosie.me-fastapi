from datetime import datetime
from pathlib import Path
from textwrap import dedent

import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.web.blog import router as blog_router
from src.web.wip import router as wip_router
from src.web.contact import router as contact_router

app = FastAPI()

templates = Jinja2Templates(directory="src/template")

top = Path(__file__).resolve().parent

app.mount("/static/css", StaticFiles(directory=top / "src" / "style"), name="static")
app.mount("/static/images", StaticFiles(directory=top / "src" / "image"), name="static")
app.mount(
    "/static/favicon", StaticFiles(directory=top / "src" / "image" / "favicon.ico"), name="static"
)
app.mount(
    "/static/animation", StaticFiles(directory=top / "src" / "style" / "animation"), name="static"
)

app.include_router(blog_router)
app.include_router(wip_router)
app.include_router(contact_router)


def get_cosie_age() -> str:
    """Get the age of Cosie in human readable string."""
    cosie_dob = datetime(2022, 6, 22)
    today = datetime.now()
    # calculate the age of Cosie in months
    cosie_age_in_month = (today.year - cosie_dob.year) * 12 + (today.month - cosie_dob.month)
    cosie_age_in_years, cosie_age_extra_months = cosie_age_in_month // 12, cosie_age_in_month % 12
    # format with proper pluralization in month (Cosie is over 2 years now)
    cosie_age_str = f"{cosie_age_in_years} years"
    if cosie_age_extra_months == 0:
        return cosie_age_str
    if cosie_age_extra_months == 1:
        return f"{cosie_age_str} and 1 month"
    return f"{cosie_age_str} and {cosie_age_extra_months} months"


@app.get("/")
def homepage(request: Request):
    """Just write a simple introduction about Ellen, Cosie and I."""
    self_introduction = dedent(
        f"""
        Greetings 🐾👋👋 (also from cool Ellen 😎 and handsome Cosie/Zz ⽝, {get_cosie_age()} old).
        Cosie, Ellen and I all love hiking 🥾 (yes, we enjoy the bush capital! 🌳🪾🍃)
        We are an army of three 🐶😎🤓, building a small world one line of code at a time / one bark at a time.
        """
    )
    return templates.TemplateResponse(
        "home.html", {"request": request, "self_introduction": self_introduction}
    )


if __name__ == "__main__":
    uvicorn.run("hello:app", port=8000, reload=True)
