# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from tracking_user.models import AuditableModel
# Create your models here.

class Tabla01(AuditableModel):
    nombre = models.CharField('Nombre', max_length=128)
    observacion = models.TextField('Observación', null=True, blank=True)

    def __unicode__(self):
        return self.nombre