from ast import AnnAssign
from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    
    # Define what name is returned when python transfor a Book object to string
    def __str__(self):
        return self.title

class Question2(Question):
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)

class Question4(Question):
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    answer4 = models.CharField(max_length=100)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question