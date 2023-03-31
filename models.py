from django.db import models

# Create your models here.
class Student(models.Model):
    sName = models.TextField()
    sPhno = models.IntegerField()
    sRollno = models.TextField()
 
    