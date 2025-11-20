from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # Existing function-based pages
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("posts/", views.posts, name="posts"),
    path("category/<str:category_name>/", views.category_posts, name="category_posts"),
    path("search/", views.search_posts, name="search_posts"),
    path("author/<str:author_name>/", views.author_posts, name="author_posts"),
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/create/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
]
