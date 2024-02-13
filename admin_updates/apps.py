# -*- coding: utf-8
from django.apps import AppConfig


class DjangoAdminUpdatesConfig(AppConfig):
    name = 'admin_updates'
    verbose_name = 'Update'
    verbose_name_plural = verbose_name


__all__= ['DjangoAdminUpdatesConfig']
