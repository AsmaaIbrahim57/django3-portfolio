from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=2000)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
