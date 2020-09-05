# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from tracking_user.models import AuditableModel, StatusAuditable2Model
# Create your models here.

class Tabla01(AuditableModel):
    nombre = models.CharField('Nombre', max_length=128)
    observacion = models.TextField('Observación', null=True, blank=True)

    def __unicode__(self):
        return self.nombre

class Tabla02(StatusAuditable2Model):
    TIPO_OPC_MERCADO = 'MERCADO'
    TIPO_OPC_VIVIENDA = 'VIVIENDA'

    TIPO_CHOICES = (
        (TIPO_OPC_MERCADO, 'Mercado'),
        (TIPO_OPC_VIVIENDA, 'Vivienda'),
    )
    descripcion = models.CharField('Nombre', max_length=100)
    comentario = models.TextField('Comentario', null=True, blank=True)
    tipo = models.CharField("Tipo",max_length=50, choices=TIPO_CHOICES)

    def __unicode__(self):
        return self.descripcion