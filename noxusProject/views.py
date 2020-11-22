from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout


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
    query = request.GET.get('search')
    try:
        if query:
            return search(request,query)
    except Champion.DoesNotExist:
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


def search(request,champion_name):
    champion  = Champion.objects.get(name=champion_name)
    context = {'champ':champion}
    return HttpResponse(render(request,'noxusProject/search.html',context))

def contact(request):
    return HttpResponse(render(request,'noxusProject/contact.html'))

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,f"The Account has been created : {user}")
            return redirect('login')
    context = {'form':form}
    return HttpResponse(render(request,'noxusProject/sign_up.html',context))

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			user_name = request.POST.get('username')
			passcode =request.POST.get('password')

			user = authenticate(request, username=user_name, password=passcode)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'noxusProject/login.html', context)


def logoutPage(request):
	logout(request)
	return redirect('login')
    
    

