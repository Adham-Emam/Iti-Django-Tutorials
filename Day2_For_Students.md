# Day 2: Advanced Views, URLs & Templates Mastery

---

## 🎯 **PROJECT CONTINUATION: BlogHub - Blogging Platform**

---

## 📋 **DAY 2 LEARNING OBJECTIVES**

By the end of Day 2, students will:
1. Master dynamic URL patterns with parameters
2. Use path converters (int, str, slug, uuid)
3. Implement named URLs and URL reversing
4. Handle different HTTP methods in views
5. Use Django shortcuts (redirect, get_object_or_404)
6. Create template inheritance with base templates
7. Integrate Bootstrap globally using base templates
8. Build blog post detail pages with dynamic URLs
9. Implement category filtering
10. Add search functionality
11. Handle forms with CSRF protection

---

## 🗓️ **DETAILED LECTURE PLAN**

### **⏰ TIME ALLOCATION**

```
LECTURE SESSIONS (4 hours):
├── Session 1: Dynamic URLs & Advanced Views (2 hours)
│   ├── Part 1: URL Patterns with Parameters (45 min)
│   ├── Break (10 minutes)
│   ├── Part 2: Path Converters & Named URLs (45 min)
│   ├── Break (10 minutes)
│   └── Part 3: Advanced Views & HTTP Methods (20 min)
├── Session 2: Template Inheritance & Advanced Features (2 hours)
│   ├── Part 4: Template Inheritance (45 min)
│   ├── Break (10 minutes)
│   ├── Part 5: Category Filtering & Search (45 min)
│   └── Part 6: Forms & CSRF Protection (20 min)
```

---

## 📚 **SESSION 1: Dynamic URLs & Advanced Views**

---

### **Part 1: URL Patterns with Parameters**

#### 🎯 **Goal**: Create dynamic URLs that accept parameters

**📋 What We Will Learn:**
- Why we need dynamic URLs
- How to capture URL parameters
- Passing parameters to views
- Building blog post detail pages

---

#### **1.1 The Problem: Static URLs**

```
Yesterday we created pages with static URLs:
  /                → Home page
  /about/          → About page
  /contact/        → Contact page
  /posts/          → All blog posts

But what if we want to show ONE specific post?
  /post/1/         → Post with ID 1
  /post/2/         → Post with ID 2
  /post/999/       → Post with ID 999

We can't create 999 different URL patterns!
We need DYNAMIC URLs!
```

**🎨 See This Visual:**
```
Static URLs (Day 1):
┌──────────────────────────────────┐
│  URL              View           │
├──────────────────────────────────┤
│  /                home()         │
│  /about/          about()        │
│  /contact/        contact()      │
│  /posts/          posts()        │
└──────────────────────────────────┘
Fixed, unchanging URLs

Dynamic URLs (Day 2):
┌──────────────────────────────────┐
│  URL Pattern           View      │
├──────────────────────────────────┤
│  /post/<id>/       post_detail   │
│                    ↑             │
│              Variable part!      │
└──────────────────────────────────┘

Examples:
  /post/1/  → post_detail(request, id=1)
  /post/5/  → post_detail(request, id=5)
  /post/99/ → post_detail(request, id=99)

One URL pattern, infinite possibilities!
```

---

#### **1.2 Creating Dynamic URL Patterns**

**Syntax:**
```python
path('post/<parameter_name>/', view_function)
           ↑       ↑
           │       └─ Variable name (passed to view)
           └─ Angle brackets = dynamic part
```

**Example - Update blog/urls.py:**

```python
# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('posts/', views.posts, name='posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # ⭐ New!
]
```

**Explanation:**
```
path('post/<int:post_id>/', views.post_detail, name='post_detail')
              ↑   ↑
              │   └─ Variable name that will be passed to view
              └─ Path converter (int) - ensures only integers match

Path converters automatically validate and convert URL parts to the correct Python type before passing them to your view function.


How it works:
1. User visits: /post/5/
2. Django captures: post_id = 5 (as integer!)
3. Django calls: post_detail(request, post_id=5)
4. View receives the post_id and can use it

Important: 
  - <int:post_id> captures as INTEGER (not string)
  - /post/5/ → post_id = 5 (integer)
  - /post/abc/ → 404 Not Found (doesn't match pattern!)
```

---

#### **1.3 Create Post Detail View**

**Add to blog/views.py:**

```python
from django.http import Http404

def post_detail(request, post_id):
    """
    Display a single blog post's details
    
    Parameters:
        request: Django's HttpRequest object
        post_id: Captured from URL (integer thanks to path converter)
    
    In a real app, we would:
        post = Post.objects.get(id=post_id)
    But we don't have database yet, so we'll use sample data.
    """
    
    # Sample blog post data (simulating database)
    # Later (Day 3), this will come from the database
    all_posts = [
        {
            'id': 1,
            'title': 'Getting Started with Django',
            'author': 'Sarah Johnson',
            'category': 'Technology',
            'content': 'Django is a powerful web framework that makes building web applications fast and easy. In this comprehensive guide, we\'ll explore the fundamentals of Django development, from setting up your first project to deploying it to production.',
            'published': True,
            'date': '2025-01-15',
            'tags': ['Django', 'Python', 'Web Development', 'Tutorial'],
            'views': 1250,
            'reading_time': '8 min'
        },
        {
            'id': 2,
            'title': 'Mastering CSS Grid Layout',
            'author': 'Mike Chen',
            'category': 'Design',
            'content': 'CSS Grid is a revolutionary layout system that changed how we build responsive designs. Learn how to create complex, flexible layouts with ease.',
            'published': True,
            'date': '2025-01-20',
            'tags': ['CSS', 'Design', 'Frontend', 'Grid'],
            'views': 890,
            'reading_time': '6 min'
        },
        {
            'id': 3,
            'title': 'Traveling Through Southeast Asia',
            'author': 'Emma Rodriguez',
            'category': 'Travel',
            'content': 'Discover the hidden gems of Southeast Asia with our comprehensive travel guide. From bustling cities to tranquil beaches.',
            'published': True,
            'date': '2025-01-25',
            'tags': ['Travel', 'Asia', 'Adventure', 'Culture'],
            'views': 2100,
            'reading_time': '10 min'
        },
        {
            'id': 4,
            'title': 'Understanding Machine Learning Basics',
            'author': 'Dr. James Wilson',
            'category': 'Education',
            'content': 'Machine learning demystified. Learn the fundamental concepts and algorithms that power modern AI applications.',
            'published': False,
            'date': '2025-01-28',
            'tags': ['AI', 'Machine Learning', 'Education', 'Technology'],
            'views': 0,
            'reading_time': '12 min'
        },
        {
            'id': 5,
            'title': 'Top 10 Photography Tips for Beginners',
            'author': 'Lisa Anderson',
            'category': 'Photography',
            'content': 'Transform your photography skills with these essential tips. From composition to lighting, master the basics.',
            'published': True,
            'date': '2025-02-01',
            'tags': ['Photography', 'Tutorial', 'Beginner', 'Tips'],
            'views': 1500,
            'reading_time': '7 min'
        },
    ]
    
    # Find the post with matching ID
    post = next((p for p in all_posts if p['id'] == post_id), None)
    
    # If post not found, raise 404
    if post is None:
        raise Http404(f"Post {post_id} not found")
    
    # Post found! Show details
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)
```

**Explanation:**
```
This view demonstrates several important concepts:

1. Receiving URL parameters:
   def post_detail(request, post_id):
                            ↑
                       Matches <int:post_id> from URL
                       Comes as integer already!

2. Simulating database lookup:
   for p in all_posts:
       if p['id'] == post_id:
           post = p
   
   On Day 3, this becomes:
   post = Post.objects.get(id=post_id)

3. Error handling with Http404:
   if post is None:
       raise Http404("Post not found")
   
   Django automatically shows a 404 error page
   Professional error handling!

4. Context dictionary:
   context = {'post': post}
   
   Pass the found post to template for display.
```

---

#### **1.4 Create Post Detail Template**

