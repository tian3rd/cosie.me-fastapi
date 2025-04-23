from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/template")


@router.get("/wip")
async def wip(request: Request):
    return templates.TemplateResponse("wip.html", {"request": request})


@router.get("/wip/{wip_id}")
async def wip_id(request: Request, wip_id: str):
    return templates.TemplateResponse("wip.html", {"request": request, "wip_id": wip_id})
