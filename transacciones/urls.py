from django.urls import path, re_path
from transacciones import views

urlpatterns = [
    path('ingreso_form', views.IngresoCreateView.as_view(), name='ingreso_form'),
    path('ingreso_list', views.ingreso_list, name='ingreso_list'),
    path('gasto_form', views.GastoCreateView.as_view(), name='gasto_form'),
    path('gasto_list', views.gasto_list, name='gasto_list'),
]
