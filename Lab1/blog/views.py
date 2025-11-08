from django.shortcuts import render
from datetime import datetime


# Create your views here.
def home(request):
    context = {
        "site_name": "BlogHub",
        "tagline": "Your Platform for Sharing Ideas",
        "total_posts": 247,
        "total_authors": 45,
        "current_year": datetime.now().year,
        "featured_topics": ["Technology", "Design", "Travel", "Education", "Lifestyle"],
        "features": [
            {
                "icon": "✍️",
                "title": "Easy Publishing",
                "description": "Write and publish posts effortlessly",
            },
            {
                "icon": "🎨",
                "title": "Beautiful Design",
                "description": "Professional templates for your content",
            },
            {
                "icon": "👥",
                "title": "Engage Readers",
                "description": "Build your audience and community",
            },
            {
                "icon": "�",
                "title": "Analytics",
                "description": "Track your post performance",
            },
        ],
        "is_featured_active": True,
        "spotlight_topic": "Web Development",
    }
    return render(request, "blog/home.html", context)


def about(request):
    context = {}
    return render(request, "blog/about.html")


def contact(request):
    context = {
        "title": "Contact Us",
        "email": "adham@gmail.com",
        "phone": "+1234567890",
        "address": "123 Blog St, Blog City, BL 45678",
        "business_hours": "Monday-Friday" "9am - 6pm",
        "departments": [
            {"name": "adham", "email": "adham@gmail.com"},
            {"name": "elsayed", "email": "example@yahoo.com"},
            {"name": "hossam", "email": "test@yahoo.com"},
            {"name": "youssef", "email": "sdfeiwehgw@yahoo.com"},
        ],
        "social_media": [
            {"platform": "Twitter", "url": "https://twitter.com/example"},
            {"platform": "Facebook", "url": "https://facebook.com/example"},
            {"platform": "LinkedIn", "url": "https://linkedin.com/in/example"},
            {"platform": "Instagram", "url": "https://instagram.com/example"},
        ],
    }
    return render(request, "blog/contact.html", context)


def posts(request):
    context = {
        "title": "Posts",
        "posts_list": [
            {
                "title": "Getting Started with Django",
                "author": "Sarah Johnson",
                "category": "Technology",
                "excerpt": "Learn the fundamentals of Django web development",
                "published": False,
                "date": "2025-01-15",
            },
            {
                "title": "Getting Started with Django",
                "author": "Sarah Johnson",
                "category": "Technology",
                "excerpt": "Learn the fundamentals of Django web development",
                "published": True,
                "date": "2025-01-15",
            },
            {
                "title": "Getting Started with Django",
                "author": "Sarah Johnson",
                "category": "Technology",
                "excerpt": "Learn the fundamentals of Django web development",
                "published": False,
                "date": "2025-01-15",
            },
            {
                "title": "Getting Started with Django",
                "author": "Sarah Johnson",
                "category": "Technology",
                "excerpt": "Learn the fundamentals of Django web development",
                "published": False,
                "date": "2025-01-15",
            },
            {
                "title": "Getting Started with Django",
                "author": "Sarah Johnson",
                "category": "Technology",
                "excerpt": "Learn the fundamentals of Django web development",
                "published": True,
                "date": "2025-01-15",
            },
            {
                "title": "Getting Started with Django",
                "author": "Sarah Johnson",
                "category": "Technology",
                "excerpt": "Learn the fundamentals of Django web development",
                "published": False,
                "date": "2025-01-15",
            },
            {
                "title": "Getting Started with Django",
                "author": "Sarah Johnson",
                "category": "Technology",
                "excerpt": "Learn the fundamentals of Django web development",
                "published": True,
                "date": "2025-01-15",
            },
        ],
    }

    return render(request, "blog/posts.html", context)
