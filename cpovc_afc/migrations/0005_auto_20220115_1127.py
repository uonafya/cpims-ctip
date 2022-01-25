# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0006_regpersonsothergeo'),
        ('cpovc_afc', '0004_afcevents_afcforms'),
    ]

    operations = [
        migrations.AddField(
            model_name='afcmain',
            name='immunization_status',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='afcmain',
            name='org_unit',
            field=models.ForeignKey(default=2, to='cpovc_registry.RegOrgUnit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='afcmain',
            name='school_level',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
