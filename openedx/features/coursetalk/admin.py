"""Manage coursetalk configuration. """
from config_models.admin import ConfigurationModelAdmin
from django.contrib import admin

from openedx.features.coursetalk.models import CourseTalkWidgetConfiguration

admin.site.register(CourseTalkWidgetConfiguration, ConfigurationModelAdmin)
