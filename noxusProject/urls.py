from noxusProject.views import search
from django.urls import path
from . import views

app_name = "noxusProject" 
urlpatterns = [
    path('', views.index,name="index"),
    path('<str:role>',views.index, name = "index-role"),
    path("champion/<str:champion_name>" , views.detail, name = 'detail'),
    path("contact/",views.contact, name= "contact")
]