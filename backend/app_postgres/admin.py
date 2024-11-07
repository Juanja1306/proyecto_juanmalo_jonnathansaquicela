from django.contrib import admin
from .models import TablaPostgres

class TablaPostgresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  # Campos visibles en la lista
    search_fields = ('nombre',)  # Campo de búsqueda
    
admin.site.register(TablaPostgres, TablaPostgresAdmin)
