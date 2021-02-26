from django.db import models

# Create your models here.

class book(models.Model):
    title=models.CharField(max_length=256,null=True,blank=True)
    author=models.CharField(max_length=256,null=True,blank=True)
    image=models.CharField(max_length=256,null=True,blank=True)
    year=models.PositiveIntegerField(default=9,null=True,blank=True)
    price=models.PositiveIntegerField(default=-1.0,null=True,blank=True)
    description=models.CharField(max_length=2000,null=True,blank=True)
    bestseller=models.BooleanField(default=False)