# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView

from django.urls import reverse
from django.urls import reverse_lazy 

from tracking_user.views import AuditableMixin
from app_test.models import *
from app_test.forms import *

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'home.html'

class Tabla01ListView(ListView):
    template_name = 'tabla01_list.html'
    model = Tabla01

class Tabla01CreateView(AuditableMixin, CreateView):
    template_name = 'tabla01_add.html'
    model = Tabla01
    form_class = Tabla01Form
    
    def get_success_url(self):
        messages.success(self.request, "Guardo el registro : {}".format(self.object.nombre))
        return reverse('tabla01_list')

class Tabla01UpdateView(AuditableMixin, UpdateView):
    template_name = 'tabla01_add.html'
    model = Tabla01
    form_class = Tabla01Form    

    def get_success_url(self):
        messages.success(self.request, "Actualizo el registro : {}".format(self.object.nombre))
        return reverse('tabla01_update', kwargs={
            'pk': self.object.id
        })

class Tabla01DeleteView(DeleteView):
    template_name = 'tabla01_confirm_delete.html'
    model = Tabla01
    success_url = reverse_lazy('tabla01_list')