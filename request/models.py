from django.db import models
from blood.models import Blood
from address.models import District
# Create your models here.
class Request(models.Model):
	name = models.CharField(max_length=30)
	contact = models.CharField(max_length=25)
	blood = models.ForeignKey(Blood)
	district = models.ForeignKey(District, null=True)
	particulars = models.TextField(null=True)
	units = models.IntegerField()
	date_create = models.DateTimeField(auto_now=True)
	date_of_request = models.DateTimeField()

	
	def __str__(self):
		return str(self.blood)+"---"+str(self.district)+"---"+self.name
		