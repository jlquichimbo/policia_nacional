from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('persona_list', views.persona_list, name='persona_list'),
    path('persona_create', views.persona_create, name='persona_create'),
]