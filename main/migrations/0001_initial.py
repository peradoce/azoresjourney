# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('url', models.URLField()),
                ('booking', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('stars', models.IntegerField()),
                ('telephone', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=75)),
                ('default_img', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('description_en', models.TextField()),
                ('description_fr', models.TextField()),
                ('description_de', models.TextField()),
                ('hour_open', models.TimeField()),
                ('hour_close', models.TimeField()),
                ('map_coordinates', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('categorie', models.CharField(max_length=50)),
                ('categorie_en', models.CharField(max_length=50)),
                ('categorie_fr', models.CharField(max_length=50)),
                ('categorie_de', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Citys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('city', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='CitysDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('history', models.TextField()),
                ('history_en', models.TextField()),
                ('history_fr', models.TextField()),
                ('history_de', models.TextField()),
                ('number_parishes', models.IntegerField()),
                ('video', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('city', models.ForeignKey(to='main.Citys')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
                ('hour_begin', models.TimeField()),
                ('hour_end', models.TimeField()),
                ('img', models.CharField(max_length=100)),
                ('video', models.CharField(max_length=100)),
                ('city', models.ForeignKey(to='main.Citys')),
            ],
        ),
        migrations.CreateModel(
            name='ImagesArticles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.CharField(max_length=100)),
                ('article', models.ForeignKey(to='main.Articles')),
            ],
        ),
        migrations.CreateModel(
            name='Islands',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('island', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='IslandsDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('history', models.TextField()),
                ('history_en', models.TextField()),
                ('history_fr', models.TextField()),
                ('history_de', models.TextField()),
                ('number_provinces', models.IntegerField()),
                ('number_parishes', models.IntegerField()),
                ('video', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('island', models.ForeignKey(to='main.Islands')),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('location', models.CharField(max_length=60)),
                ('city', models.ForeignKey(to='main.Citys')),
                ('island', models.ForeignKey(to='main.Islands')),
            ],
        ),
        migrations.CreateModel(
            name='LocationsDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('history', models.TextField()),
                ('history_en', models.TextField()),
                ('history_fr', models.TextField()),
                ('history_de', models.TextField()),
                ('video', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('location', models.ForeignKey(to='main.Locations')),
            ],
        ),
        migrations.CreateModel(
            name='RegionalFood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('food', models.CharField(max_length=60)),
                ('recipe', models.TextField()),
                ('recipe_en', models.TextField()),
                ('recipe_fr', models.TextField()),
                ('recipe_de', models.TextField()),
                ('restaurant', models.ManyToManyField(to='main.Articles')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subcategorie', models.CharField(max_length=50)),
                ('subcategorie_en', models.CharField(max_length=50)),
                ('subcategorie_fr', models.CharField(max_length=50)),
                ('subcategorie_de', models.CharField(max_length=50)),
                ('categorie', models.ForeignKey(to='main.Categories')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='island',
            field=models.ForeignKey(to='main.Islands'),
        ),
        migrations.AddField(
            model_name='events',
            name='location',
            field=models.ForeignKey(to='main.Locations'),
        ),
        migrations.AddField(
            model_name='citys',
            name='island',
            field=models.ForeignKey(to='main.Islands'),
        ),
        migrations.AddField(
            model_name='articles',
            name='categorie',
            field=models.ForeignKey(to='main.Categories'),
        ),
        migrations.AddField(
            model_name='articles',
            name='city',
            field=models.ForeignKey(to='main.Citys'),
        ),
        migrations.AddField(
            model_name='articles',
            name='island',
            field=models.ForeignKey(to='main.Islands'),
        ),
        migrations.AddField(
            model_name='articles',
            name='location',
            field=models.ForeignKey(to='main.Locations'),
        ),
        migrations.AddField(
            model_name='articles',
            name='subcategorie',
            field=models.ForeignKey(to='main.Subcategories'),
        ),
    ]
