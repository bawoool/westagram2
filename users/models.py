from django.db import models

# Create your models here.

class User(models.Model): 
    name       = models.CharField(max_length=40)
    email      = models.CharField(max_length=100, unique=True)
    password   = models.CharField(max_length=400)
    phone      = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'users'
