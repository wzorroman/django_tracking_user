# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tracking_user.models import *

# Register your models here.
class AuditableAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.modified_by = request.user
        obj.save()
        
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            # Check if it is the correct type of inline
            if isinstance(instance, AuditableModel):
                if not instance.created_by_id:
                    instance.created_by = request.user
                instance.modified_by = request.user
                instance.save()

class Auditable2Admin(admin.ModelAdmin):
    exclude = ('created_by', 'modified_by',)
    readonly_fields = ('created_by', 'modified_by', 'created', 'modified')
    
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, Auditable2Model):  # Check if it is the correct type of inline
                if not instance.created_by_id:
                    instance.created_by = "{} {}".format(request.user.id, request.user.username)
                instance.modified_by = "{} {}".format(request.user.id, request.user.username)
                instance.save()

    def format_created(self, obj):
        return obj.created.strftime("%d/%m/%Y %H:%M:%S") if obj.created else '-'

    def format_modified(self, obj):
        return obj.modified.strftime("%d/%m/%Y %H:%M:%S") if obj.modified else '-'

    format_created.short_description = 'Fecha creacion'
    format_created.admin_order_field = 'created'
    format_modified.short_description = 'Fecha edicion'
    format_modified.admin_order_field = 'modified'


class StatusAuditable2Admin(admin.ModelAdmin):
    exclude = ('termination_by',)
    readonly_fields = ('termination', 'termination_by')
    list_display = ('format_termination', 'termination_by', 'estado')
    list_filter = ('estado', )

    def format_termination(self, obj):
        return obj.termination.strftime("%d/%m/%Y %H:%M:%S") if obj.termination else '-'

    format_termination.short_description = 'Fecha terminacion'
    format_termination.admin_order_field = 'termination'

    # funcion q debe incluirse en la herencia del admin para list_display
    # def get_list_display(self, request):
    #     # campos del modelo a mostrar en el listado
    #     lista_mostrar = ('id', 'nombre')
    #     return lista_mostrar + self.list_display

    # funcion q debe incluirse en la herencia del admin para list_filter
    # def get_list_filter(self, request):
    #     # campos del modelo a filtrar
    #     filtros = ('tipo',)
    #     return self.list_filter + filtros
