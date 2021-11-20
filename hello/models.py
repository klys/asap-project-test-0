from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

# Unique Member ID
class Members(models.Model):
    member_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    date_of_birth = models.DateField()
    when = models.DateTimeField("date created", auto_now_add=True)
    
    

