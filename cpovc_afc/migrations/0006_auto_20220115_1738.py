# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_afc', '0005_auto_20220115_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='afcmain',
            name='cg_consent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='afcmain',
            name='cg_consent_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='afcmain',
            name='ovc_consent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='afcmain',
            name='ovc_consent_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
