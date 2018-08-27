from django import forms
from django.db import models
from .models import CulturalEvent
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django.forms.fields import DateField, TimeField
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
#	CE_Date 		= models.DateField(blank=False, null = True)
#	CE_Time 		= models.TimeField(blank=False, null = True)

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
    input_formats=['%I:%M %p']

class CulturalEventForm(forms.ModelForm):

	class Meta:
		model = CulturalEvent
		fields 	= [
				'tittle',
				'description',
				'price',
				'summary',
				'over18',
				'location',
				'File',
				'CE_type',
				'CE_email',
				'CE_phonenumber',
				'CE_isWhatsApp',
				'CE_Date',
				'CE_Time',
		]
		widgets = {
           		'CE_Date':DateInput(),
           		'CE_Time':TimeInput(),
           		}

		labels	={
				'tittle':'titulo',
				'description':'descricao',
				'price':'valor',
				'summary':'sumario',
				'over18':'18+',
				'location':'local',
				'File':'imagem de divulgacao',
				'CE_type':'tipo de evento',
				'CE_email':'email de divulgacao',
				'CE_phonenumber':'telefone de informacoes',
				'CE_isWhatsApp':'esse telefone e WhatsApp',
				'CE_Date':'data do evento',
				'CE_Time':'hora do evento',
		}
		help_texts = {
				'tittle':'Um titulo para seu evento',
				'description':'uma descricao adequada para seu evento, com principais atracoes, recomendacoes e etc',
				'price':'valor para entrar',
				'summary':'uma descricao curta para seu evento, que seja um chamariz para os visitantes',
				'over18':'seu evento e para maiores?',
				'location':'local onde acontecera o evento',
				'File':'uma imagem/folder/panfleto do seu evento',
				'CE_type':'seu evento se assemelha a qual dessas opcoes?',
				'CE_email':'use um email de diulgacao para as pessoas se informarem',
				'CE_phonenumber':'telefone para informacoes sobre o evento',
				'CE_isWhatsApp':'selecione se for WhatsApp',
				'CE_Date':'coloque a data do primeiro dia do evento',
				'CE_Time':'hora do evento',
		}
		error_messages={
				'tittle':{'required': 'Obrigatorio'},
				'summary':{'required': 'Obrigatorio'},
				}
