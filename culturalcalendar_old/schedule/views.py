# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404

from .models import CulturalEvent
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.conf import settings

# Create your views here.
def index(request):
    CE_Events = CulturalEvent.objects.all()
    #must have the CE_Recent
    CE_first = CE_Events.first()
    CE_second = CE_Events.__getitem__(1)
    CE_third = CE_Events.__getitem__(2)
    context = {
        'CE_third':CE_third,
        'CE_second':CE_second,
        'CE_first': CE_first,
        } 

    return render(request,'schedule/index/index.html',context)

def details(request,CulturalEvent_id):
    CE_ = get_object_or_404(CulturalEvent.objects.get(CulturalEvent_id)) 
    return render(request, 'index/index.html', {'CE_Events': CE_,} )

class IndexView(generic.ListView):
    template_name = 'culturalevent/index.html'
    context_object_name = 'all_culturalevents'
    
    def get_queryset(self):
        return CulturalEvent.objects.all()
    
class DetailView(generic.DetailView):
    model = CulturalEvent
    template_name = 'culturalevent/detail.html'
    
class CreateEvent(CreateView):
    model = CulturalEvent
    fields = ['CE_name',
              'CE_location',
              'CE_date_and_time',
              'CE_value',
              'CE_description',
              'CE_file',
              ]
    
    
    
    
    
    
    
    
    
    
    
    