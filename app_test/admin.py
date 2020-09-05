# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tracking_user.admin import AuditableAdmin

# Register your models here.
from app_test.models import *

class Tabla01Admin(admin.ModelAdmin):
    exclude = ('created_by','modified_by',)
    readonly_fields = ('created_by','modified_by','created', 'modified')

admin.site.register(Tabla01, Tabla01Admin)


class Tabla02Admin(StatusAuditable2Admin):
    # list_display = ('id', 'descripcion', 'format_termination', 'termination_by', 'estado')
    # list_filter = ('estado', 'tipo')
    search_fields = ('id', 'descripcion')

    def get_list_display(self, request):
        lista_mostrar = ('id', 'descripcion', 'tipo')
        return lista_mostrar + self.list_display

    def get_list_filter(self, request):
        filtros = ('tipo',)
        return self.list_filter + filtros


admin.site.register(Tabla02, Tabla02Admin)
