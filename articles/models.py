from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField
from products.models import Category, SkinType


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_posts")
    content = SummernoteTextField()
    excerpt = models.TextField(max_length=250, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    skin_type = models.ForeignKey(SkinType, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Article Title: {self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"