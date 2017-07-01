from django.contrib import admin
from .models import *
# Register your models here.

class ConcelhoAdmin(admin.ModelAdmin):
    list_display = ('concelho', 'ilha', )


class FreguesiaAdmin(admin.ModelAdmin):
    list_display = ('freguesia', 'concelho', 'ilha', )


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'categoria_en',  )

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('subcategoria', 'categoria', )


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'ilha')


class DetalheIlhaAdmin(admin.ModelAdmin):
    list_display = ('ilha', 'numero_concelhos', 'numero_freguesias', )


class DetalheConcelhoAdmin(admin.ModelAdmin):
    list_display = ('concelho', 'numero_freguesias', )


class DetalheFreguesiaAdmin(admin.ModelAdmin):
    list_display = ('freguesia', )


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ilha', 'data_comeco', 'data_fim', )


class ComidaRegionalAdmin(admin.ModelAdmin):
    list_display = ('comida', )
    filter_horizontal = ('restaurante', )

class ImagemArtigoAdmin(admin.ModelAdmin):
    list_display = ('artigo', )


class ImagemIlhaAdmin(admin.ModelAdmin):
    list_display = ('ilha', )


class ImagemConcelhoAdmin(admin.ModelAdmin):
    list_display = ('concelho', )


class ImagemFreguesiaAdmin(admin.ModelAdmin):
    list_display = ('freguesia', )


admin.site.register(Ilha)
admin.site.register(Concelho, ConcelhoAdmin)
admin.site.register(Freguesia, FreguesiaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(DetalheIlha, DetalheIlhaAdmin)
admin.site.register(DetalheConcelho, DetalheConcelhoAdmin)
admin.site.register(DetalheFreguesia, DetalheFreguesiaAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(ComidaRegional, ComidaRegionalAdmin)
admin.site.register(ImagemArtigo, ImagemArtigoAdmin)
admin.site.register(ImagemIlha, ImagemIlhaAdmin)
admin.site.register(ImagemConcelho, ImagemConcelhoAdmin)
admin.site.register(ImagemFreguesia, ImagemFreguesiaAdmin)
