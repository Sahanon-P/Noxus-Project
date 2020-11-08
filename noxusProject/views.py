from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    context = {'champion':Champion.objects.all()}
    return HttpResponse(render(request,'noxusProject/index.html',context))

def detail(request, champion_name):
    champion  = Champion.objects.get(name=champion_name)
    item_champion = ItemChampion.objects.get(name = champion_name)
    starter1 = Items.objects.get(id= item_champion.starter1)
    starter2 = Items.objects.get(id= item_champion.starter2)
    items_1 = Items.objects.get(id= item_champion.items_1)
    items_2 = Items.objects.get(id= item_champion.items_2)
    items_3 = Items.objects.get(id= item_champion.items_3)
    items_4 = Items.objects.get(id= item_champion.items_4)
    items_5 = Items.objects.get(id= item_champion.items_5)
    items_6 =Items.objects.get(id= item_champion.items_6)
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

