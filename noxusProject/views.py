from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



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
                # for user quality of life Ex.(user search "A" >> it will show all champ start with "A")
                if (x.lower().__contains__(querylist[i].lower())): 
                    return search(request,querylist[i])
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

def search(request,champion_name):
    context = {}
    context['champion'] = Champion.objects.filter(name__startswith=champion_name)
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
	return redirect('index')

class BuildCreate(LoginRequiredMixin,CreateView):
    model = Build
    fields = ['build_name', 'champion','starter1','starter2',
    'items_1',
    'items_2',
    'items_3',
    'items_4',
    'items_5',
    'items_6',
    'spell1',
    'spell2',
    'key_stone', 
    'row1',
    'row2',
    'row3',
    'sub_row1',
    'sub_row2',
    ]
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BuildUpdate(UpdateView,UserPassesTestMixin,LoginRequiredMixin):
    model = Build
    fields = ['build_name', 'champion','starter1','starter2',
    'items_1',
    'items_2',
    'items_3',
    'items_4',
    'items_5',
    'items_6',
    'spell1',
    'spell2',
    'key_stone', 
    'row1',
    'row2',
    'row3',
    'sub_row1',
    'sub_row2',
    ]
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        build = self.get_object()
        if self.request.user == build.user:
            return True
        return False

    
class BuildDelete(DeleteView,UserPassesTestMixin,LoginRequiredMixin):
    model = Build

def my_build(request):
    champion = Build.objects.filter(user = request.user)
    context = {'build': champion}
    return HttpResponse(render(request,'noxusProject/build_user.html',context))
    
def detail_build(request,name):
    champion = Build.objects.get(build_name = name)
    context = {'champion': champion}
    return HttpResponse(render(request,'noxusProject/detail_user.html',context))
    

