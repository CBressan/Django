"""projeto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from .views import anne
from .views import ano
from .views import fnome2
from django.conf import settings
from django.conf.urls.static import static
from clientes import urls as clients_urls

urlpatterns = [
                  path('anne', anne),
                  path('year/<int:year>', ano),  # a url é year/algumano
                  path('pessoa/<str:nome>', fnome2),
                  path('admin/', admin.site.urls),
                  path('person/', include(clients_urls))
              ] + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)  # todos os patterts de path, ou seja, as url que já temos configuradas
# irá adicionar a elas a url de media_url e qd acessar a url, acessará o media_root, ou seja, a pasta de media que estão as fotos, assim,
# será capaz de servir (em tempo de desenvolvimento) o arquivo quando clicamos nele, no site. Ou sejam o arquivo q o usuário subiu, poderemos
# visualizar. É uma GAMBIARRA temporária para testar a aplicação
