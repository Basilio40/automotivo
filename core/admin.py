from django.contrib import admin
from .models import Marca , Automotivo,Person

# Register your models here.

class AutomoveisAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca','ano','modelo') # mostra os itens listados na tupla ao lado no admin
    search_fields = ['patente','modelo'] # cria uma barra de busca no django admin
    list_filter = ['marca'] # cria um filtro no django admin

admin.site.register(Marca)
admin.site.register(Automotivo, AutomoveisAdmin)
admin.site.register(Person)