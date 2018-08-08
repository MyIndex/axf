from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from axf.models import axf_wheel, axf_nav, axf_mustbuy, axf_shop, axf_mainshow


def index(reques):
    return render(reques,'base_main.html')


def home(request):
    axfwheel = axf_wheel.objects.all()
    axfnav = axf_nav.objects.all()
    axfmustbuy = axf_mustbuy.objects.all()
    axfshop = axf_shop.objects.all()
    shop1 = axfshop[0]
    shop2 = axfshop[1:3]
    shop3 = axfshop[3:7]
    shop4 = axfshop[7:11]

    axfshow = axf_mainshow.objects.all()


    data = {
        'title' : '首页',
        'wheels' : axfwheel,
        'navs': axfnav,
        'mustbuy' : axfmustbuy,
        'shop_0': shop1,
        'shop_1_3': shop2,
        'shop_3_7' : shop3,
        'shop_7_11': shop4,
        'mainshows': axfshow,

    }

    return render(request,'home.html',data)


def market(request):

    data = {
        'title': '闪购',

    }

    return render(request, 'market.html', data)


def shopcar(request):
    data = {
        'title': '购物车',
    }

    return render(request, 'shopcar.html', data)