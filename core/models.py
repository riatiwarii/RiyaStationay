# appname/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class UserProfile(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100, null=True, unique=False)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, unique=True)
    
    def __str__(self) -> str:
        return f"{self.fname} {self.lname}"




class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return self.product
