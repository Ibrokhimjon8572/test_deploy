from django.db import models

class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)