from datetime import date
from pyexpat import model
from django.db import models

# Create your models here.
class article (models.Model):
    title = models.CharField(max_length= 100)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField()
