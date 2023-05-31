"""gameshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from shop.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage_view, name='mainpage'),
    path('login/', view_login_page, name='loginpage'),
    path('registration/', view_registration_page, name='regpage'),
    path('catalog/', view_catalog, name='catalog'),
    path('game/<int:game_id>/',view_game, name='game'),
    path('profile/',view_profile, name='profile'),
    path('basket/',view_basket, name='basket'),
    path('add-to-cart/<int:game_id>', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:pre_order_id>/', remove_from_cart, name='remove-from-cart'),
    path('order_success/', order_success, name='order_success'),
    path('game/<int:game_id>/add_review/', add_review, name='add_review'),
    path('profile/logout/', logout_view, name='logout'),
    path('dbpanel/',dbpanel,name='dbpanel')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
