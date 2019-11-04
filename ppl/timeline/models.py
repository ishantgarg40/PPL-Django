from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to="media")
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"


class Categories(models.Model):
    image = models.ImageField(blank=True, upload_to="media")
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    image = models.FileField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)

    def save_post(self, request, *args, **kwargs):
        self.created_by = request.user
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.image}"

