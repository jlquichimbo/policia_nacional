from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.persona_list, name='home'),
    path('persona_list', views.persona_list, name='persona_list'),
    path('persona_create', views.persona_create, name='persona_create'),
    path('persona_detail/<pk>', views.persona_detail, name='persona_detail'),
    path('persona_edit/<pk>', views.persona_edit, name='persona_edit'),
    path('persona_delete/<pk>', views.persona_delete, name='persona_delete'),
]