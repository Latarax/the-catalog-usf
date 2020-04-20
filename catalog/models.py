from django.db import models

class Book(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    quantity = models.IntegerField()
    availability = models.CharField(max_length=100)
    author = models.CharField(max_length=100)