**Create blog/templates/blog/post_detail.html:**

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ post.title }} - BlogHub</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/">� BlogHub</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="/posts/">Posts</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/about/">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/contact/">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    
    <!-- Breadcrumb Navigation -->
    <div class="container mt-3">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="/">Home</a></li>
                <li class="breadcrumb-item"><a href="/posts/">Posts</a></li>
                <li class="breadcrumb-item active" aria-current="page">{{ post.title }}</li>
            </ol>
        </nav>
    </div>
    
    <!-- Post Details -->
    <div class="container my-5">
        <div class="row">
            <!-- Post Cover Image Placeholder -->
            <div class="col-md-12">
                <div class="card mb-4">
                    <div class="card-body text-center" style="min-height: 300px; display: flex; align-items: center; justify-content: center; background: #f8f9fa;">
                        <h1 style="font-size: 8rem;">�</h1>
                    </div>
                </div>
            </div>
            
            <!-- Post Information -->
            <div class="col-md-12">
                <h1 class="display-5">{{ post.title }}</h1>
                
                <!-- Category Badge and Meta Info -->
                <p class="text-muted">
                    <span class="badge bg-secondary">{{ post.category }}</span>
                    | By {{ post.author }} | {{ post.date }} | {{ post.reading_time }} read | {{ post.views }} views
                </p>
                
                <!-- Published Status -->
                <div class="mb-3">
                    {% if post.published %}
                        <span class="badge bg-success">Published</span>
                    {% else %}
                        <span class="badge bg-warning">Draft</span>
                    {% endif %}
                </div>
                
                <!-- Content -->
                <div class="card mb-4">
                    <div class="card-body">
                        <h5 class="card-title">Article Content</h5>
                        <p class="card-text">{{ post.content }}</p>
                    </div>
                </div>
                
                <!-- Tags -->
                <div class="card mb-4">
                    <div class="card-body">
                        <h5 class="card-title">Tags</h5>
                        <div>
                            {% for tag in post.tags %}
                                <span class="badge bg-info me-2">{{ tag }}</span>
                            {% endfor %}
                        </div>
                    </div>
                </div>
                
                <!-- Engagement Buttons -->
                {% if post.published %}
                    <button class="btn btn-primary btn-lg w-100 mb-2">
                        � Like this Post
                    </button>
                    <button class="btn btn-outline-secondary w-100">
                        🔖 Bookmark for Later
                    </button>
                {% else %}
                    <button class="btn btn-secondary btn-lg w-100" disabled>
                        Currently Unavailable
                    </button>
                {% endif %}
            </div>
        </div>
        
        <!-- Back to Posts Link -->
        <div class="mt-5">
            <a href="/posts/" class="btn btn-outline-primary">← Back to All Posts</a>
        </div>
    </div>
    
    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3 mt-5">
        <p class="mb-0">&copy; 2025 BlogHub. All rights reserved.</p>
    </footer>
    
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
</body>
</html>
```

---

#### **1.5 Update Posts Page with Post Links**

**Modify blog/templates/blog/posts.html:**

Find the post cards section and update the footer:

```html
{% for post in posts %}
<div class="col-lg-4 col-md-6 mb-4">
    <div class="card h-100">
        <div class="card-body">
            <h5 class="card-title">{{ post.title }}</h5>
            <p class="text-muted">{{ post.category }} | By {{ post.author }}</p>
            <p class="text-muted small">{{ post.date }} | {{ post.reading_time }} read</p>
            <p class="card-text">{{ post.excerpt }}</p>
            
            {% if post.published %}
                <span class="badge bg-success">✓ Published</span>
            {% else %}
                <span class="badge bg-warning">Draft</span>
            {% endif %}
        </div>
        <div class="card-footer">
            <!-- ⭐ New: Link to post detail page -->
            <a href="/post/{{ post.id }}/" class="btn btn-primary btn-sm w-100">
                Read More
            </a>
        </div>
    </div>
</div>
{% endfor %}
```

---

#### **1.6 Update Posts View with Post IDs**

**Modify blog/views.py - posts function:**

Make sure each post has an 'id' field:

```python
def posts(request):
    """Posts page view - display all blog posts"""
    posts_list = [
        {
            'id': 1,  # ⭐ Make sure all posts have IDs!
            'title': 'Getting Started with Django',
            'author': 'Sarah Johnson',
            'category': 'Technology',
            'excerpt': 'Learn the fundamentals of Django development',
            'date': '2025-01-15',
            'published': True,
            'reading_time': '8 min'
        },
        {
            'id': 2,
            'title': 'Mastering CSS Grid Layout',
            'author': 'Mike Chen',
            'category': 'Design',
            'excerpt': 'CSS Grid revolutionized responsive design',
            'date': '2025-01-20',
            'published': True,
            'reading_time': '6 min'
        },
        {
            'id': 3,
            'title': 'Traveling Through Southeast Asia',
            'author': 'Emma Rodriguez',
            'category': 'Travel',
            'excerpt': 'Discover hidden gems of Southeast Asia',
            'date': '2025-01-25',
            'published': True,
            'reading_time': '10 min'
        },
        {
            'id': 4,
            'title': 'Understanding Machine Learning Basics',
            'author': 'Dr. James Wilson',
            'category': 'Education',
            'excerpt': 'Machine learning concepts demystified',
            'date': '2025-01-28',
            'published': False,
            'reading_time': '12 min'
        },
        {
            'id': 5,
            'title': 'Top 10 Photography Tips',
            'author': 'Lisa Anderson',
            'category': 'Photography',
            'excerpt': 'Transform your photography skills',
            'date': '2025-02-01',
            'published': True,
            'reading_time': '7 min'
        },
        {
            'id': 6,
            'title': 'Building REST APIs with Django',
            'author': 'Carlos Martinez',
            'category': 'Technology',
            'excerpt': 'Create powerful REST APIs using Django REST Framework',
            'date': '2025-02-05',
            'published': True,
            'reading_time': '15 min'
        },
        {
            'id': 7,
            'title': 'Minimalist Interior Design Trends',
            'author': 'Sophie Laurent',
            'category': 'Design',
            'excerpt': 'Less is more in modern interior design',
            'date': '2025-02-08',
            'published': False,
            'reading_time': '5 min'
        },
        {
            'id': 8,
            'title': 'Healthy Meal Prep for Busy Professionals',
            'author': 'Jennifer Lee',
            'category': 'Health',
            'excerpt': 'Save time and eat healthy with these meal prep tips',
            'date': '2025-02-10',
            'published': True,
            'reading_time': '9 min'
        },
    ]
    
    context = {
        'page_title': 'All Blog Posts',
        'posts': posts_list,
        'total_posts': len(posts_list),
    }
    return render(request, 'blog/posts.html', context)
```

---

#### **1.7 Test Dynamic URLs**

```bash
# Run server
python manage.py runserver

# Test in browser:
http://127.0.0.1:8000/posts/
# Click "Read More" on any post

# Or directly visit:
http://127.0.0.1:8000/post/1/   # Getting Started with Django
http://127.0.0.1:8000/post/2/   # Mastering CSS Grid Layout
http://127.0.0.1:8000/post/999/ # Not found (404 error)
http://127.0.0.1:8000/post/abc/ # Invalid (404 - doesn't match int pattern)
```

---

### **🎬 Break (10 minutes)**

---

### **Part 2: Path Converters & Named URLs**

#### 🎯 **Goal**: Use path converters for type-safe URLs and implement named URL patterns

---

#### **2.1 Path Converters Deep Dive**

**Built-in Path Converters:**

```python
str    - Matches any non-empty string (excluding '/')
       - Default if you don't specify
       - <username> is same as <str:username>
       - Example: /author/john/ → username="john"

int    - Matches zero or any positive integer
       - <int:id> only matches: 1, 2, 100, 999, etc.
       - Does NOT match: abc, -5, 1.5
       - Example: /post/5/ → post_id=5

slug   - Matches ASCII letters, numbers, hyphens, underscores
       - <slug:slug> matches: hello-world, my_post_123
       - Does NOT match: Hello World (space), "hello!" (special chars)
       - Example: /article/django-tutorial/ → slug="django-tutorial"

uuid   - Matches UUID (Universally Unique Identifier)
       - <uuid:id> matches: 550e8400-e29b-41d4-a716-446655440000
       - Used for secure, unpredictable IDs
       - Example: /verify/550e8400-e29b-41d4-a716-446655440000/

path   - Matches any string INCLUDING '/'
       - <path:file_path> matches: docs/file.pdf, a/b/c/d.txt
       - Use for file paths or nested routes
       - Example: /docs/api/users.html → file_path="api/users.html"
```

**🎨 See This Visual:**
```
Path Converter Examples:

┌──────────────────────────────────────────────────┐
│  Pattern                    Matches              │
├──────────────────────────────────────────────────┤
│  <int:id>                   1, 42, 999           │
│                             NOT: abc, -5         │
├──────────────────────────────────────────────────┤
│  <str:username>             alice, john123       │
│                             NOT: (empty)         │
├──────────────────────────────────────────────────┤
│  <slug:post_slug>           my-blog-post-123     │
│                             NOT: my blog post    │
├──────────────────────────────────────────────────┤
│  <uuid:token>               550e8400-e29b...     │
│                             NOT: 123             │
├──────────────────────────────────────────────────┤
│  <path:file>                docs/readme.txt      │
│                             a/b/c/d.pdf          │
└──────────────────────────────────────────────────┘
```

---

#### **2.2 Named URLs - The Proper Way**

```
Problem: Hardcoded URLs everywhere!
  <a href="/posts/">Posts</a>
  <a href="/post/5/">Post 5</a>
  
What if URLs change?
  /posts/ → /blog-posts/
  /post/5/ → /articles/5/
  
Must update EVERY template! 😱

Solution: Named URLs!
  <a href="{% url 'blog:posts' %}">Posts</a>
  <a href="{% url 'blog:post_detail' 5 %}">Post 5</a>
  
URL changes? Just update urls.py! All links work! ✅
```

**How Named URLs Work:**

```python
# urls.py
path('post/<int:post_id>/', views.post_detail, name='post_detail')
                                                            ↑
                                                        URL name

# In template:
{% url 'blog:post_detail' 5 %}
 ↑              ↑         ↑
 │              │         └─ Arguments (post_id=5)
 │              └─ URL name from urls.py
 └─ Template tag

# Django generates:
/post/5/
```

**🎨 See This Visual:**
```
Named URL System:

urls.py (blog/urls.py):
  app_name = 'blog'
  path('post/<int:id>/', views.method_name, name='post_detail')
                                                         ↑
                                                   Give it a name

Template:
  {% url 'blog:post_detail' post.id %}
   ↑            ↑             ↑
   │            │             └─ Variable (5)
   │            └─ Name from urls.py
   └─ Template tag to generate URL

Django generates the correct URL:
  /post/5/

If URL pattern changes to:
  path('article/<int:id>/', ...)
  
Django automatically generates:
  /article/5/
  
Templates don't need updating! Magic! ✨
```

---

#### **2.3 Update All Templates with Named URLs**

**Update blog/templates/blog/posts.html:**

```html
<!-- BEFORE (hardcoded URLs): -->
<a href="/post/{{ post.id }}/" class="btn btn-primary btn-sm w-100">
    Read More
</a>

<!-- AFTER (named URLs): -->
<a href="{% url 'blog:post_detail' post.id %}" class="btn btn-primary btn-sm w-100">
    Read More
