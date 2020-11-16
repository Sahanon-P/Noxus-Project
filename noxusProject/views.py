from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import reset_queries



# Create your views here.
def index(request,role=""):
    context = {}
    if role == "top":
        context['champion'] = Champion.objects.filter(top = True).all()
    elif role == "jungle":
        context['champion'] = Champion.objects.filter(jungler = True).all()
    elif role == "mid":
        context['champion'] = Champion.objects.filter(mid = True).all()
    elif role == "adc":
        context['champion'] = Champion.objects.filter(adc = True).all()
    elif role == "support":
        context['champion'] = Champion.objects.filter(support = True).all()
    else:
        context['champion'] = Champion.objects.all()
    if request.GET:
        query = request.GET.get("search")
        all_champ = Champion.objects.all()
        querylist = query.split(" ")
        for x in all_champ:
            for i in range(len(querylist)):
                if (querylist[i].lower() == x.lower()):
                    try:
                        return detail(request,x)
                    except ItemChampion.DoesNotExist:
                        return HttpResponse(render(request,'noxusProject/error.html'))
        if query:
            return HttpResponse(render(request,'noxusProject/error.html'))
    return HttpResponse(render(request,'noxusProject/index.html',context))

def detail(request, champion_name):
    champion  = Champion.objects.get(name=champion_name)
    item_champion = ItemChampion.objects.get(name = champion_name)
    rune_champion = RuneChampion.objects.get(name = champion_name)
    spell = SummonnerSpellChampion.objects.get(name = champion_name)
    context = {'champion':champion,
                'items' : item_champion,
                'runes' : rune_champion,
                'summonner_spell' : spell
    }
    return HttpResponse(render(request,'noxusProject/detail.html',context))


