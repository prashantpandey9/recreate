from django.db import models

# Create your models here.

class Contactus(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,blank=False)
    text=models.TextField(max_length=2500, blank=False)

