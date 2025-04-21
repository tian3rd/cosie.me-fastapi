from datetime import datetime

posts = [
    {
        "title": "My First Blog Post",
        "date": datetime(2023, 1, 1),
        "author": "John Doe",
        "tags": ["blogging", "writing"],
        "body": "This is the body of my first blog post. I'm excited to start sharing my thoughts!",
        "version": 1,
        "is_published": True,
    },
    {
        "title": "Why I Love Python",
        "date": datetime(2023, 2, 15),
        "author": "Jane Smith",
        "tags": ["python", "programming"],
        "body": "In this post, I'll explain some of the reasons Python is my favorite programming language.",
        "version": 1,
        "is_published": True,
    },
    {
        "title": "Unpublished Draft Post",
        "date": datetime(2023, 3, 1),
        "author": "John Doe",
        "tags": ["drafts"],
        "body": "This is an unpublished draft post. It won't show up on the blog page.",
        "version": 1,
        "is_published": False,
    },
]
