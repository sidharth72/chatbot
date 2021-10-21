from django.db import models

# Create your models here.

class Query(models.Model):
	data = models.CharField(max_length=200)
