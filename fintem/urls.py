# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("transacciones/", include(("transacciones.urls", 'transacciones'), namespace='transacciones')),             # Transacciones
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),           # UI Kits Html files
    # path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    
]
