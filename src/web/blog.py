from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from src.fake.posts import posts

router = APIRouter()
templates = Jinja2Templates(directory="src/template")


@router.get("/blog")
def blog_list(request: Request):
    published_posts = [post for post in posts if post["is_published"]]
    return templates.TemplateResponse(
        "blog_list.html", {"request": request, "posts": published_posts}
    )


@router.get("/blog/{post_title}")
def blog_post(request: Request, post_title: str):
    slugified_title = post_title.replace("-", " ")
    matching_posts = [post for post in posts if post["title"].lower() == slugified_title.lower()]

    if matching_posts:
        return templates.TemplateResponse(
            "blog.html", {"request": request, "post": matching_posts[0]}
        )
    else:
        return {"message": "Blog post not found"}
