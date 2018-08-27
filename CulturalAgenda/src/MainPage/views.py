from django.shortcuts import render, get_object_or_404, redirect
from CulturalEvent.models import CulturalEvent
from CulturalEvent.LocalSettings import CulturalEventTypes
from CulturalEvent.views import culturalevent_create_view, culturalevent_create
from django.db.models import Count
from django.contrib.auth import authenticate, get_user_model


from Accounts.views import login_form,login_view
from Accounts.forms import UserLoginForm
#	]
def MainReload(request):
	print("********************RELOAD*******************")
	return redirect('/')

def Main(request, *args, **kwargs):
	print("********************MAIN*******************")

	if request.POST:
		print(request.POST)
		if 'login' in request.POST:
			print('will login')
			return login_view(request)
		if 'InsertEvent' in request.POST:
			print('will insert the event')
			return culturalevent_create_view(request)
			

	if request.user.is_authenticated:
		print("what is this?")
		InsertForm = culturalevent_create(request)
	else:
		print("not logged in")
		InsertForm = UserLoginForm

	CE_Events = CulturalEvent.objects.all()
	CE_NewEvents= CulturalEvent.objects.all().order_by('-id')[:5]
	CE_ordered_by_date_events = CulturalEvent.objects.all().order_by('-CE_Date')
	CE_ordered_by_location_events = CulturalEvent.objects.all().order_by('-location')
	CE_Events = CulturalEvent.objects.all()

	event_counts = []
	for each in CulturalEventTypes:
		CE_list = CE_Events.filter(CE_type = each[0])
		event_counts += [(each[0],each[1],CE_list, CE_list.count())]

	context = {
			'InsertForm':InsertForm,
			'CE_Events':CE_Events,
			'CE_NewEvents':CE_NewEvents,
			'CE_ordered_by_date_events':CE_ordered_by_date_events,
			'CE_ordered_by_location_events':CE_ordered_by_location_events,
			'EventTypes':CulturalEventTypes,
			'event_counts':event_counts,
	} 
	print("********************MAIN*******************")
	return render(request,"CE_index.html",context)

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

