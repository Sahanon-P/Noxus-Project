from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('home', views.index, name='index'),
    path('<str:role>', views.index, name = "index/role"),
    path("champion/<str:champion_name>" , views.detail, name = 'detail')
    # path("create_build" , views.create_build, name = 'create_build')
]