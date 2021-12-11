from django.contrib import admin
from .models import Categoria, Cliente

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'data_inclusao', 'categoria', 'situacao', 'mostrar')
    list_display_links = ('nome', 'cpf')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'cpf')
    list_editable = ('mostrar'),


admin.site.register(Categoria)
admin.site.register(Cliente, ClienteAdmin)
