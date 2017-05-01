from django.db import models
from address.models import District
from rrc.models import Rrc
from django.contrib.auth.models import User, Group

# Create your models here.
class Camp(models.Model):
	name = models.CharField(max_length=15, null=False, unique=True)
	district = models.ForeignKey(District)
	user = models.ForeignKey(User, on_delete=models.CASCADE,default='')
	address = models.TextField(null=True)
	date = models.DateTimeField(null=True)
	contact = models.CharField(max_length=25, null=False)

	def __str__(self):
		return self.name+' ----- '+str(self.district)+' ----- '+str(self.user)+' ----- '+str(self.date)