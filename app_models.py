from django.db import models

class Datas(models.Model):
    name = models.CharField(max_length=20, default="")
    age = models.IntegerField(default=0)  
    address = models.CharField(max_length=50, default="")
    contact = models.IntegerField(default=0)  
    email = models.CharField(max_length=50, default="") 