</a>
```

**Update blog/templates/blog/post_detail.html:**

```html
<!-- Update navigation links -->
<ul class="navbar-nav ms-auto">
    <li class="nav-item">
        <a class="nav-link" href="{% url 'blog:home' %}">Home</a>
    </li>
    <li class="nav-item">
        <a class="nav-link active" href="{% url 'blog:posts' %}">Posts</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="{% url 'blog:about' %}">About</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="{% url 'blog:contact' %}">Contact</a>
    </li>
</ul>

<!-- Update breadcrumb -->
<ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="{% url 'blog:home' %}">Home</a></li>
    <li class="breadcrumb-item"><a href="{% url 'blog:posts' %}">Posts</a></li>
    <li class="breadcrumb-item active">{{ post.title }}</li>
</ol>

<!-- Update back button -->
<a href="{% url 'blog:posts' %}" class="btn btn-outline-primary">
    ← Back to All Posts
</a>
```

**Explanation of {% url %} syntax:**
```
Basic syntax:
  {% url 'app_name:url_name' %}

With positional arguments:
  {% url 'blog:post_detail'  post.id post.category.id %}
                                  ↑                ↑
                                 1st              2nd

With keyword arguments:
  {% url 'blog:post_detail' post_id=post.id %}

With variables:
  {% url 'blog:post_detail' post.id %}
                                 ↑
                       Uses value from context

Multiple Mix arguments:
  {% url 'blog:category_post' post_category=post.category.id post.id %}
  # For URL: category/<str:cat>/post/<int:id>/
  # must have keyword args before positional!

Why use app_name prefix?
  blog:home vs users:home
    ↑             ↑
  Different apps might have URLs with same name!
  Namespace prevents conflicts.
```

---

#### **2.4 URL Reversing in Views**

```
Named URLs aren't just for templates!
You can use them in views too with reverse() and redirect()!
```

**Example - Add to blog/views.py:**

```python
from django.shortcuts import render, redirect
from django.urls import reverse

def redirect_example(request):
    """
    Example of redirecting using named URLs
    """
    # Method 1: Direct redirect with named URL
    return redirect('blog:home')
    
    # Method 2: redirect with arguments
    post_id = 5
    return redirect('blog:post_detail', post_id=post_id)
    
    # Method 3: Using reverse() to generate URL first
    url = reverse('blog:post_detail', args=[post_id])
    url = reverse('blog:post_detail', kwargs={'post_id': 5})
    # url = '/post/5/'
    return redirect(url)
```

---

### **❓ Common Questions - Path Converters & Named URLs:**

**Q: "What's the difference between <post_id> and <int:post_id>?"**
A: `<post_id>` captures as string (default str converter). `<int:post_id>` captures as integer and validates it's a number. Always use appropriate converter!

**Q: "Can I use multiple converters in one URL?"**
A: Yes! Example: `path('author/<str:author_name>/post/<int:id>/', ...)` captures both author_name (string) and id (integer).

**Q: "Why use named URLs? Typing {% url %} is longer than /posts/!"**
A: Named URLs are maintainable. If you change URL patterns, all links automatically update. In large projects, this saves hours of work!

**Q: "What if I forget to add name= to a path()?"**
A: You can't use {% url %} for it. Always add name= to every URL pattern. It's a Django best practice.

**Q: "Can I create custom path converters?"**
A: Yes! Advanced topic. You can create converters for custom patterns like ISBN numbers, phone numbers, etc.

**Q: "What's the difference between redirect() and reverse()?"**
A: `redirect()` sends HTTP redirect response. `reverse()` just generates URL string. Use redirect() in views to redirect users, reverse() when you just need the URL.

---

### **🎬 Break (10 minutes)**

---

### **Part 3: Advanced Views & HTTP Methods**

#### 🎯 **Goal**: Handle different HTTP methods and use Django shortcuts

---

#### **3.1 HTTP Methods Overview**

```
HTTP Methods are like "verbs" for web requests:
  GET    - Retrieve data (viewing pages, searching)
  POST   - Submit data (forms, create new records)
  PUT    - Update entire resource
  PATCH  - Update part of resource
  DELETE - Delete resource

In Django views:
  - request.method tells you which HTTP method was used
  - We can handle different methods differently!
```

**🎨 See This Visual:**
```
HTTP Methods in Blogging:

┌────────────────────────────────────────────────┐
│  Action                   Method   URL         │
├────────────────────────────────────────────────┤
│  View posts              GET      /posts/      │
│  View one post           GET      /post/5/     │
│  Search posts            GET      /search/?q=  │
│  Like post               POST     /post/like/  │
│  Bookmark post           POST     /post/save/  │
│  Add comment             POST     /comment/add/│
│  Subscribe               POST     /subscribe/  │
│  Submit contact form     POST     /contact/    │
└────────────────────────────────────────────────┘

GET  = Safe, no changes, can bookmark, can refresh
POST = Makes changes, can't bookmark, ask before refresh
```

---

#### **3.2 Handling POST Requests**

**Add to blog/views.py:**

```python
from django.views.decorators.http import require_POST
from django.shortcuts import redirect

@require_POST
def like_post(request, post_id):
    """
    Like a blog post
    Only accepts POST requests (security best practice)
    
    Decorator @require_POST ensures only POST requests reach this function
    GET, PUT, DELETE → 405 Method Not Allowed
    """
    # In a real app, we would:
    # 1. Get user from request
    # 2. Get or create Like object
    # 3. Update post like count
    # 4. Save to database
    
    # For now, just simulate:
    print(f"✓ Liking post {post_id}")
    
    # Redirect back to post detail page
    # This follows the Post-Redirect-Get (PRG) pattern
    return redirect('blog:post_detail', post_id=post_id)
```

**Add URL for like_post:**

```python
# blog/urls.py
urlpatterns = [
    # ... existing patterns ...
    path('post/like/<int:post_id>/', views.like_post, name='like_post'),
]
```

**Update post_detail.html to use it:**

```html
<!-- Find the "Like Post" button and update -->
{% if post.published %}
    <form method="POST" action="{% url 'blog:like_post' post.id %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-primary btn-lg w-100 mb-2">
            ❤️ Like Post
        </button>
    </form>
{% else %}
    <button class="btn btn-secondary btn-lg w-100" disabled>
        Draft - Not Published
    </button>
{% endif %}
```

**Explanation:**
```
HTML Form for POST request:
  <form method="POST" action="{% url 'blog:like_post' post.id %}">
         ↑             ↑
         │             └─ Where to send data (like_post view)
         └─ HTTP method (POST)
  
  {% csrf_token %}
    ↓
    CSRF protection (Django security feature)
    Prevents Cross-Site Request Forgery attacks
    Django requires this for all POST forms!
    Generates hidden input: <input type="hidden" name="csrfmiddlewaretoken" value="...">
    
  <button type="submit">Like Post</button>
    ↓
    Clicking submits the form via POST
    
Flow:
  1. User clicks "Like Post"
  2. Browser sends POST to /post/like/5/
  3. Django routes to like_post view
  4. View processes (adds like)
  5. Redirects back to post page
  6. Browser shows post page with updated like count
```

---

#### **3.3 Django Shortcuts Summary**

```python
from django.shortcuts import render, redirect, get_object_or_404

# 1. render() - Load template with context
render(request, 'template.html', context)
# Most common! Returns HttpResponse with rendered template

# 2. redirect() - Redirect to another URL
redirect('blog:home')              # Named URL
redirect('/posts/')                # Direct URL
redirect('https://google.com')     # External URL

# 3. get_object_or_404() - Get from database or show 404
# (We'll use this heavily on Day 3 with models)
post = get_object_or_404(Post, id=post_id)
# If post exists: returns post object
# If not: automatically raises Http404 (shows 404 page)
```

---

### **❓ Common Questions - HTTP Methods & Views:**

**Q: "What's CSRF and why do I need {% csrf_token %}?"**
A: CSRF (Cross-Site Request Forgery) is an attack where a malicious site tricks your browser into making requests. {% csrf_token %} generates a secret token that validates the form came from your site. Django requires it for all POST forms.

**Q: "Can I have one view handle both GET and POST?"**
A: Yes! Common pattern:
```python
def my_view(request):
    if request.method == 'POST':
        # Process form
    else:  # GET
        # Show form
```

**Q: "Why redirect after POST instead of just rendering?"**
A: If you render after POST, refreshing the page re-submits the form! Redirect prevents duplicate submissions. This is called the Post-Redirect-Get (PRG) pattern.

**Q: "What happens if I forget {% csrf_token %}?"**
A: Django returns 403 Forbidden error. CSRF protection is mandatory for POST requests (unless you explicitly disable it, which is dangerous!).

---

## 📚 **SESSION 2: Template Inheritance & Advanced Features**

---

### **Part 4: Template Inheritance**

#### 🎯 **Goal**: Create reusable base templates using Django's template inheritance

---

#### **4.1 The Problem: Code Duplication**

```
Right now, every template has:
  - Full HTML structure (<!DOCTYPE>, <html>, <head>, <body>)
  - Bootstrap CSS/JS links
  - Navigation bar
  - Footer
  
home.html:         200 lines (150 lines repeated)
about.html:        180 lines (150 lines repeated)
contact.html:      190 lines (150 lines repeated)
posts.html:        250 lines (150 lines repeated)
post_detail.html:  280 lines (150 lines repeated)

Total: 750+ lines of repeated code! 😱

If we want to change navigation:
  Update 5 files! ❌

If we add new navigation link:
  Update 5 files! ❌

This is NOT maintainable!
```

**🎨 See This Visual:**
```
Current Approach (BAD):

