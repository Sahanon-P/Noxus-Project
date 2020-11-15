from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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
    return HttpResponse(render(request,'noxusProject/index.html',context))

def detail(request, champion_name):
    champion  = Champion.objects.get(name=champion_name)
    item_champion = ItemChampion.objects.get(name = champion_name)
    starter1 = item_champion.starter1
    starter2 = item_champion.starter2
    items_1 = item_champion.items_1
    items_2 = item_champion.items_2
    items_3 = item_champion.items_3
    items_4 = item_champion.items_4
    items_5 = item_champion.items_5
    items_6 = item_champion.items_6
    context = {'champion':champion,
                'starter1':starter1,
                "starter2":starter2,
                "items_1":items_1,
                "items_2":items_2,
                "items_3":items_3,
                "items_4":items_4,
                "items_5":items_5,
                "items_6":items_6
    }
    # context = {'champion':champion}
    return HttpResponse(render(request,'noxusProject/detail.html',context))

def contact(request):
    return HttpResponse(render(request,'noxusProject/contact.html'))

