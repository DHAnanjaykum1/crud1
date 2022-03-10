
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField(help_text="please enter 10 digits")
    email = models.EmailField()
    city = models.CharField(max_length=200,null=True,blank=True,help_text="optional")