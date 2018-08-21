"""DjangoAXF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url

from axf import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home),
    url(r'^index/',views.index),
    url(r'^market/',views.market),
    url(r'^market_by_typeid/(\d+)/(\d+)/(\d+)/',views.market_by_typeid),
    url(r'^login/',views.login),
    url(r'^dologin/',views.dologin),
    url(r'^regist/',views.regist),
    url(r'^doregist/',views.doregist),
    url(r'^checkname/',views.checkname),


    url(r'^addshopcar/',views.addshopcar),
    url(r'^subshopcar/',views.subshopcar),
    url(r'^shopcar/',views.shopcar),
    url(r'^shopcarselect/',views.shopcarselect),
    url(r'^createorder/',views.createorder),
    url(r'^mine/',views.mine),

]
