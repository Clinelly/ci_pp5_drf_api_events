from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.TextField(blank=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ckdmjc'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id} {self.title}"
