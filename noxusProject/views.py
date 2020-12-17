from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import CreateUserForm, BuildForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# Create your views here.
def index(request,role=""):
    """Index page showed by filter roll and can search the champion"""

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
        if not query.isalpha():
            return HttpResponse(render(request,'noxusProject/error.html'))
        for x in all_champ:
            for i in range(len(querylist)):
                # for user quality of life Ex.(user search "A" >> it will show all champ start with "A")
                if (x.capital().__contains__(querylist[i].capitalize())): 
                    return search(request,querylist[i].capitalize())
        if query:
            return HttpResponse(render(request,'noxusProject/error.html'))
    return HttpResponse(render(request,'noxusProject/index.html',context))

def detail(request, champion_name):
    """Detail page show the best build of that champion."""

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
    """Searching the champion name by filter the character in their name."""

    context = {}
    context['champion'] = Champion.objects.filter(name__startswith=champion_name)
    return HttpResponse(render(request,'noxusProject/search.html',context))

def contact(request):
    """Contact button which could redirect to contact page."""

    return HttpResponse(render(request,'noxusProject/contact.html'))

def register(request):
    """Register the user by enter username and password."""

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
    """Login page of user. After login the website will redirect to index page."""

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
    """Logout page. After logout, it will redirect to index page."""

    logout(request)
    return redirect('index')

class BuildCreate(LoginRequiredMixin,CreateView):
    """Class for make the user create build."""

    model = Build
    form_class = BuildForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BuildUpdate(UpdateView,UserPassesTestMixin,LoginRequiredMixin):
    """Update the old build to the new one."""

    model = Build
    form_class = BuildForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        build = self.get_object()
        if self.request.user == build.user:
            return True
        return False

    
class BuildDelete(DeleteView,UserPassesTestMixin,LoginRequiredMixin):
    """Delete the build."""

    model = Build
    success_url = "/build/"
    def test_func(self):
        build = self.get_object()
        if self.request.user == build.user:
            return True
        return False

def my_build(request):
    if request.user.is_authenticated:
        champion = Build.objects.filter(user = request.user)
        context = {'build': champion}
        return HttpResponse(render(request,'noxusProject/build_user.html',context))
    else:
        return redirect('index')
    
def detail_build(request,pk):
    if request.user.is_authenticated:
        champion = Build.objects.get(id = pk)
        context = {'champion': champion}
        return HttpResponse(render(request,'noxusProject/detail_user.html',context))
    else:
        return redirect('index')
