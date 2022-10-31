from django.db import models

# Create your models here.
class Activite(models.Model):
    title = models.fields.CharField(max_length=100)    