home.html:                about.html:              contact.html:
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ <!DOCTYPE html> │      │ <!DOCTYPE html> │      │ <!DOCTYPE html> │
│ <head>          │      │ <head>          │      │ <head>          │
│   Bootstrap     │      │   Bootstrap     │      │   Bootstrap     │
│ </head>         │      │ </head>         │      │ </head>         │
│ <body>          │      │ <body>          │      │ <body>          │
│   <nav>...</nav>│      │   <nav>...</nav>│      │   <nav>...</nav>│
│   HOME CONTENT  │      │   ABOUT CONTENT │      │   CONTACT       │
│   <footer>...   │      │   <footer>...   │      │   <footer>...   │
│ </body>         │      │ </body>         │      │ </body>         │
└─────────────────┘      └─────────────────┘      └─────────────────┘

                       Repeated code! ❌
```

---

#### **4.2 Template Inheritance Solution**

```
Django Template Inheritance:
  - Create ONE base template with common structure
  - Child templates "extend" base
  - Only write unique content in child templates
  - Change base = all pages update automatically!

Like object-oriented programming for HTML!
```

**🎨 See This Visual:**
```
Template Inheritance (GOOD):

base.html (Parent):
┌────────────────────────────────────┐
│ <!DOCTYPE html>                    │
│ <html>                             │
│ <head>                             │
│   <title>{% block title %}</title> │  ← Child fills this
│   Bootstrap CSS                    │
│ </head>                            │
│ <body>                             │
│   <nav>...</nav>                   │
│                                    │
│   {% block content %}              │  ← Child fills this
│   {% endblock %}                   │
│                                    │
│   <footer>...</footer>             │
│ </body>                            │
│ </html>                            │
└────────────────────────────────────┘

home.html (Child):               about.html (Child):
┌──────────────────────┐         ┌──────────────────────┐
│ {% extends "base" %} │         │ {% extends "base" %} │
│                      │         │                      │
│ {% block content %}  │         │ {% block content %}  │
│   HOME CONTENT       │         │   ABOUT CONTENT      │
│ {% endblock %}       │         │ {% endblock %}       │
└──────────────────────┘         └──────────────────────┘

Result: DRY (Don't Repeat Yourself)!
Change navigation in base.html → all pages update! ✅
```

---

#### **4.3 Create Base Template**

**Create blog/templates/blog/base.html:**

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Page title (child templates can override) -->
    <title>{% block title %}BlogHub - Share Your Stories{% endblock %}</title>
    
    <!-- Bootstrap 5 CSS -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    
    <!-- Extra CSS (child templates can add more CSS) -->
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navigation Bar (same for all pages) -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'blog:home' %}">� BlogHub</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'blog:home' %}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'blog:posts' %}">Posts</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'blog:about' %}">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'blog:contact' %}">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    
    <!-- Main Content (child templates fill this) -->
    <main>
        {% block content %}
        <!-- Default content if child doesn't override -->
        <div class="container my-5">
            <h1>Welcome to BlogHub</h1>
            <p>This is the default content.</p>
        </div>
        {% endblock %}
    </main>
    
    <!-- Footer (same for all pages) -->
    <footer class="bg-dark text-white mt-5 py-4">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <h5>BlogHub</h5>
                    <p>Share your stories with the world</p>
                </div>
                <div class="col-md-4">
                    <h5>Quick Links</h5>
                    <ul class="list-unstyled">
                        <li><a href="{% url 'blog:home' %}" class="text-white">Home</a></li>
                        <li><a href="{% url 'blog:posts' %}" class="text-white">Posts</a></li>
                        <li><a href="{% url 'blog:about' %}" class="text-white">About</a></li>
                        <li><a href="{% url 'blog:contact' %}" class="text-white">Contact</a></li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <h5>Follow Us</h5>
                    <p>Facebook | Twitter | Instagram</p>
                </div>
            </div>
            <hr class="bg-white">
            <div class="text-center">
                <p class="mb-0">&copy; 2025 BlogHub. All rights reserved.</p>
            </div>
        </div>
    </footer>
    
    <!-- Bootstrap 5 JS -->
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    
    <!-- Extra JS (child templates can add more JS) -->
    {% block extra_js %}{% endblock %}
</body>
</html>
```

**Explanation of {% block %}:**
```
{% block block_name %}
  Default content (optional)
{% endblock %}

Purpose:
  - Defines a "slot" that child templates can fill
  - Child templates override the block content
  - If child doesn't override, uses default

Common blocks:
  {% block title %} - Page title
  {% block content %} - Main page content
  {% block extra_css %} - Additional CSS files
  {% block extra_js %} - Additional JavaScript files
  {% block header %} - Custom header content
  {% block footer %} - Custom footer content

You can have as many blocks as you want!
```

---

#### **4.4 Update Home Template**

**Modify blog/templates/blog/home.html:**

```html
{% extends 'blog/base.html' %}
{% load static %}

{% block title %}Home - BlogHub{% endblock %}

{% block content %}
<!-- Hero Section -->
<div class="container-fluid bg-primary text-white py-5">
    <div class="container">
        <h1 class="display-4">� Welcome to {{ site_name }}!</h1>
        <p class="lead">{{ tagline }}</p>
        <a href="{% url 'blog:posts' %}" class="btn btn-light btn-lg">Explore Posts</a>
    </div>
</div>

<!-- Featured Post Alert (Conditional) -->
{% if is_featured_active %}
<div class="container mt-4">
    <div class="alert alert-success border-start border-5 border-success">
        <h2 class="alert-heading">⭐ FEATURED POST!</h2>
        <p class="mb-0">Check out our latest featured article! Don't miss it!</p>
    </div>
</div>
{% endif %}

<!-- Blog Statistics -->
<div class="container my-4">
    <div class="card bg-light">
        <div class="card-body">
            <h2 class="card-title">Our Blog Statistics</h2>
            <div class="row text-center mt-3">
                <div class="col-md-4">
                    <h3 class="text-primary">{{ total_posts }}</h3>
                    <p class="text-muted">Published Posts</p>
                </div>
                <div class="col-md-4">
                    <h3 class="text-primary">{{ categories_count }}</h3>
                    <p class="text-muted">Categories</p>
                </div>
                <div class="col-md-4">
                    <h3 class="text-primary">2025</h3>
                    <p class="text-muted">Blogging Since</p>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Why Read Our Blog Section -->
<div class="container my-5">
    <h2 class="text-center mb-4">Why Read Our Blog?</h2>
    <div class="row">
        {% for benefit in benefits %}
        <div class="col-md-6 col-lg-3 mb-3">
            <div class="card h-100 text-center">
                <div class="card-body">
                    <h3>{{ benefit.icon }}</h3>
                    <h5 class="card-title">{{ benefit.title }}</h5>
                    <p class="card-text">{{ benefit.description }}</p>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

<!-- Popular Categories -->
<div class="container my-5">
    <h2 class="text-center mb-4">Popular Categories</h2>
    <div class="row">
        {% for category in featured_categories %}
        <div class="col-md-6 col-lg-4 mb-3">
            <div class="list-group">
                <a href="#" class="list-group-item list-group-item-action">
                    {{ category }}
                </a>
            </div>
        </div>
        {% endfor %}
    </div>
    <div class="text-center mt-4">
        <a href="{% url 'blog:about' %}" class="btn btn-primary">Learn more about {{ site_name }}</a>
    </div>
</div>
{% endblock %}
```

**What changed:**
```
BEFORE:
  - Full HTML structure (<!DOCTYPE>, <html>, <head>, <body>)
  - Navigation
  - Content
  - Footer
  - Bootstrap links
  
  Total: 200+ lines

AFTER:
  {% extends 'blog/base.html' %}
  {% block content %}
    ... only unique content ...
  {% endblock %}
  
  Total: ~100 lines
  
Removed:
  ✓ HTML boilerplate
  ✓ Navigation (inherited from base)
  ✓ Footer (inherited from base)
  ✓ Bootstrap CSS/JS (inherited from base)

Benefits:
  ✓ Shorter, cleaner code
  ✓ Only unique content
  ✓ Changes to navigation/footer happen in ONE place
  ✓ Easier to maintain
```

---

#### **4.5 Update Posts Template**

**Modify blog/templates/blog/posts.html:**

```html
{% extends 'blog/base.html' %}
{% load static %}

{% block title %}{{ page_title }} - BlogHub{% endblock %}

{% block content %}
<!-- Header -->
<div class="bg-warning text-dark py-4">
    <div class="container">
        <h1>� {{ page_title }}</h1>
        <p class="lead">Discover our latest articles and stories</p>
    </div>
</div>

<!-- Posts Grid -->
<div class="container my-5">
    <div class="row">
        {% for post in posts %}
        <div class="col-lg-4 col-md-6 mb-4">
            <div class="card h-100">
                <div class="card-body">
                    <h5 class="card-title">{{ post.title }}</h5>
                    <p class="text-muted">By {{ post.author }} | {{ post.category }}</p>
                    <p class="card-text">{{ post.excerpt }}</p>
                    <small class="text-muted">{{ post.date }} • {{ post.reading_time }} read</small>
                    
                    {% if post.published %}
                        <span class="badge bg-success">✓ Published</span>
                    {% else %}
                        <span class="badge bg-secondary">Draft</span>
                    {% endif %}
                </div>
                <div class="card-footer">
                    <a href="{% url 'blog:post_detail' post.id %}" class="btn btn-primary btn-sm w-100">
                        Read More
                    </a>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
    
    <!-- Posts Count -->
    <div class="text-center mt-4">
        <p class="lead">Showing {{ total_posts }} posts</p>
    </div>
</div>
{% endblock %}
```

---

#### **4.6 Update About Template**

**Modify blog/templates/blog/about.html:**

```html
{% extends 'blog/base.html' %}
{% load static %}

{% block title %}About Us - BlogHub{% endblock %}

{% block content %}
<!-- Header -->
<div class="bg-dark text-white py-4">
    <div class="container">
        <h1>About {{ company_name }}</h1>
        <p class="lead">Sharing stories since {{ founded_year }}</p>
    </div>
</div>

<!-- Main Content -->
<div class="container my-5">
    <div class="row">
        <div class="col-lg-8">
            <h2>Our Mission</h2>
            <p class="lead">{{ mission }}</p>
            
            <h2 class="mt-4">Our Writers</h2>
            <p>We're a community of <strong>{{ team_size }}</strong> passionate writers and contributors.</p>
            
            <h2 class="mt-4">Our Values</h2>
            <div class="row mt-3">
                {% for value in values %}
                <div class="col-md-6 col-lg-3 mb-3">
                    <div class="card bg-light h-100">
                        <div class="card-body text-center">
                            <h5 class="card-title">{{ value }}</h5>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
        
        <div class="col-lg-4">
            <div class="card bg-light">
                <div class="card-body">
                    <h4 class="card-title">Quick Stats</h4>
                    <hr>
                    <p><strong>Founded:</strong> {{ founded_year }}</p>
                    <p><strong>Writers:</strong> {{ team_size }} contributors</p>
                    <p><strong>Mission:</strong> {{ mission }}</p>
                </div>
            </div>
            
            <div class="card mt-3 bg-primary text-white">
                <div class="card-body text-center">
                    <h5>Ready to Read?</h5>
                    <a href="{% url 'blog:home' %}" class="btn btn-light mt-2">Go to Homepage</a>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

---

#### **4.7 Update Contact Template**

**Modify blog/templates/blog/contact.html:**

```html
{% extends 'blog/base.html' %}
{% load static %}

{% block title %}Contact Us - BlogHub{% endblock %}

{% block content %}
<!-- Header -->
<div class="bg-success text-white py-4">
    <div class="container">
        <h1>📞 Contact Us</h1>
        <p class="lead">We're here to help! Reach out anytime.</p>
    </div>
</div>

<!-- Contact Information -->
<div class="container my-5">
    <div class="row">
        <div class="col-md-6 mb-3">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">📧 Email</h5>
                    <p class="card-text">{{ email }}</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-6 mb-3">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">📱 Phone</h5>
                    <p class="card-text">{{ phone }}</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-6 mb-3">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">📍 Address</h5>
                    <p class="card-text">{{ address }}</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-6 mb-3">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">🕐 Business Hours</h5>
                    <p class="card-text">{{ business_hours }}</p>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Departments -->
    <div class="mt-5">
        <h2 class="mb-4">📋 Departments</h2>
        <div class="row">
            {% for dept in departments %}
            <div class="col-md-4 mb-3">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ dept.name }}</h5>
                        <p class="card-text">{{ dept.email }}</p>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    
    <!-- Social Media -->
    <div class="mt-5">
        <h2 class="mb-4">🌐 Follow Us</h2>
        <div class="row">
            {% for social in social_media %}
            <div class="col-md-4 mb-3">
                <div class="card text-center">
                    <div class="card-body">
                        <h5 class="card-title">{{ social.platform }}</h5>
                        <a href="https://{{ social.link }}" class="btn btn-primary btn-sm">Visit</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</div>
{% endblock %}
```

---

#### **4.8 Update Post Detail Template**

**Modify blog/templates/blog/post_detail.html:**

```html
{% extends 'blog/base.html' %}
{% load static %}

