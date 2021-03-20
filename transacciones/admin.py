from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    '''Admin View for Categoria'''

    list_display = ('id', 'nombre')


@admin.register(Transaccion)
class TransaccionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    '''Admin View for Transaccion'''

    list_display = (
        'titulo',
        'valor',
        'categoria',
        'fecha',
        'hora',
        )

    list_filter = ('categoria',)
    