from django.db import models
from timeline.models import Post
from django.utils import timezone


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=100, blank=True)
    created_on = models.DateTimeField(default=timezone.now(), blank=True)

    def __str__(self):
        return f"{self.comment} on {self.post}"


class Reply(models.Model):
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE)
    reply = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.reply} on {self.comment}"




