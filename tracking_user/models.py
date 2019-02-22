# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# audit
from crum import get_current_user


class AuditableModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_created_by')

    modified = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_modidied_by')

    class Meta:
        abstract = True        
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(AuditableModel, self).save(*args, **kwargs)