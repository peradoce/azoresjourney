# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170302_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=60)),
                ('titulo_en', models.CharField(max_length=60, blank=True, null=True)),
                ('titulo_fr', models.CharField(max_length=60, blank=True, null=True)),
                ('titulo_de', models.CharField(max_length=60, blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('booking', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, blank=True, null=True)),
                ('estrelas', models.IntegerField(blank=True, null=True)),
                ('telefone', models.CharField(max_length=15, blank=True, null=True)),
                ('telemovel', models.CharField(max_length=15, blank=True, null=True)),
                ('morada', models.CharField(max_length=75)),
                ('imagem', models.FileField(upload_to='articles_images')),
                ('descricao', models.TextField()),
                ('descricao_en', models.TextField(blank=True, null=True)),
                ('descricao_fr', models.TextField(blank=True, null=True)),
                ('descricao_de', models.TextField(blank=True, null=True)),
                ('hora_aberto', models.TimeField(blank=True, null=True)),
                ('hora_fechado', models.TimeField(blank=True, null=True)),
                ('coordenadas_mapa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BlocoDataEvento',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=60)),
                ('titulo_en', models.CharField(max_length=60, blank=True, null=True)),
                ('titulo_fr', models.CharField(max_length=60, blank=True, null=True)),
                ('titulo_de', models.CharField(max_length=60, blank=True, null=True)),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BlocoHoraEvento',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=60)),
                ('titulo_en', models.CharField(max_length=60, blank=True, null=True)),
                ('titulo_fr', models.CharField(max_length=60, blank=True, null=True)),
                ('titulo_de', models.CharField(max_length=60, blank=True, null=True)),
                ('hora', models.TimeField()),
                ('bloco_evento', models.ForeignKey(to='main.BlocoDataEvento')),
            ],
        ),
        migrations.CreateModel(
            name='Concelho',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('concelho', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='DetalheConcelho',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('historia', tinymce.models.HTMLField()),
                ('historia_en', tinymce.models.HTMLField(blank=True, null=True)),
                ('historia_fr', tinymce.models.HTMLField(blank=True, null=True)),
                ('historia_de', tinymce.models.HTMLField(blank=True, null=True)),
                ('numero_freguesias', models.IntegerField()),
                ('video', models.CharField(max_length=100, blank=True, null=True)),
                ('imagem', models.CharField(max_length=100)),
                ('concelho', models.ForeignKey(to='main.Concelho')),
            ],
        ),
        migrations.CreateModel(
            name='DetalheFreguesia',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('historia', tinymce.models.HTMLField()),
                ('historia_en', tinymce.models.HTMLField(blank=True, null=True)),
                ('historia_fr', tinymce.models.HTMLField(blank=True, null=True)),
                ('historia_de', tinymce.models.HTMLField(blank=True, null=True)),
                ('video', models.CharField(max_length=100, blank=True, null=True)),
                ('imagem', models.FileField(upload_to='location_images')),
            ],
        ),
        migrations.CreateModel(
            name='DetalheIlha',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('historia', tinymce.models.HTMLField()),
                ('historia_en', tinymce.models.HTMLField(blank=True, null=True)),
                ('historia_fr', tinymce.models.HTMLField(blank=True, null=True)),
                ('historia_de', tinymce.models.HTMLField(blank=True, null=True)),
                ('numero_concelhos', models.IntegerField()),
                ('numero_freguesias', models.IntegerField()),
                ('video', models.CharField(max_length=100, blank=True, null=True)),
                ('imagem', models.FileField(upload_to='island_images')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('data_comeco', models.DateField()),
                ('data_fim', models.DateField()),
                ('hora_comeco', models.TimeField()),
                ('hora_fim', models.TimeField()),
                ('imagem', models.FileField(upload_to='city_images')),
                ('video', models.CharField(max_length=100, blank=True, null=True)),
                ('concelho', models.ForeignKey(to='main.Concelho')),
            ],
        ),
        migrations.CreateModel(
            name='Freguesia',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('freguesia', models.CharField(max_length=60)),
                ('concelho', models.ForeignKey(to='main.Concelho')),
            ],
        ),
        migrations.CreateModel(
            name='ImagemArtigo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('imagem', models.FileField(upload_to='articles_images')),
                ('artigo', models.ForeignKey(to='main.Artigo')),
            ],
        ),
        migrations.CreateModel(
            name='ImagemConcelho',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('imagem', models.FileField(upload_to='city_images')),
                ('concelho', models.ForeignKey(to='main.Concelho')),
            ],
        ),
        migrations.CreateModel(
            name='ImagemFreguesia',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('imagem', models.FileField(upload_to='location_images')),
                ('freguesia', models.ForeignKey(to='main.Freguesia')),
            ],
        ),
        migrations.CreateModel(
            name='ImagemIlha',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('imagem', models.FileField(upload_to='island_images')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('subcategoria', models.CharField(max_length=50)),
                ('subcategoria_en', models.CharField(max_length=50)),
                ('subcategoria_fr', models.CharField(max_length=50)),
                ('subcategoria_de', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Categories',
            new_name='Categoria',
        ),
        migrations.RenameModel(
            old_name='RegionalFood',
            new_name='ComidaRegional',
        ),
        migrations.RenameModel(
            old_name='Islands',
            new_name='Ilha',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='city',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='island',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='location',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='subcategorie',
        ),
        migrations.RemoveField(
            model_name='citydetailimage',
            name='city',
        ),
        migrations.RemoveField(
            model_name='citys',
            name='island',
        ),
        migrations.RemoveField(
            model_name='citysdetails',
            name='city',
        ),
        migrations.RemoveField(
            model_name='eventblockdate',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventblockhour',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventblockhour',
            name='event_block',
        ),
        migrations.RemoveField(
            model_name='events',
            name='city',
        ),
        migrations.RemoveField(
            model_name='events',
            name='island',
        ),
        migrations.RemoveField(
            model_name='events',
            name='location',
        ),
        migrations.RemoveField(
            model_name='imagesarticles',
            name='article',
        ),
        migrations.RemoveField(
            model_name='islanddetailimage',
            name='island',
        ),
        migrations.RemoveField(
            model_name='islandsdetails',
            name='island',
        ),
        migrations.RemoveField(
            model_name='locationdetailimage',
            name='location',
        ),
        migrations.RemoveField(
            model_name='locations',
            name='city',
        ),
        migrations.RemoveField(
            model_name='locations',
            name='island',
        ),
        migrations.RemoveField(
            model_name='locationsdetails',
            name='location',
        ),
        migrations.RemoveField(
            model_name='subcategories',
            name='categorie',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='categorie',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='categorie_de',
            new_name='categoria_de',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='categorie_en',
            new_name='categoria_en',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='categorie_fr',
            new_name='categoria_fr',
        ),
        migrations.RenameField(
            model_name='comidaregional',
            old_name='food',
            new_name='comida',
        ),
        migrations.RenameField(
            model_name='comidaregional',
            old_name='recipe',
            new_name='receita',
        ),
        migrations.RenameField(
            model_name='comidaregional',
            old_name='recipe_de',
            new_name='receita_de',
        ),
        migrations.RenameField(
            model_name='comidaregional',
            old_name='recipe_en',
            new_name='receita_en',
        ),
        migrations.RenameField(
            model_name='comidaregional',
            old_name='recipe_fr',
            new_name='receita_fr',
        ),
        migrations.RenameField(
            model_name='ilha',
            old_name='island',
            new_name='ilha',
        ),
        migrations.RemoveField(
            model_name='comidaregional',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
        migrations.DeleteModel(
            name='CityDetailImage',
        ),
        migrations.DeleteModel(
            name='Citys',
        ),
        migrations.DeleteModel(
            name='CitysDetails',
        ),
        migrations.DeleteModel(
            name='EventBlockDate',
        ),
        migrations.DeleteModel(
            name='EventBlockHour',
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.DeleteModel(
            name='ImagesArticles',
        ),
        migrations.DeleteModel(
            name='IslandDetailImage',
        ),
        migrations.DeleteModel(
            name='IslandsDetails',
        ),
        migrations.DeleteModel(
            name='LocationDetailImage',
        ),
        migrations.DeleteModel(
            name='Locations',
        ),
        migrations.DeleteModel(
            name='LocationsDetails',
        ),
        migrations.DeleteModel(
            name='Subcategories',
        ),
        migrations.AddField(
            model_name='subcategoria',
            name='categoria',
            field=models.ForeignKey(to='main.Categoria'),
        ),
        migrations.AddField(
            model_name='imagemilha',
            name='ilha',
            field=models.ForeignKey(to='main.Ilha'),
        ),
        migrations.AddField(
            model_name='freguesia',
            name='ilha',
            field=models.ForeignKey(to='main.Ilha'),
        ),
        migrations.AddField(
            model_name='evento',
            name='freguesia',
            field=models.ForeignKey(to='main.Freguesia'),
        ),
        migrations.AddField(
            model_name='evento',
            name='ilha',
            field=models.ForeignKey(to='main.Ilha'),
        ),
        migrations.AddField(
            model_name='detalheilha',
            name='ilha',
            field=models.ForeignKey(to='main.Ilha'),
        ),
        migrations.AddField(
            model_name='detalhefreguesia',
            name='freguesia',
            field=models.ForeignKey(to='main.Freguesia'),
        ),
        migrations.AddField(
            model_name='concelho',
            name='ilha',
            field=models.ForeignKey(to='main.Ilha'),
        ),
        migrations.AddField(
            model_name='blocohoraevento',
            name='evento',
            field=models.ForeignKey(to='main.Evento'),
        ),
        migrations.AddField(
            model_name='blocodataevento',
            name='evento',
            field=models.ForeignKey(to='main.Evento'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='categoria',
            field=models.ForeignKey(to='main.Categoria'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='concelho',
            field=models.ForeignKey(to='main.Concelho'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='freguesia',
            field=models.ForeignKey(to='main.Freguesia'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='ilha',
            field=models.ForeignKey(to='main.Ilha'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='subcategoria',
            field=models.ForeignKey(to='main.Subcategoria'),
        ),
        migrations.AddField(
            model_name='comidaregional',
            name='restaurante',
            field=models.ManyToManyField(to='main.Artigo'),
        ),
    ]
