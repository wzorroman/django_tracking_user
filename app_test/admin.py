# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tracking_user.admin import AuditableAdmin

# Register your models here.
from app_test.models import *

#class Tabla01Admin(AuditableAdmin):
class Tabla01Admin(admin.ModelAdmin):
    exclude = ('created_by','modified_by',)
    readonly_fields = ('created_by','modified_by','created', 'modified')
    

admin.site.register(Tabla01, Tabla01Admin)
