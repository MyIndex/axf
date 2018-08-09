from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from axf.models import axf_wheel, axf_nav, axf_mustbuy, axf_shop, axf_mainshow, axf_foodtypes, axf_goods


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


def market_by_typeid(request,typeid,sort=0,childtypenames=0):
    # 全部类别
    foodtypes = axf_foodtypes.objects.all()
    # 升序
    if sort == '1':
        goodslist = axf_goods.objects.filter(categoryid=typeid).order_by('price')
    # 降序
    elif sort == '2':
        goodslist = axf_goods.objects.filter(categoryid=typeid).order_by('-price')
    # 销量
    elif sort == '3':
        goodslist = axf_goods.objects.filter(categoryid=typeid).order_by('productnum')
    else:
        goodslist = axf_goods.objects.filter(categoryid=typeid)

    if childtypenames != '0':
        goodslist = goodslist.filter(childcid = childtypenames)

    # 对类别进行切割
    goodstype = axf_foodtypes.objects.filter(typeid = typeid).first()
    # ['全部分类:0', '进口水果:103534', '国产水果:103533']
    typelist = goodstype.childtypenames.split('#')
    types = []
    for str in typelist:
        types.append(str.split(':'))
    # [['全部分类', '0'], ['进口水果', '103534'], ['国产水果', '103533']]
    # print(types)
    data = {
        'title': '闪购',
        'foodtypes': foodtypes,
        'goodslist': goodslist,
        'typeid': typeid,
        'type': types,
        'childtypenames': childtypenames,

    }
    return render(request, 'market.html', data)

def market(requetst):
    # 回转
    return redirect('/market_by_typeid/104749/0/0/')

def shopcar(request):
    data = {
        'title': '购物车',
    }

    return render(request, 'shopcar.html', data)