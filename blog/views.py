from django.shortcuts import render, redirect
from .models import Blog, Subscriber
from django.contrib import messages
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """handle index page""" #
    all_blogs = Blog.objects.all()  # Fetch all blog posts from the database
    return render(render, "index.html", {"blogs": all_blogs})

@login_required
def subscribe(request):
    if request.method == "POST":
        email = request.POST["email"]

        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, "You are already subscribed.")

        else:
            new_subscriber = Subscriber(email=email)
            new_subscriber.save()
            messages.success(request, "You have successfully subscribed!")
            return redirect("subscribe")

    return render(request, "subscribe.html")

def add_blog(request):
    """Handle adding a new blog post"""
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)  # Include FILES to handle image uploads
        if form.is_valid():
            blog = form.save()
            return redirect("index")
    else:
        form = BlogForm()
    return render(request, "add_blog.html", {"form": form})
