from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000000)
    author = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    categories = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
