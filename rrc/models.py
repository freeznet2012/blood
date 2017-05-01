from django.db import models
from django.contrib.auth.models import User, Group
from address.models import District

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Rrc(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,default='')
	name = models.CharField(max_length=15, null=False)
	address = models.TextField(blank=True)
	district = models.ForeignKey(District, null=True)
	contact = models.CharField(max_length=25, null=False)

	def __str__(self):
		return self.name+' ----- '+str(self.district)

#User.profile = property(lambda u: Donor.objects.get_or_create(user=u)[0])

