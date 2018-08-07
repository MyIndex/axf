from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from axf.models import axf_wheel


def index(reques):
    return render(reques,'base_main.html')


def home(request):
    axfwheel = axf_wheel.objects.all()
    data = {
        'title' : '首页',
        'wheels' : axfwheel
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