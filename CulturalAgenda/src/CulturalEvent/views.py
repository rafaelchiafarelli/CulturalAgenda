from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .LocalSettings import CulturalEventTypes
from .forms import CulturalEventForm
from .models import CulturalEvent
from django.views.generic.detail import DetailView
from django.conf import settings
from django.contrib.auth.decorators import login_required
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
	

@login_required(login_url='/login_view/')
def culturalevent_create_view(request):

	form = CulturalEventForm(request.POST or None, request.FILES)
	
	if form.is_valid():
		form.save()
		return render(request,"CE_success.html")
	context = {
		'form':form
	}
	return render(request,"CE_save.html",context) 

def culturalevent_detail_view(request, id):
	instance = get_object_or_404(CulturalEvent,id=id)
	context = {
	'instance':instance,
	}
	return render(request,"CE_detail.html",context)

def culturalevent_list_view(request,choice):
	CE_Events = CulturalEvent.objects.all()

	for c in CulturalEventTypes:
			if int(choice) == int(c[0]):
				CE_Events = CulturalEvent.objects.filter(CE_type = choice)

	context = {'CE_Events':CE_Events}
	return render(request,"CE_list.html",context)

def newer_events(request):
	CE_Events_not_ordered = CulturalEvent.objects.all().order_by('-id')[:10]
	CE_Events = reversed(CE_Events_not_ordered)
	context = {'CE_Events':CE_Events}
	return render(request,"CE_list.html",context)

def next_events(request):
	CE_Events = CulturalEvent.objects.all().order_by('-CE_Date')
	context = {'CE_Events':CE_Events}
	return render(request,"CE_list.html",context)

def location(request):
	CE_Events = CulturalEvent.objects.all().order_by('-location')
	context = {'CE_Events':CE_Events}
	return render(request,"CE_list.html",context)