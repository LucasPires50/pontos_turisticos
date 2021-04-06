"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet

routers = routers.DefaultRouter()
routers.register(r'pontoturistico', PontoTuristicoViewSet,
                 basename='PontoTuristico')
routers.register(r'atracoes', AtracaoViewSet)
routers.register(r'enderecos', EnderecoViewSet)
routers.register(r'comentarios', ComentarioViewSet)
routers.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('admin/', admin.site.urls),
]