{% block title %}{{ post.title }} - BlogHub{% endblock %}

{% block content %}
<!-- Breadcrumb Navigation -->
<div class="container mt-3">
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="{% url 'blog:home' %}">Home</a></li>
            <li class="breadcrumb-item"><a href="{% url 'blog:posts' %}">Posts</a></li>
            <li class="breadcrumb-item active" aria-current="page">{{ post.title }}</li>
        </ol>
    </nav>
</div>

<!-- Post Details -->
<div class="container my-5">
    <div class="row">
        <!-- Post Featured Image Placeholder -->
        <div class="col-md-12 mb-4">
            <div class="card">
                <div class="card-body text-center" style="min-height: 300px; display: flex; align-items: center; justify-content: center; background: #f8f9fa;">
                    <h1 style="font-size: 8rem;">�</h1>
                </div>
            </div>
        </div>
    </div>
    
    <div class="row">
        <!-- Post Content -->
        <div class="col-md-8">
            <h1 class="display-5">{{ post.title }}</h1>
            
            <!-- Post Meta -->
            <p class="text-muted">
                By <strong>{{ post.author }}</strong> | {{ post.date }} | {{ post.reading_time }} read
            </p>
            <p class="text-muted">
                <span class="badge bg-secondary">{{ post.category }}</span>
            </p>
            
            <!-- Post Content -->
            <div class="card mb-4">
                <div class="card-body">
                    <p class="card-text">{{ post.content }}</p>
                </div>
            </div>
            
            <!-- Tags -->
            <div class="card mb-4">
                <div class="card-body">
                    <h5 class="card-title">Tags</h5>
                    <div>
                        {% for tag in post.tags %}
                            <span class="badge bg-info">{{ tag }}</span>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Sidebar -->
        <div class="col-md-4">
            <!-- Post Stats -->
            <div class="card mb-4">
                <div class="card-body">
                    <h5 class="card-title">Post Stats</h5>
                    <p><strong>Views:</strong> {{ post.views }}</p>
                    <p><strong>Reading Time:</strong> {{ post.reading_time }}</p>
                    <p><strong>Category:</strong> {{ post.category }}</p>
                </div>
            </div>
            
            <!-- Like Post Button -->
            {% if post.published %}
                <form method="POST" action="{% url 'blog:like_post' post.id %}">
                    {% csrf_token %}
                    <button type="submit" class="btn btn-primary btn-lg w-100 mb-2">
                        ❤️ Like Post
                    </button>
                </form>
                <button class="btn btn-outline-secondary w-100">
                    🔖 Bookmark
                </button>
            {% else %}
                <button class="btn btn-secondary btn-lg w-100" disabled>
                    Draft - Not Published
                </button>
            {% endif %}
        </div>
    </div>
    
    <!-- Back to Posts Link -->
    <div class="mt-5">
        <a href="{% url 'blog:posts' %}" class="btn btn-outline-primary">← Back to All Posts</a>
    </div>
</div>
{% endblock %}
```

---

**Test Everything:**

```bash
# Run server
python manage.py runserver

# Visit all pages and verify:
http://127.0.0.1:8000/              # Home
http://127.0.0.1:8000/posts/        # Posts
http://127.0.0.1:8000/about/        # About
http://127.0.0.1:8000/contact/      # Contact
http://127.0.0.1:8000/post/1/       # Post detail

# All pages should now:
# ✓ Use the same navigation and footer (from base.html)
# ✓ Have consistent Bootstrap styling
# ✓ Show proper page titles in browser tabs
# ✓ Display correctly on all screen sizes (responsive)
# ✓ Have working links between pages

# Try making a change to base.html:
# - Update the navbar brand text
# - Add a new link to navigation
# - Change footer text
# Then refresh any page - all pages update automatically!

# This is the power of template inheritance! 🎉
```

**What You Should See:**

1. **Consistent Header/Footer**: All pages have identical navigation and footer
2. **Unique Content**: Each page has its own content in the main area
3. **Bootstrap Working**: Responsive design, buttons, cards all styled
4. **Named URLs**: All links use {% url %} tags (check page source)
5. **No Code Duplication**: Check each template - they're much shorter now!

**Success Criteria:**
- ✅ Navigation links work on all pages
- ✅ All pages use base.html template
- ✅ Post detail pages load correctly
- ✅ Like Post button shows (doesn't need to work yet)
- ✅ Bootstrap styling is consistent across all pages
- ✅ Page titles show correctly in browser tabs

---

### **❓ Common Questions - Template Inheritance:**

**Q: "Can I have multiple levels of inheritance?"**
A: Yes! Example: base.html → blog_base.html → post_list.html. Each can extend the previous one.

**Q: "What if I want to ADD to a block, not replace it?"**
A: Use {{ block.super }}:
```html
{% block title %}
    {{ block.super }} - My Extra Title
{% endblock %}
```

**Q: "Can I use {% extends %} in the middle of a file?"**
A: No! {% extends %} MUST be the first tag in the file (before any HTML or whitespace).

**Q: "What if I define a block in parent but forget to override in child?"**
A: Django uses the parent's default content. That's why we add default content in blocks!

**Q: "Can I have the same block name in multiple templates?"**
A: Yes, that's the point! Parent defines it, child overrides it. Same name connects them.

---

### **🎬 Break (10 minutes)**

---

### **Part 5: Category Filtering & Search**

#### 🎯 **Goal**: Implement category filtering and post search functionality

---

#### **5.1 Category Filtering**

**Add category view to blog/views.py:**

```python
def category_posts(request, category_name):
    """
    Display posts filtered by category
    
    URL: /category/technology/
    Shows only posts in that category
    """
    # All posts (will be from database on Day 3)
    all_posts = [
        {'id': 1, 'title': 'Getting Started with Django', 'author': 'Sarah Johnson', 'category': 'Technology',
         'excerpt': 'A comprehensive guide to Django', 'published': True},
        {'id': 2, 'title': 'CSS Grid Layout Guide', 'author': 'Mike Chen', 'category': 'Technology',
         'excerpt': 'Master CSS Grid', 'published': True},
        {'id': 3, 'title': 'Travel Tips for Europe', 'author': 'Emily Davis', 'category': 'Travel',
         'excerpt': 'Essential travel advice', 'published': True},
        {'id': 4, 'title': 'Healthy Breakfast Recipes', 'author': 'Jennifer Lee', 'category': 'Health',
         'excerpt': 'Start your day right', 'published': False},
        {'id': 5, 'title': 'JavaScript ES6 Features', 'author': 'David Wilson', 'category': 'Technology',
         'excerpt': 'Modern JavaScript features', 'published': True},
        {'id': 6, 'title': 'Photography Basics', 'author': 'Alex Brown', 'category': 'Art',
         'excerpt': 'Learn photography', 'published': True},
        {'id': 7, 'title': 'Meditation for Beginners', 'author': 'Lisa Martinez', 'category': 'Health',
         'excerpt': 'Find your inner peace', 'published': False},
        {'id': 8, 'title': 'Building REST APIs', 'author': 'Tom Anderson', 'category': 'Technology',
         'excerpt': 'API development guide', 'published': True},
    ]
    
    # Filter posts by category
    # force category_name to lower case for display
    # URL: /category/technology/ → category_name = "technology"
    # We need now to match: "technology" (lowercase)
    
    if category_name != category_name.lower():
        # Redirect to lowercase version
        return redirect('blog:category_posts', category_name=category_name.lower())
    
    filtered_posts = [
        post for post in all_posts
        if post['category'].lower() == category_name
    ]
    
    # On Day 3 with database, this becomes:
    # filtered_posts = Post.objects.filter(category__iexact=category_name)
    
    context = {
        'category_name': category_name.title(),
        'posts': filtered_posts,
        'total_posts': len(filtered_posts),
    }
    return render(request, 'blog/category_posts.html', context)
