from django.db import models

# Create your models here.

class Student(models.Model):
    sroll=models.IntegerField()
    sname=models.CharField(max_length=255)
    smarks=models.FloatField()
    sadd=models.CharField(max_length=255)
