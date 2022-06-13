from django.urls import path
from . import views


urlpatterns = [
    path('user_list/', views.user_list, name="user_list"),
    path('add_user/', views.add_user, name='add_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('update_user/', views.update_user, name='update_user'),
    path('pos_list/', views.pos_list, name='pos_list'),
    path('update_pos/', views.update_pos, name='update_pos'),
    path('add_pos/', views.add_pos, name='add_pos'),
    path('delete_pos/', views.delete_pos, name='delete_pos'),
]