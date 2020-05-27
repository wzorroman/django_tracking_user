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