```

**Add URL pattern in blog/urls.py:**

```python
urlpatterns = [
    # ... existing patterns ...
    path('category/<str:category_name>/', views.category_posts, name='category_posts'),
]
```

**Create blog/templates/blog/category_posts.html:**

```html
{% extends 'blog/base.html' %}
{% load static %}

{% block title %}{{ category_name }} - BlogHub{% endblock %}

{% block content %}
<!-- Header -->
<div class="bg-info text-white py-4">
    <div class="container">
        <h1>📂 {{ category_name }} Posts</h1>
        <p class="lead">Browse our {{ category_name }} articles</p>
    </div>
</div>

<!-- Breadcrumb -->
<div class="container mt-3">
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="{% url 'blog:home' %}">Home</a></li>
            <li class="breadcrumb-item"><a href="{% url 'blog:posts' %}">Posts</a></li>
            <li class="breadcrumb-item active">{{ category_name }}</li>
        </ol>
    </nav>
</div>

<!-- Posts Grid -->
<div class="container my-5">
    {% if posts %}
        <div class="row">
            {% for post in posts %}
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="card h-100">
                    <div class="card-body">
                        <h5 class="card-title">{{ post.title }}</h5>
                        <p class="text-muted">By {{ post.author }} | {{ post.category }}</p>
                        <p class="card-text">{{ post.excerpt }}</p>
                        
                        {% if post.published %}
                            <span class="badge bg-success">✓ Published</span>
                        {% else %}
                            <span class="badge bg-secondary">Draft</span>
                        {% endif %}
                    </div>
                    <div class="card-footer">
                        <a href="{% url 'blog:post_detail' post.id %}" class="btn btn-primary btn-sm w-100">
                            Read More
                        </a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
        
        <div class="text-center mt-4">
            <p class="lead">Showing {{ total_posts }} {{ category_name }} posts</p>
            <a href="{% url 'blog:posts' %}" class="btn btn-outline-primary">← View All Posts</a>
        </div>
    {% else %}
        <div class="alert alert-warning text-center">
            <h4>No posts found in {{ category_name }} category</h4>
            <p>Check out our other categories!</p>
            <a href="{% url 'blog:posts' %}" class="btn btn-primary">View All Posts</a>
        </div>
    {% endif %}
</div>
{% endblock %}
```

**Update base.html to add category links in navigation:**

```html
<!-- Add dropdown to navigation in base.html -->
<ul class="navbar-nav ms-auto">
    <li class="nav-item">
        <a class="nav-link" href="{% url 'blog:home' %}">Home</a>
    </li>
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">
            Categories
        </a>
        <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="{% url 'blog:category_posts' 'technology' %}">Technology</a></li>
            <li><a class="dropdown-item" href="{% url 'blog:category_posts' 'travel' %}">Travel</a></li>
            <li><a class="dropdown-item" href="{% url 'blog:category_posts' 'health' %}">Health</a></li>
            <li><a class="dropdown-item" href="{% url 'blog:category_posts' 'art' %}">Art</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="{% url 'blog:posts' %}">All Posts</a></li>
        </ul>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="{% url 'blog:about' %}">About</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="{% url 'blog:contact' %}">Contact</a>
    </li>
</ul>
```

---

#### **5.2 Search Functionality**

**Add search view to blog/views.py:**

```python
def search_posts(request):
    """
    Search posts by title or content
    
    URL: /search/?q=django
    Searches in post title and excerpt
    """
    # Get search query from URL parameters
    query = request.GET.get('q', '')  # Default to empty string if no query
    
    # All posts
    all_posts = [
        {'id': 1, 'title': 'Getting Started with Django', 'author': 'Sarah Johnson', 'category': 'Technology',
         'excerpt': 'A comprehensive guide to Django web framework', 'published': True},
        {'id': 2, 'title': 'CSS Grid Layout Guide', 'author': 'Mike Chen', 'category': 'Technology',
         'excerpt': 'Master modern CSS Grid layouts', 'published': True},
        {'id': 3, 'title': 'Travel Tips for Europe', 'author': 'Emily Davis', 'category': 'Travel',
         'excerpt': 'Essential European travel advice', 'published': True},
        {'id': 4, 'title': 'Healthy Breakfast Recipes', 'author': 'Jennifer Lee', 'category': 'Health',
         'excerpt': 'Start your day right with these recipes', 'published': False},
        {'id': 5, 'title': 'JavaScript ES6 Features', 'author': 'David Wilson', 'category': 'Technology',
         'excerpt': 'Modern JavaScript features explained', 'published': True},
        {'id': 6, 'title': 'Photography Basics', 'author': 'Alex Brown', 'category': 'Art',
         'excerpt': 'Learn the art of photography', 'published': True},
        {'id': 7, 'title': 'Meditation for Beginners', 'author': 'Lisa Martinez', 'category': 'Health',
         'excerpt': 'Find your inner peace through meditation', 'published': False},
        {'id': 8, 'title': 'Building REST APIs', 'author': 'Tom Anderson', 'category': 'Technology',
         'excerpt': 'Complete guide to API development', 'published': True},
    ]
    
    # Search posts if query exists
    if not query:
        # If no query, return all posts
        search_results = all_posts
    else:
        search_results = [
            post for post in all_posts
            if query.lower() in post['title'].lower() or
            query.lower() in post['excerpt'].lower()
        ]
    
    # On Day 3 with database, this becomes:
    # from django.db.models import Q
    # search_results = Post.objects.filter(
    #     Q(title__icontains=query) | Q(excerpt__icontains=query)
    # )
    
    context = {
        'query': query,
        'posts': search_results,
        'total_results': len(search_results),
    }
    return render(request, 'blog/search_results.html', context)
```

**Detailed Explanation:**
```
query = request.GET.get('q', '')
  ↑              ↑   ↑   ↑    ↑
  │              │   │   │    └─ Default value (if 'q' not found)
  │              │   │   └───── Parameter name
  │              │   └───────── .get() method
  │              └───────────── Dictionary of GET parameters
  └───────────────────── Variable to store result
```

**Add URL pattern:**

```python
urlpatterns = [
    # ... existing patterns ...
    path('search/', views.search_posts, name='search_posts'),
]
```

**Add search form to base.html navigation:**

```html
<!-- Add search form in navbar -->
<div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ms-auto">
        <!-- ... existing nav items ... -->
    </ul>
    <!-- Search Form -->
    <form method="GET" action="{% url 'blog:search_posts' %}" class="d-flex ms-3">
        <input type="text" name="q" class="form-control me-2" placeholder="Search posts..." required>
        <button type="submit" class="btn btn-outline-light">🔍</button>
    </form>
</div>
```

**Create blog/templates/blog/search_results.html:**

```html
{% extends 'blog/base.html' %}
{% load static %}

{% block title %}Search Results - BlogHub{% endblock %}

{% block content %}
<!-- Header -->
<div class="bg-primary text-white py-4">
    <div class="container">
        <h1>🔍 Search Results</h1>
        {% if query %}
            <p class="lead">Results for "{{ query }}"</p>
        {% else %}
            <p class="lead">Enter a search term to find posts</p>
        {% endif %}
    </div>
</div>

<!-- Search Form -->
<div class="container mt-4">
    <form method="GET" action="{% url 'blog:search_posts' %}" class="mb-4">
        <div class="input-group">
            <input type="text" name="q" class="form-control" placeholder="Search posts..." value="{{ query }}" required>
            <button type="submit" class="btn btn-primary">🔍 Search</button>
        </div>
    </form>
</div>

<!-- Search Results -->
<div class="container my-5">
    {% if query %}
        {% if posts %}
            <div class="alert alert-success">
                Found {{ total_results }} post{{ total_results|pluralize }} matching "{{ query }}"
            </div>
            
            <div class="row">
                {% for post in posts %}
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">{{ post.title }}</h5>
                            <p class="text-muted">By {{ post.author }} | {{ post.category }}</p>
                            <p class="card-text">{{ post.excerpt }}</p>
                            
                            {% if post.published %}
                                <span class="badge bg-success">✓ Published</span>
                            {% else %}
                                <span class="badge bg-secondary">Draft</span>
                            {% endif %}
                        </div>
                        <div class="card-footer">
                            <a href="{% url 'blog:post_detail' post.id %}" class="btn btn-primary btn-sm w-100">
                                Read More
                            </a>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        {% else %}
            <div class="alert alert-warning text-center">
                <h4>No posts found for "{{ query }}"</h4>
                <p>Try different keywords or browse all posts</p>
                <a href="{% url 'blog:posts' %}" class="btn btn-primary">View All Posts</a>
            </div>
        {% endif %}
    {% else %}
        <div class="alert alert-info text-center">
            <h4>Start your search</h4>
            <p>Enter a title or keyword to find posts you're interested in!</p>
        </div>
    {% endif %}
