from django.contrib import admin
from .models import ModeloBase, Visitors, AccessSEDE


# Registrar el modelo Visitors con opciones personalizadas
@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ['Dni', 'First_name', 'Last_name', 'Nac', 'gender', 'is_deleted']
    list_filter = ['Nac', 'gender', 'is_deleted']
    search_fields = ['Dni', 'First_name', 'Last_name']
    

# Registrar el modelo AccessSEDE con opciones personalizadas
@admin.register(AccessSEDE)
class AccessSEDEAdmin(admin.ModelAdmin):
    list_display = ['visitor', 'entry', 'hours', 'hoursEx', 'Automovils', 'Licenses', 'obs']
    list_filter = ['entry']
    search_fields = ['visitorID__Dni']
    date_hierarchy = 'entry'
