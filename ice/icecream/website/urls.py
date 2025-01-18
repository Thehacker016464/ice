from django.urls import path
from website import views
urlpatterns = [
    
    path('', views.home),
    path('register/', views.user_register),

    path('menu/', views.user_menu),
    path('ingridient/', views.user_ingridient),
    path('login/', views.user_login),
]
