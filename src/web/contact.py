from textwrap import dedent

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/template")


@router.get("/contact")
async def contact(request: Request):
    headline = "Experienced Software Engineer with a strong background in DevOps, DataOps, and software development."

    about_content = "Skilled in cloud services, API development, and data engineering. Optimistic about the brave new tech world."

    work_experience = [
        {
            "company": "Seeing Machines",
            "title": "Software Engineer (DevOps/DevTools/DataOps)",
            "location": "Fyshwick, ACT",
            "dates": "Feb 2023 - Present",
            "description": dedent(
                """Customized scripts and pipelines to generate and visualize ASPICE reports.
                   Implemented automation of in-house tools to synchronize data between softwares.
                   Optimized cross-department cloud storage cost by 40% with AWS S3 services."""
            ),
        },
        {
            "company": "Software Innovation Institute",
            "title": "Software Developer",
            "location": "Acton, ACT",
            "dates": "Jun 2022 - Feb 2023",
            "description": dedent(
                """Developed an open source cross-platform package rdflib in Dart.
                   Implemented design documents and integrated peripherals with Adafruit Feather board."""
            ),
        },
        {
            "company": "Center For Gravitational Astrophysics",
            "title": "Techinal Assistant",
            "location": "Acton, ACT",
            "dates": "Feb 2022 - Feb 2023",
            "description": dedent(
                """Developed different software interfaces for mechanical equipment in the lab.
                   Assisted researchers with data analysis and visualization."""
            ),
        },
    ]

    education = [
        {
            "school": "The Australian National University",
            "degree": "Master of Computing",
            "dates": "Feb 2020 - Dec 2021",
        }
    ]

    skills = [
        "Python",
        "SQL",
        "Dart",
        "Java",
        "AWS (S3, EC2, Batch, Lambda)",
        "Jenkins",
        "GitHub Actions",
        "Docker",
        "Ansible",
        "JavaScript",
        "React",
        "FastAPI",
        "tailwindcss",
        "DuckDB",
    ]

    return templates.TemplateResponse(
        "contact.html",
        {
            "request": request,
            "name": "Tian Wu",
            "headline": headline,
            "location": "Canberra, Australia",
            "profile_img": "/static/images/profile.webp",
            "about_content": about_content,
            "work_experience": work_experience,
            "education": education,
            "skills": skills,
        },
    )
