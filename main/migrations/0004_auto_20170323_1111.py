# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170317_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blocodataevento',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='blocohoraevento',
            name='bloco_evento',
        ),
        migrations.RemoveField(
            model_name='blocohoraevento',
            name='evento',
        ),
        migrations.AddField(
            model_name='evento',
            name='cartaz',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='BlocoDataEvento',
        ),
        migrations.DeleteModel(
            name='BlocoHoraEvento',
        ),
    ]
