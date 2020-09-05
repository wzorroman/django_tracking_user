# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# audit
from crum import get_current_user

from apps.common import constants


class AuditableModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_column='FEC_CREACION')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_created_by',
                                   db_column='USR_CREACION', on_delete=models.PROTECT)
    modified = models.DateTimeField(auto_now=True, db_column='FEC_EDICION')
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_modidied_by',
                                    db_column='USR_EDICION', on_delete=models.PROTECT)

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


class StatusAuditableModel(models.Model):
    termination = models.DateTimeField("Fecha baja", db_column='FECHA_BAJA', null=True, blank=True)
    termination_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_termination',
                                       db_column='USR_BAJA', on_delete=models.PROTECT, null=True, blank=True)
    estado = models.CharField("Estado", db_column='ESTADO', max_length=1, choices=constants.ESTADO_GENERICO_CHOICES,
                              default=constants.ESTADO_GENERICO_HABILITADO)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if self.estado == constants.ESTADO_GENERICO_DESHABILITADO:
            self.termination = datetime.now()
            self.termination_by = user
        else:
            self.termination = None
            self.termination_by = None
        super(StatusAuditableModel, self).save(*args, **kwargs)


# -- auditoria sin relaciones al user

class Auditable2Model(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_column='FEC_CREACION')
    created_by = models.CharField("Created by", max_length=50, db_column='USR_CREACION')
    modified = models.DateTimeField(auto_now=True, db_column='FEC_EDICION')
    modified_by = models.CharField("Modified by", max_length=50, db_column='USR_EDICION')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = "{} {}".format(user.id, user.username)
        self.modified_by = "{} {}".format(user.id, user.username)
        super(Auditable2Model, self).save(*args, **kwargs)


class StatusAuditable2Model(models.Model):
    termination = models.DateTimeField("Fecha baja", db_column='FECHA_BAJA', null=True, blank=True)
    termination_by = models.CharField("Baja por", max_length=50, db_column='USR_BAJA', null=True, blank=True)
    estado = models.CharField("Estado", db_column='ESTADO', max_length=1, choices=constants.ESTADO_GENERICO_CHOICES,
                              default=constants.ESTADO_GENERICO_HABILITADO)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if self.estado == constants.ESTADO_GENERICO_DESHABILITADO:
            self.termination = datetime.now()
            self.termination_by = "{} {}".format(user.id, user.username)
        else:
            self.termination = None
            self.termination_by = None
        super(StatusAuditable2Model, self).save(*args, **kwargs)
