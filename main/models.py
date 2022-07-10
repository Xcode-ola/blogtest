#making required importations
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    snippet = models.CharField(max_length=255, default="Click the link to read more")
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()

    def get_absolute_url(self):
        return reverse('index')

class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    posted_at = models.DateTimeField(default=datetime.now, blank=True)
    comment = models.TextField()