from django.contrib import admin
from .models import *
#admin.site.register(Produtos)
#admin.site.register(Carrinho)
#admin.site.register(Clientes)


@admin.register(Produtos)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id","empresa","nome", "descricao","qtd","valor","promocao","image")
    list_filter = ("valor", )
    search_fields = ("nome__startswith", )

@admin.register(Carrinho)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("chave", "pedido","valor","qtd","sub_total")
    list_filter = ("chave", )
    search_fields = ("chave__startswith", )

@admin.register(Clientes)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("pedido", "nome","pagamento","endereco")
    list_filter = ("pedido", )
    search_fields = ("nome__startswith", )

@admin.register(Empresa)
class PersonAdmin(admin.ModelAdmin):
    list_display = ( "id","nome","telefone","endereco","image")
    list_filter = ("nome", )
    search_fields = ("nome__startswith", )    