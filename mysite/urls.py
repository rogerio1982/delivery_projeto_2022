from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 path('admin/', admin.site.urls),
 path('', views.home, name='home'),
 #path('ini/', views.ini, name='ini'),
 path("<int:pk>/", views.home2, name="home2"),
 path("detalhes/<int:pk>/", views.detail, name="detail"),
 path("carrinho/<int:pk>/", views.addCart, name="addCart"),
 path("carrinho/", views.verCar, name="verCar"),
 path("enviar/", views.enviar, name="enviar"),
 path("cadcli/", views.cadcli, name="cadcli"),
 path("cadclichama/", views.cadclichama, name="cadclichama"),
 path("excpedido/<int:pk>/", views.excpedido, name="excpedido"),

 path('logar_usuario/', views.logar_usuario, name="logar_usuario"),
 path('deslogar_usuario/', views.deslogar_usuario, name="deslogar_usuario"),
 path('register/', views.register, name="register"),

 path('emp/', views.emp, name="emp"),
 #path('atuemp/', views.atuemp, name="atuemp"),
 path('atuprod/<int:pk>/', views.atuprod, name="atuprod"),
 path('delprod/<int:pk>/', views.delprod, name="delprod"),

 
 path('cademp/', views.cademp, name="cademp"),
 path('cadprod/', views.cadprod, name="cadprod"),
 path('vis/', views.vis, name="vis"),
 path('chamaini/', views.chamaini, name="chamaini"),
 path('lojas/', views.lojas, name="lojas"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
