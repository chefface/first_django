# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160719_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='statecapital',
            name='state',
            field=models.OneToOneField(null=True, to='app.State'),
        ),
    ]
