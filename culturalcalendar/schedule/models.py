# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class CulturalEvent(models.Model):
    CE_name = models.CharField(max_length=250)
    CE_location = models.CharField(max_length=250)
    CE_date_and_time = models.DateTimeField(auto_now = True, auto_now_add = False)
    CE_value = models.CharField(max_length=250)
    CE_description = models.CharField(max_length=250)
    CE_file = models.ImageField(null = True, blank = True, upload_to='uploads')
    
    def __str__(self):
        return self.CE_name
    def __unicode__(self):
        return self.CE_name
    def get_absolute_url(self):
        return reverse("CulturalEvent:details", kwargs={"id":self.id})
    
class CulturalEventStatistics(models.Model):
    CE_father = models.ForeignKey(CulturalEvent, on_delete=models.CASCADE)
    
    
class CulturalEventChild(models.Model):
    CE_father = models.ForeignKey(CulturalEvent, on_delete=models.CASCADE)
    