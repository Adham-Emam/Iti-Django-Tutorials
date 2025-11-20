from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from datetime import datetime
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Post


def home(request):
    featured_posts = Post.objects.filter(is_featured=True)

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
                "icon": "📊",
                "title": "Analytics",
                "description": "Track your post performance",
            },
        ],
        "is_featured_active": True,
        "spotlight_topic": "Web Development",
        "featured_posts": featured_posts,
    }

    return render(request, "blog/home.html", context)


def about(request):
    context = {
        "current_year": datetime.now().year,
        "company_name": "BlogHub Team",
        "founded_year": 2025,
        "mission": "Empowering writers to share their stories with the world",
        "team_size": 15,
        "values": [
            "Creativity",
            "Community",
            "Quality Content",
            "Freedom of Expression",
        ],
    }

    return render(request, "blog/about.html", context)


def posts(request):
    posts = Post.objects.filter(published=True)
    context = {
        "page_title": "All Blog Posts",
        "current_year": datetime.now().year,
        "posts": posts,
        "total_posts": len(posts),
    }
    return render(request, "blog/posts.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    tags = post.tags.all()
    context = {"post": post, "tags": tags}
    return render(request, "blog/post_detail.html", context)


def category_posts(request, category_name):
    posts = Post.objects.filter(published=True)

    if category_name != category_name.lower():
        return redirect("blog:category_posts", category_name=category_name.lower())

    filtered_posts = [
        post for post in posts if post.category.name.lower() == category_name
    ]

    context = {
        "category_name": category_name.title(),
        "posts": filtered_posts,
        "total_posts": len(filtered_posts),
    }
    return render(request, "blog/category_posts.html", context)


def search_posts(request):
    posts = Post.objects.filter(published=True)
    query = request.GET.get("q", "")

    if not query:
        search_results = posts
    else:
        search_results = [
            post
            for post in posts
            if query.lower() in post.title.lower()
            or query.lower() in post.excerpt.lower()
            or query.lower() in post.category.name.lower()
            or query.lower() in post.author.first_name.lower()
            or query.lower() in post.author.last_name.lower()
        ]

    context = {
        "query": query,
        "posts": search_results,
        "total_results": len(search_results),
    }
    return render(request, "blog/search_results.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not all([name, email, subject, message]):
            messages.error(request, "Please fill in all fields.")
        elif "@" not in email:
            messages.error(request, "Please enter a valid email address.")
        else:
            print(f"Contact: {name}, {email}, {subject}, {message}")
            messages.success(request, f"Thank you {name}! We received your message.")
            return redirect("blog:contact")

    context = {
        "current_year": datetime.now().year,
        "email": "contact@bloghub.com",
        "phone": "+1-800-BLOGHUB",
        "address": "456 Writers Lane, Content City, CC 54321",
        "business_hours": "Monday - Friday: 9AM - 6PM",
        "departments": [
            {"name": "IT", "email": "it@bloghub.com"},
            {"name": "HR", "email": "HR@bloghub.com"},
            {"name": "Finance", "email": "Finance@bloghub.com"},
            {"name": "Marketing", "email": "Marketing@bloghub.com"},
        ],
        "social_media": [
            {"platform": "Facebook"},
            {"platform": "Reddit"},
            {"platform": "Twitter"},
        ],
    }
    return render(request, "blog/contact.html", context)


# ----------------------
# Author Posts
# ----------------------
def author_posts(request, author_name):
    posts = Post.objects.filter(published=True)
    author_slug = author_name.lower().replace(" ", "-")

    filtered = [
        p
        for p in posts
        if f"{p.author.first_name.lower()} {p.author.last_name.lower()}" == author_slug
    ]

    context = {
        "author_name": author_name.replace("-", " ").title(),
        "posts": filtered,
        "total_posts": len(filtered),
        "current_year": datetime.now().year,
    }
    return render(request, "blog/author_posts.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(CreateView):
    model = Post
    fields = [
        "title",
        "excerpt",
        "content",
        "category",
        "author",
        "published",
    ]
    template_name = "blog/post_create.html"
    success_url = reverse_lazy("blog:post_list")


class PostUpdateView(UpdateView):
    model = Post
    fields = [
        "title",
        "excerpt",
        "content",
        "category",
        "author",
        "published",
    ]
    template_name = "blog/post_update.html"
    success_url = reverse_lazy("blog:post_list")


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("blog:post_list")
