from django.db import models

# Create your models here.
class hospital(models.Model):
    namee=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    number=models.CharField(max_length=20)
    image=models.ImageField()
    def __str__(self):
        return self.namee
class medical(models.Model):
    name=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000) 
    number=models.IntegerField()   
    # image=models.ImageField(upload_to="/img")
class User(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    weight=models.CharField(max_length=10)
    height=models.CharField(max_length=20)
    number=models.IntegerField()
    address=models.CharField(max_length=1000)
    email=models.EmailField()
      
    