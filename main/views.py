from django.shortcuts import render, redirect
from main.models import *
from main.models import *
import datetime
# Create your views here.

def index(request):
    lang = ['pt_PT', 'pt_pt', 'pt_BR', 'pt_br', 'pt', 'PT', ]
    if request.LANGUAGE_CODE in lang:
        return redirect("/pt")
    else:
        return redirect("/en")

def indexPT(request):
    select_categories = Categoria.objects.order_by("id")
    select_islands = Ilha.objects.order_by("id")
    select_articles = Artigo.objects.order_by("-id")[:4]
    select_events = Evento.objects.all().order_by("-data_comeco")[:2]
    return render(request, 'lang/pt/index.html', {'cat':select_categories, 'isl':select_islands,
    'events': select_events, 'articles':select_articles})

def articlesPT(request, offset):
    off_value = int(offset)
    get_data = Artigo.objects.get(id=off_value)
    is_hotel = False
    if get_data.categoria.id == 1:
        is_hotel = True
    else:
        is_hotel = False
    return render(request, 'lang/pt/article.html', {'is_hotel':is_hotel, 'data':get_data})

def historyMainPT(request):
    get_island = Ilha.objects.all().order_by("id")[:9]
    return render(request, 'lang/pt/history/main.html', {'islands':get_island})

def historyIslandPT(request, offset):
    off_value = int(offset)
    get_data = DetalheIlha.objects.get(ilha=off_value)
    get_extra_data = ImagemIlha.objects.filter(ilha=off_value)
    get_city = Concelho.objects.filter(ilha=off_value)
    return render(request, 'lang/pt/history/island.html', {'data':get_data, 'extra':get_extra_data,
    'citys':get_city})

def historyCityPT(request, offset):
    off_value = int(offset)
    get_data = DetalheConcelho.objects.get(concelho=off_value)
    get_extra_data = ImagemConcelho.objects.filter(concelho=off_value)
    get_location = Freguesia.objects.filter(concelho=off_value)
    return render(request, 'lang/pt/history/city.html', {'data':get_data, 'extra':get_extra_data,
    'locations':get_location})

def historyLocationPT(request, offset):
    off_value = int(offset)
    get_data = DetalheFreguesia.objects.get(freguesia=off_value)
    get_extra_data = ImagemFreguesia.objects.filter(freguesia=off_value)
    return render(request, 'lang/pt/history/location.html', {'data':get_data, 'extra':get_extra_data})

def searchArticlePT(request):
    if ('cat' and 'isl' in request.GET) and ('ct' not in request.GET):
        count = Artigo.objects.filter(ilha=request.GET['isl'], categoria=request.GET['cat']).count()
        city = Concelho.objects.filter(ilha=request.GET['isl'])
        is_zero = False
        is_search_city = False
        if count > 0:
            is_search_city = False
            is_zero = False
            get_data = Artigo.objects.filter(ilha=request.GET['isl'], categoria=request.GET['cat'])
            island = Ilha.objects.get(id=request.GET['isl'])
            categorie = Categoria.objects.get(id=request.GET['cat'])
        else:
            is_zero = True
        return render(request, 'lang/pt/search_article.html', {'data':get_data, 'island':island,
        'categorie':categorie,'is_zero':is_zero, 'citys':city, 'is_search_city':is_search_city})
    elif ('cat' and 'isl' and 'ct' in request.GET) and ('lc' not in request.GET):
        is_search_city = True
        count = Artigo.objects.filter(ilha=request.GET['isl'], categoria=request.GET['cat'], concelho=request.GET['ct']).count()
        parish = Freguesia.objects.filter(concelho=request.GET['ct'])
        is_zero = False
        if count > 0:
            is_search_city = True
            is_zero = False
            get_data = Artigo.objects.filter(ilha=request.GET['isl'], categoria=request.GET['cat'], concelho=request.GET['ct'])
            island = Ilha.objects.get(id=request.GET['isl'])
            categorie = Categoria.objects.get(id=request.GET['cat'])
        else:
            is_zero = True
        return render(request, 'lang/pt/search_article.html', {'data':get_data, 'island':island,
        'categorie':categorie,'is_zero':is_zero, 'parishes':parish, 'is_search_city':is_search_city})


def eventPT(request):
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho',
    8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}

    today = datetime.date.today()
    m = meses[int(today.month)]
    select_islands = Ilha.objects.order_by("id")
    count = Evento.objects.filter(data_comeco__month=today.month).count()
    is_zero = False
    if count > 0:
        is_zero = False
        get_data = Evento.objects.filter(data_comeco__month=today.month)
        return render(request, 'lang/pt/events/main.html', {'events':get_data, 'month':m, 'is_zero':is_zero,
        'months':meses, 'islands':select_islands})
    else:
        is_zero = True
        return render(request, 'lang/pt/events/main.html', {'month':m, 'is_zero':is_zero, 'months':meses,
        'islands':select_islands})

def searchEventPT(request):
    error = False
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho',
    8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    if 'm' and 'isl' in request.GET:
        error = False
        get_data = Evento.objects.filter(data_comeco__month=request.GET['m'], ilha=request.GET['isl'])
        m = meses[int(request.GET['m'])]
        get_island = Ilha.objects.get(id=request.GET['isl'])
        return render(request, 'lang/pt/events/search.html', {'events':get_data, 'month':m, 'island':get_island})

def eventShowPT(request, offset):
    off_value = int(offset)
    get_data = Evento.objects.get(id=off_value)
    return render(request, 'lang/pt/events/event.html', {'data':get_data})

def indexEN(request):
    lan = request.LANGUAGE_CODE
    return render(request, 'lang/en/index.html', {'lan':lan, })
