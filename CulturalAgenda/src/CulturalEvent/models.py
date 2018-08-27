from django.db import models
from .LocalSettings import CulturalEventTypes
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime  
from django.utils import timezone
# Create your models here.
def upload_location(instance, filename):
	return "%s/%s" %(instance.id,filename)
class CulturalEvent(models.Model):
	tittle			= models.CharField(blank = False, null = False, max_length=120)
	description		= models.TextField(blank=True, null = True)
	price 			= models.DecimalField(blank = True, null = True,max_digits=10,decimal_places = 2)
	summary			= models.TextField(blank = False, null = False)
	over18			= models.NullBooleanField(default=False)
	location		= models.CharField(blank = True, null = True, max_length=120)
	File 			= models.ImageField(blank=True, null = True,
					upload_to=upload_location,
					height_field="CE_ImageHeight", 
					width_field="CE_ImageWidth",
					)
	CE_ImageHeight  = models.IntegerField(default=0)
	CE_ImageWidth  = models.IntegerField(default=0)
	CE_type			= models.CharField(max_length=100, choices=CulturalEventTypes, default = 'generico')
	CE_email 		= models.EmailField(blank = True, null = True)
	CE_phonenumber	= PhoneNumberField(blank=True, null = True)
	CE_isWhatsApp	= models.NullBooleanField(blank = True)
	CE_Date 		= models.DateField(blank=False, null = True)
	CE_Time 		= models.TimeField(blank=False, null = True)
	
	def __str__(self):
		return self.tittle + ' - ' + self.summary
