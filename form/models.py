from django.db import models

# Create your models here.

class usermodel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
    age=models.IntegerField()
    location=models.CharField(max_length=20)