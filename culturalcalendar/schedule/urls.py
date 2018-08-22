from django.conf.urls import url

from . import views

app_name = 'schedule'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #createevent/add
    url(r'culturalevent/add/$', views.CreateEvent.as_view(), name='createevent-add'),
    
    #view specific culturalevent
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    
]