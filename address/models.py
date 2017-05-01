from django.db import models

# Create your models here.
class District(models.Model):
	name = models.CharField(max_length=20, null=False, unique=True)

	def __str__(self):
		return self.name



class State(models.Model):
	name = models.CharField(max_length=15, null=False, unique=True)

	def __str__(self):
		return self.name