"""CulturalAgenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.views.static import serve

from MainPage.views import home_view
from CulturalEvent.views import culturalevent_detail_view, culturalevent_create_view, culturalevent_list_view, newer_events, next_events, location


from django.conf.urls.static import static
urlpatterns = [
	path('', home_view, name='home'),
    path('create_event/',culturalevent_create_view),
    path('details_event/<int:id>',culturalevent_detail_view,name='culuturalevent'),
    path('list_event/<int:choice>',culturalevent_list_view,name='culuturalevent'),
    path('newer_events/',newer_events,name='culuturalevent'),
    path('next_events/',next_events,name='culuturalevent'),
    path('location/',location,name='culuturalevent'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
