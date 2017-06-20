# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20170207_0458'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('can_deactivate_users', 'Can deactivate, but NOT delete users'), ('can_call_check_course_access_api', 'Can access CheckCourseAccessView'))},
        ),
    ]
