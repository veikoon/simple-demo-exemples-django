from email.policy import default
from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    
    # Define what name is returned when python transfor a Book object to string
    def __str__(self):
        return self.name