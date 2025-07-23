from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Author(models.Model):
    """Model for blog authors"""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    """Model for blog posts"""
    image = CloudinaryField('image', blank=True, null=True)  # Cloudinary field for image uploads
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1 )
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Newest posts first
        verbose_name_plural = "Blogs"  # Plural name for admin interface


class Subscriber(models.Model):
    """Model for blog subscribers"""
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Subscribers"  # Plural name for admin interface