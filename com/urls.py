from django.urls import path
from . import views


urlpatterns = [
    path('user_list/', views.user_list, name="user_list"),
    path('add_user/', views.add_user, name='add_user'),
    path('delete_user/',views.delete_user, name='delete_user'),
    path('update_user/', views.update_user, name='update_user'),
    path('pos_list/', views.position_list, name='pos_list'),
]