</div>
{% endblock %}
```

**Explanation:**
```
Search Flow:

1. User types in search box
2. Form submits GET request: /search/?q=django
3. Django receives: request.GET.get('q') = "django"
4. View searches posts
5. Returns results to template

GET vs POST for search:
  - Search uses GET (not POST!)
  - GET allows bookmarking: /search/?q=django
  - GET allows sharing search results
  - POST is for creating/modifying data

URL parameters:
  /search/?q=django&category=technology&sort=date
  
  request.GET.get('q') → "django"
  request.GET.get('category') → "technology"
  request.GET.get('sort') → "date"
```

---

### **Part 6: Forms & CSRF Protection**

#### 🎯 **Goal**: Understand Django forms and CSRF protection

---

#### **6.1 CSRF Protection Explained**

```
CSRF (Cross-Site Request Forgery):
  
Scenario without protection:
1. You're logged into bloghub.com
2. You visit evil-site.com
3. evil-site.com has hidden form:
   <form action="http://bloghub.com/delete-account/" method="POST">
   </form>
4. Form auto-submits using YOUR session!
5. Your account gets deleted! 😱

Django's CSRF Protection:
1. Server generates unique token for each session
2. {% csrf_token %} adds token to form
3. Server verifies token matches session
4. evil-site.com doesn't have your token → request rejected! ✅

The token:
  <input type="hidden" name="csrfmiddlewaretoken" value="abc123xyz...">
  
Django checks:
  - Is token present in form?
  - Does it match session token? [ secret_token vs masked_token ]
  - Is it expired?
  
If any check fails → 403 Forbidden
```

**🎨 See This Visual:**
```
Without CSRF Protection:
┌───────────────────────────────────┐
│  evil-site.com                    │
│  <form action="bloghub.com">      │
│    <button>Click Me!</button>     │
│  </form>                          │
└───────────────────────────────────┘
         ↓ (submits form)
┌───────────────────────────────────┐
│  bloghub.com                      │
│  ✗ No CSRF token!                 │
│  ✓ Deletes your data! 😱          │
└───────────────────────────────────┘

With CSRF Protection:
┌───────────────────────────────────┐
│  evil-site.com                    │
│  <form action="bloghub.com">      │
│    (No CSRF token!)               │
│  </form>                          │
└───────────────────────────────────┘
         ↓ (submits form)
┌───────────────────────────────────┐
│  bloghub.com                      │
│  ✗ CSRF token missing!            │
│  ✓ 403 Forbidden                  │
│  ✓ Your data is safe! ✅          │
└───────────────────────────────────┘
```

---

#### **6.2 Contact Form Example**

**Update contact view in blog/views.py:**

```python
from django.contrib import messages

def contact(request):
    """
    Contact page with form submission
    GET: Show form
    POST: Process form submission
    """
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Basic validation
        if not all([name, email, subject, message]):
            messages.error(request, 'Please fill in all fields.')
        elif '@' not in email:
            messages.error(request, 'Please enter a valid email address.')
        else:
            # In real app: Send email, save to database, etc.
            print(f"Contact form submission:")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Subject: {subject}")
            print(f"Message: {message}")
            
            # Success message
            messages.success(request, f'Thank you {name}! We received your message and will respond soon.')
            
            # Redirect to avoid form resubmission
            return redirect('blog:contact')
    
    # GET request or after POST redirect
    context = {
        'email': 'contact@bloghub.com',
        'phone': '+1-800-BLOGHUB',
        'address': '123 Writer Street, Content City, CC 12345',
        'business_hours': 'Monday - Friday: 9AM - 6PM',
        'departments': [
            {'name': 'Editorial', 'email': 'editorial@bloghub.com'},
            {'name': 'Support', 'email': 'support@bloghub.com'},
            {'name': 'Partnerships', 'email': 'partners@bloghub.com'},
        ],
        'social_media': [
            {'platform': 'Facebook', 'link': 'facebook.com/bloghub'},
            {'platform': 'Twitter', 'link': 'twitter.com/bloghub'},
            {'platform': 'Instagram', 'link': 'instagram.com/bloghub'},
        ]
    }
    return render(request, 'blog/contact.html', context)
```

**Update contact.html with form:**

```html
{% extends 'blog/base.html' %}
{% load static %}

{% block title %}Contact Us - BlogHub{% endblock %}

{% block content %}
<!-- Header -->
<div class="bg-success text-white py-4">
    <div class="container">
        <h1>📞 Contact Us</h1>
        <p class="lead">We're here to help! Reach out anytime.</p>
    </div>
</div>

<!-- Messages (Success/Error) -->
{% if messages %}
<div class="container mt-3">
    {% for message in messages %}
    <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
    {% endfor %}
</div>
{% endif %}

<!-- Contact Form -->
<div class="container my-5">
    <div class="row">
        <!-- Form Column -->
        <div class="col-lg-8 mb-4">
            <div class="card">
                <div class="card-body">
                    <h2 class="card-title">Send Us a Message</h2>
                    <form method="POST" action="{% url 'blog:contact' %}">
                        {% csrf_token %}
                        
                        <div class="mb-3">
                            <label for="name" class="form-label">Your Name *</label>
                            <input type="text" class="form-control" id="name" name="name" required>
                        </div>
                        
                        <div class="mb-3">
                            <label for="email" class="form-label">Email Address *</label>
                            <input type="email" class="form-control" id="email" name="email" required>
                        </div>
                        
                        <div class="mb-3">
                            <label for="subject" class="form-label">Subject *</label>
                            <input type="text" class="form-control" id="subject" name="subject" required>
                        </div>
                        
                        <div class="mb-3">
                            <label for="message" class="form-label">Message *</label>
                            <textarea class="form-control" id="message" name="message" rows="5" required></textarea>
                        </div>
                        
                        <button type="submit" class="btn btn-success btn-lg w-100">
                            📧 Send Message
                        </button>
                    </form>
                </div>
            </div>
        </div>
        
        <!-- Contact Info Column -->
        <div class="col-lg-4">
            <div class="card mb-3">
                <div class="card-body">
                    <h5 class="card-title">📧 Email</h5>
                    <p class="card-text">{{ email }}</p>
                </div>
            </div>
            
            <div class="card mb-3">
                <div class="card-body">
                    <h5 class="card-title">📱 Phone</h5>
                    <p class="card-text">{{ phone }}</p>
                </div>
            </div>
            
            <div class="card mb-3">
                <div class="card-body">
                    <h5 class="card-title">📍 Address</h5>
                    <p class="card-text">{{ address }}</p>
                </div>
            </div>
            
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">🕐 Business Hours</h5>
                    <p class="card-text">{{ business_hours }}</p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

**Explanation:**
```
Form Processing Flow:

1. GET Request (User visits page):
   if request.method == 'POST':  # False
       # Skip this
   # Show empty form
   return render(request, 'contact.html')

2. POST Request (User submits form):
   if request.method == 'POST':  # True
       # Get data from form
       name = request.POST.get('name')
       # Validate data
       # Process data
       # Show success message
       return redirect('blog:contact')  # PRG pattern!

3. After redirect:
   # GET request again
   # Show form with success message

Django messages framework:
  from django.contrib import messages
  
  messages.success(request, 'Success!')  # Green alert
  messages.error(request, 'Error!')      # Red alert
  messages.warning(request, 'Warning!')  # Yellow alert
  messages.info(request, 'Info!')        # Blue alert
  
  Messages are stored in session and display once

request.POST dictionary:
  <input name="email" value="user@example.com">
  
  request.POST.get('email') → "user@example.com" [returns None if missing] [the safe way]
  request.POST['email'] → "user@example.com" (raises error if missing)
  request.POST.get('email', 'default') → Uses default if missing
```

---

## 🔬 **LAB SESSION (90 minutes)**

---

### **📝 LAB TASK 1: Implement "Featured Posts" Section**

**Goal:** Create a view that shows the newest 4 posts on the home page

**Instructions:**
1. Modify home view to include a 'featured_posts' list in context
2. Add 4 posts with an 'is_featured' flag or recent dates
3. Update home.html to display these in a "Featured Posts" section
4. Use Bootstrap cards in a row
5. Link each post to its detail page

**💡 Hints:**
```python
# In home view
featured_posts = [p for p in all_posts if p['id'] >= 6][:4]
context = {
    # ... existing context ...
    'featured_posts': featured_posts,
}
```

**✅ Expected Result:**
- Home page shows "Featured Posts" section
- 4 newest posts displayed
- Clicking goes to post detail page

---

### **📝 LAB TASK 2: Add Author Filter**

**Goal:** Filter posts by author

**Instructions:**
1. Create view: `author_posts(request, author_name)`
2. URL: `/author/<str:author_name>/`
3. Filter posts by author name
4. Create template showing filtered results
5. Add author links in post detail pages

**💡 Hints:**
```python
def author_posts(request, author_name):
    filtered = [p for p in all_posts if p['author'].lower().replace(' ', '-') == author_name]
    # ...
```

---

### **📝 LAB TASK 3: Advanced Search with Category Filter**

**Goal:** Enhance search to filter by category

**Instructions:**
1. Update search form to include category dropdown
2. Modify search_posts view to accept category parameter
3. Filter by both search query AND category
4. Update search_results.html to show selected filters

**💡 Hints:**
```python
query = request.GET.get('q', '')
category = request.GET.get('category', '')

if category:
    results = [p for p in results if p['category'] == category]
```

---

### **📝 LAB TASK 4: Product Comparison Page**

**Goal:** Compare 2-3 products side-by-side

**Instructions:**
1. Create URL: `/compare/?ids=1,2,3`
2. Extract product IDs from query string
3. Display products in columns with features listed
4. Show price comparison
5. Highlight best value

**💡 Hints:**
```python
ids_string = request.GET.get('ids', '')
product_ids = [int(id) for id in ids_string.split(',') if id]
```

