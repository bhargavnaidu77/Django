from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    img=models.ImageField(upload_to='photos/')
    author=models.CharField(max_length=30)
    created_at=models.DateTimeField(default=datetime.now)
    
    
    def __str__(self):
        return self.title
''''class User(models.Model):
    user=models.CharField(max_length=30)
    email=models.EmailField()
    pwd=models.CharField(max_length=30)

    def __str__(self):
        return self.user'''