from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module

ModuleFormSet = inlineformset_factory(Course, Module,
                                      fields=['title', 'decription'],
                                      
                                      extra=2,
                                      can_delete=True)