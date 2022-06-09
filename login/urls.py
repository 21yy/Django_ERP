from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register_user, name="register"),
    path('registerCom/', views.register_company, name="register_com"),
    path('logout/', views.logout, name="logout"),
]