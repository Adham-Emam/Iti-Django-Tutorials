import random
from datetime import date
from django.contrib.auth.models import User
from blog.models import Category, Tag, Post  # adjust app name if needed

# Clear old data
Post.objects.all().delete()
Category.objects.all().delete()
Tag.objects.all().delete()
User.objects.exclude(is_superuser=True).delete()

# Create dummy users
usernames = [
    "sarah",
    "michael",
    "emma",
    "david",
    "alex",
    "nora",
    "james",
    "sophia",
    "chris",
]
users = []

for username in usernames:
    user = User.objects.create_user(
        username=username,
        first_name=username,
        last_name=f"test{username}",
        email=f"{username}@example.com",
        password="password123",
    )
    users.append(user)

# Create categories
category_names = [
    "Technology",
    "Self-Improvement",
    "Design",
    "Business",
    "Lifestyle",
    "Health",
    "Career",
]
categories = [Category.objects.create(name=name) for name in category_names]

# Create tags
tag_names = [
    "Django",
    "Python",
    "Web Development",
    "Productivity",
    "Habits",
    "UI",
    "UX",
    "Machine Learning",
    "AI",
    "Backend",
    "API",
    "Business",
    "Finance",
    "Reading",
    "Health",
    "Projects",
]
tags = [Tag.objects.create(name=name) for name in tag_names]

# Dummy post data
post_data = [
    {
        "title": "Getting Started with Django",
        "author": users[0],
        "category": categories[0],
        "excerpt": "Learn the fundamentals of Django web development.",
        "published": True,
        "reading_time": 5,
        "is_featured": True,
        "tag_names": ["Django", "Python", "Web Development"],
    },
    {
        "title": "The Psychology of Productivity",
        "author": users[1],
        "category": categories[1],
        "excerpt": "How to build strong habits without burning out.",
        "published": True,
        "reading_time": 6,
        "is_featured": False,
        "tag_names": ["Productivity", "Habits"],
    },
    {
        "title": "Top 10 UI Mistakes in Modern Web Design",
        "author": users[2],
        "category": categories[2],
        "excerpt": "Avoid these common design pitfalls that reduce user engagement.",
        "published": True,
        "reading_time": 7,
        "is_featured": True,
        "tag_names": ["UI", "Design", "UX"],
    },
    {
        "title": "Exploring Machine Learning with Python",
        "author": users[3],
        "category": categories[0],
        "excerpt": "Why ML matters and how to begin building models.",
        "published": False,
        "reading_time": 9,
        "is_featured": False,
        "tag_names": ["Python", "Machine Learning", "AI"],
    },
    {
        "title": "How to Invest as a Beginner",
        "author": users[4],
        "category": categories[3],
        "excerpt": "Understanding the basics of financial investments.",
        "published": True,
        "reading_time": 8,
        "is_featured": False,
        "tag_names": ["Business", "Finance"],
    },
    {
        "title": "Why Reading Every Day Changes You",
        "author": users[5],
        "category": categories[4],
        "excerpt": "Reading is a superpower that expands thinking.",
        "published": True,
        "reading_time": 6,
        "is_featured": False,
        "tag_names": ["Lifestyle", "Reading", "Habits"],
    },
    {
        "title": "Mastering RESTful APIs",
        "author": users[6],
        "category": categories[0],
        "excerpt": "Build scalable and maintainable APIs using best practices.",
        "published": True,
        "reading_time": 10,
        "is_featured": True,
        "tag_names": ["API", "REST", "Backend", "Web Development"],
    },
    {
        "title": "Healthy Eating for Programmers",
        "author": users[7],
        "category": categories[5],
        "excerpt": "Tips to stay energized and avoid burnout.",
        "published": False,
        "reading_time": 5,
        "is_featured": False,
        "tag_names": ["Health", "Productivity", "Lifestyle"],
    },
    {
        "title": "The Power of Side Projects",
        "author": users[8],
        "category": categories[6],
        "excerpt": "How personal projects can transform your professional life.",
        "published": True,
        "reading_time": 7,
        "is_featured": True,
        "tag_names": ["Career", "Projects", "Self Improvement"],
    },
]

# Create posts and attach tags
for data in post_data:
    post = Post.objects.create(
        title=data["title"],
        author=data["author"],
        category=data["category"],
        excerpt=data["excerpt"],
        published=data["published"],
        reading_time=data["reading_time"],
        is_featured=data["is_featured"],
        views=random.randint(0, 500),
    )
    post.tags.set(Tag.objects.filter(name__in=data["tag_names"]))

print("✅ Database seeded successfully with users, categories, tags, and posts!")
