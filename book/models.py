from django.db import models
from django.contrib.auth.models import User
class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birth_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    price=models.FloatField()
    count=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.ManyToManyField(Book)
    created_at=models.DateTimeField(auto_now_add=True)

