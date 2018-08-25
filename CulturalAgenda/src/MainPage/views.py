from django.shortcuts import render
from CulturalEvent.models import CulturalEvent
from CulturalEvent.LocalSettings import CulturalEventTypes

from django.db.models import Count
# Create your views here.

#	tittle			= models.CharField(blank = False, null = False, max_length=120)
#	description		= models.TextField(blank=True, null = True)
#	price 			= models.DecimalField(blank = True, null = True,max_digits=10,decimal_places = 2)
#	summary			= models.TextField(blank = False, null = False)
#	over18			= models.NullBooleanField(default=False,blank = True, null = True)
#	location		= models.CharField(blank = True, null = True, max_length=120)
#	File 			= models.ImageField(blank=True, null = True,
#					upload_to=upload_location,
#					height_field="CE_ImageHeight", 
#					width_field="CE_ImageWidth",
#					default=settings.DEFAULT_IMG,
#					)
#	CE_ImageHeight  = models.IntegerField(default=0)
#	CE_ImageWidth  = models.IntegerField(default=0)
#	CE_type			= models.CharField(max_length=100, choices=CulturalEventTypes, default = 'generico')
#	CE_email 		= models.EmailField(blank = True, null = True)
#	CE_phonenumber	= PhoneNumberField(blank=True, null = True)
#	CE_isWhatsApp	= models.NullBooleanField(blank = True)
	

def home_view(request, *args, **kwargs):
	CE_Events = CulturalEvent.objects.all()
	event_counts = []
	for each in CulturalEventTypes:
		event_counts += [(each[0],each[1],CE_Events.filter(CE_type = each[0]).count())]

	context = {
	'CE_Events':CE_Events,
	'EventTypes':CulturalEventTypes,
	'event_counts':event_counts,
	} 

	return render(request,"index.html",context)

