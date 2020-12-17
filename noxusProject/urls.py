from noxusProject.views import search
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('<str:role>',views.index, name = "index-role"),
    path("champion/<str:champion_name>" , views.detail, name = 'detail'),
    path("contact/",views.contact, name= "contact"),
    path("user/register/",views.register, name = 'register'),
    path("user/login/",views.loginPage, name = 'login'),
    path("user/logout/",views.logoutPage, name = 'logout'),
    path("build/",views.my_build, name = 'my_build'),
    path("build/<int:pk>",views.detail_build, name = 'detail_build'),
    path('build/create/', views.BuildCreate.as_view(), name='build_create'),
    path('build/<int:pk>/update/', views.BuildUpdate.as_view(), name='build_update'),
    path('build/<int:pk>/delete/', views.BuildDelete.as_view(), name='build_delete'),

]