---

### **🎉 Lab Completion Checklist:**

```
BY THE END OF LAB, YOU MUST HAVE:

✅ REQUIRED:
   ✓ Dynamic product detail pages working
   ✓ Template inheritance implemented (all pages use base.html)
   ✓ Named URLs throughout the project
   ✓ Category filtering functional
   ✓ Search functionality working
   ✓ Contact form with CSRF protection
   ✓ Bootstrap dropdown navigation

✅ BONUS (Extra credit):
   ✓ New Arrivals section
   ✓ Price range filtering
   ✓ Advanced search with category
   ✓ Product comparison page
   ✓ Custom 404 error page
   ✓ Breadcrumb navigation on all pages
```

---

## 📝 **WRAP-UP & SUMMARY**

---

### **What We Accomplished Today:**

```
SESSION 1: Dynamic URLs & Views
✓ Dynamic URL patterns with <int:id>
✓ Path converters (int, str, slug, uuid, path)
✓ Named URLs with {% url %}
✓ URL reversing with reverse() and redirect()
✓ HTTP methods (GET vs POST)
✓ CSRF protection
✓ View decorators (@require_POST)

SESSION 2: Templates & Features
✓ Template inheritance ({% extends %}, {% block %})
✓ Created base.html for consistent layout
✓ Converted all templates to use inheritance
✓ Category filtering
✓ Search functionality
✓ Forms with POST handling
✓ Django messages framework
```

---

### **Key Concepts Mastered:**

```
1. Dynamic URLs:
   path('product/<int:id>/', view, name='detail')
   → /post/5/ captures id=5

2. Named URLs:
   {% url 'blog:detail' 5 %}
   → Generates correct URL automatically

3. Template Inheritance:
   Parent: {% block content %}{% endblock %}
   Child: {% extends 'base.html' %}
          {% block content %}My Content{% endblock %}

4. HTTP Methods:
   GET → Retrieve data (safe, idempotent)
   POST → Submit data (causes changes)

5. CSRF Protection:
   {% csrf_token %} in all POST forms
   Prevents cross-site request forgery

6. Request Data:
   request.GET.get('q') → URL parameters
   request.POST.get('name') → Form data
   request.method → 'GET' or 'POST'
```

---

### **Common Issues & Solutions:**

```
┌──────────────────────────────────────────────┐
│  Issue                  Solution             │
├──────────────────────────────────────────────┤
│  NoReverseMatch         Check URL name and   │
│                         app namespace        │
├──────────────────────────────────────────────┤
│  CSRF verification      Add {% csrf_token %} │
│  failed                 to POST forms        │
├──────────────────────────────────────────────┤
│  TemplateDoesNotExist   Check file path and  │
│                         app in INSTALLED_APPS│
├──────────────────────────────────────────────┤
│  404 on product detail  Check path converter │
│                         matches view param   │
└──────────────────────────────────────────────┘
```

---

## 🏠 **HOMEWORK ASSIGNMENTS**

---

### **Assignment 1: "Featured Products" on Home Page**

**Requirements:**
- Add a "Featured Products" section to home page
- Show 6 products marked as featured
- Use Bootstrap card grid (3 per row)
- Add a "featured" boolean to product dictionaries
- Link to product detail pages

**Deliverable:** Screenshot of home page with featured section

---

### **Assignment 2: "Related Products" on Detail Page**

**Requirements:**
- On product detail page, show "Related Products"
- Related = same category, different product
- Display 3 related products in cards
- If no related products, hide section

**Deliverable:** Product detail page showing related products

---

### **Assignment 3: Advanced Search Features**

**Requirements:**
- Add sorting to search results (price low-high, high-low, name A-Z)
- Add price range filters ($0-$50, $50-$100, $100+)
- Show number of results for each filter
- Allow combining filters

**Deliverable:** Enhanced search page with filters

---

### **Assignment 4: Custom 404 Page**

**Requirements:**
- Create templates/404.html
- Design professional "Page Not Found" page
- Include search box
- Show popular products
- Link to home

**Deliverable:** Custom 404 page

---

### **Assignment 5: Newsletter Subscription Form**

**Requirements:**
- Add newsletter form to footer
- Email field with validation
- Handle POST submission
- Show success message
- Store emails (just print for now)

**Deliverable:** Working newsletter subscription

---

## 📚 **READING ASSIGNMENTS**

**Required Reading:**

```
📖 Django Documentation:
1. URL Dispatcher:
   https://docs.djangoproject.com/en/stable/topics/http/urls/
   - Focus on: path converters, reverse(), include()

2. Views:
   https://docs.djangoproject.com/en/stable/topics/http/views/
   - Focus on: request/response objects, shortcuts

3. Templates:
   https://docs.djangoproject.com/en/stable/ref/templates/language/
   - Focus on: template inheritance, built-in tags/filters

4. CSRF Protection:
   https://docs.djangoproject.com/en/stable/ref/csrf/
   - Understand how and why it works
```

---

## 🔧 **QUICK REFERENCE COMMANDS**

```bash
# ====================
# Development Server
# ====================
python manage.py runserver
python manage.py runserver 8080  # Different port

# ====================
# Django Shell (testing code)
# ====================
python manage.py shell

# Test URL reversing:
>>> from django.urls import reverse
>>> reverse('blog:home')
'//'
>>> reverse('blog:post_detail', args=[5])
'/post/5/'

# ====================
# Template Debugging
# ====================
# In views.py, print context:
print(context)

# In templates, show all variables:
{{ debug }}  # Only works if DEBUG=True

# ====================
# Check for Issues
# ====================
python manage.py check
```

---

## 🎯 **PREPARATION FOR DAY 3**

**Before Day 3, ensure you have:**

```
✅ Working BlogHub project with:
   - Home, Posts, About, Contact pages
   - Product detail pages
   - Category filtering
   - Search functionality
   - Template inheritance
   - Named URLs throughout

✅ Understanding of:
   - Dynamic URLs and path converters
   - Template inheritance and blocks
   - HTTP GET vs POST
   - CSRF protection
   - request.GET and request.POST

✅ Homework completed:
   - At least 3 of 5 assignments done
   - Code committed to GitHub (optional but recommended)
```

**Day 3 Preview:**
```
Tomorrow we'll learn:
- Django Models (database layer!)
- Creating Product, Category, Order models
- Django ORM (Object-Relational Mapping)
- Database queries (filter, get, all, etc.)
- Django Admin panel
- Migrations (creating database tables)
- Model relationships (ForeignKey, ManyToMany)

We'll convert our hardcoded product lists to real database!
This is where Django becomes REALLY powerful! 🚀
```

---

## 📊 **PROJECT STRUCTURE AFTER DAY 2**

```
bloghub_project/
├── venv/
├── bloghub/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py  # Project URLs (includes blog.urls)
│   ├── asgi.py
│   └── wsgi.py
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html  # ⭐ Base template
│   │       ├── home.html  # Extends base
│   │       ├── posts.html  # Extends base
│   │       ├── about.html  # Extends base
│   │       ├── contact.html  # Extends base
│   │       ├── post_detail.html  # Extends base
│   │       ├── category_posts.html  # ⭐ New
│   │       └── search_results.html  # ⭐ New
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py  # Still empty (Day 3!)
│   ├── tests.py
│   ├── urls.py  # ⭐ All routes defined
│   └── views.py  # ⭐ All views implemented
├── static/
│   ├── css/
│   │   └── bootstrap.min.css
│   └── js/
│       └── bootstrap.bundle.min.js
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## ✅ **SELF-ASSESSMENT CHECKLIST**

**Before moving to Day 3, you should be able to:**

```
URLs & Views:
□ Create dynamic URLs with path converters
□ Use named URLs in templates and views
□ Handle GET and POST requests
□ Use redirect() and reverse()
□ Apply view decorators

Templates:
□ Create base templates with blocks
□ Extend base templates in child templates
□ Override blocks in child templates
□ Use {% url %} tag correctly
□ Apply template filters

Forms:
□ Create HTML forms with POST method
□ Add {% csrf_token %} to forms
□ Process form data in views
□ Display success/error messages
□ Validate form input

Features:
□ Filter products by category
□ Search products by name/description
□ Navigate between pages using named URLs
□ Display dynamic content from context
□ Handle missing/invalid data gracefully
```

---

## 🎓 **EXTRA CREDIT CHALLENGES**

**Advanced Tasks:**

### **Challenge 1: Pagination**
- Show 9 products per page
- Add "Previous" and "Next" buttons
- Show page numbers
- Use URL parameters: `/posts/?page=2`

### **Challenge 2: Post Sorting**
- Sort by date (newest to oldest, oldest to newest)
- Sort by title (A-Z, Z-A)
- Sort by reading time
- Use URL parameters: `/posts/?sort=date_desc`

### **Challenge 3: Reading List (Session-based)**
- Add "Save to Reading List" button
- Store post IDs in session
- Create `/reading-list/` page
- Show all saved posts
- Allow removing from reading list

### **Challenge 4: Bookmark Counter**
- Add bookmark icon to navigation
- Show number of bookmarked posts
- Update counter when bookmarking posts
- Use Django sessions

### **Challenge 5: Post Comments Section**
- Add comments list to post detail
- Show commenter name and date
- Show comment text
- Calculate comment count
- Use static data for now (database on Day 3)

---

## 🌟 **CONGRATULATIONS!**

```
🎉 You've completed Day 2! 🎉

You now know:
✓ Dynamic URLs with parameters
✓ Template inheritance
✓ Named URLs and reversing
✓ HTTP methods (GET/POST)
✓ CSRF protection
✓ Category filtering
✓ Search functionality
✓ Form handling

Tomorrow: Django Models & Database! 🗄️
The real power of Django awaits!
```

---

# 🚀 **Day 2 Complete! See you on Day 3!** 🚀