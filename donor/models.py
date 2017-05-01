from django.db import models
from django.contrib.auth.models import User, Group
from blood.models import Blood
from address.models import District

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Donor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,default='')
	name = models.CharField(max_length=15, null=False, default="one")
	blood = models.ForeignKey(Blood, null=True)
	district = models.ForeignKey(District, null=True)
	address = models.TextField(null=True)
	pincode = models.IntegerField(null=True)
	contact = models.CharField(max_length=25, null=True)
	weight = models.IntegerField(null=True)
	dob = models.DateField(null=True)
	last_donated = models.DateField(null=True)
	GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)

	def __str__(self):
		return str(self.user)


