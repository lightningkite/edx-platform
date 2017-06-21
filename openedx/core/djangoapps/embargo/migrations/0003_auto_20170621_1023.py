# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('embargo', '0002_data__add_countries'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='embargoedcourse',
            options={'permissions': ('can_call_check_course_access_api', 'Can access CheckCourseAccessView')},
        ),
    ]
