# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityDetailImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.FileField(upload_to='city_images')),
                ('city', models.ForeignKey(to='main.Citys')),
            ],
        ),
        migrations.CreateModel(
            name='EventBlockDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=60)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EventBlockHour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=60)),
                ('hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='IslandDetailImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.FileField(upload_to='island_images')),
                ('island', models.ForeignKey(to='main.Islands')),
            ],
        ),
        migrations.CreateModel(
            name='LocationDetailImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.FileField(upload_to='location_images')),
                ('location', models.ForeignKey(to='main.Locations')),
            ],
        ),
        migrations.AlterField(
            model_name='articles',
            name='booking',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='description_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='description_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='email',
            field=models.EmailField(max_length=254, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='hour_close',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='hour_open',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='phone',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='stars',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='telephone',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='citysdetails',
            name='history',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='citysdetails',
            name='history_de',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='citysdetails',
            name='history_en',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='citysdetails',
            name='history_fr',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='citysdetails',
            name='video',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='video',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='islandsdetails',
            name='history',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='islandsdetails',
            name='history_de',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='islandsdetails',
            name='history_en',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='islandsdetails',
            name='history_fr',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='islandsdetails',
            name='video',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locationsdetails',
            name='history',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='locationsdetails',
            name='history_de',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locationsdetails',
            name='history_en',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locationsdetails',
            name='history_fr',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locationsdetails',
            name='video',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='regionalfood',
            name='recipe_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='regionalfood',
            name='recipe_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='regionalfood',
            name='recipe_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventblockhour',
            name='event',
            field=models.ForeignKey(to='main.Events'),
        ),
        migrations.AddField(
            model_name='eventblockhour',
            name='event_block',
            field=models.ForeignKey(to='main.EventBlockDate'),
        ),
        migrations.AddField(
            model_name='eventblockdate',
            name='event',
            field=models.ForeignKey(to='main.Events'),
        ),
    ]
