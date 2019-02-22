# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

class AuditableMixin(object,):
    def form_valid(self, form, ):
        if not form.instance.id:
            form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(AuditableMixin, self).form_valid(form)
