from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from axf.models import axf_wheel, axf_nav, axf_mustbuy, axf_shop, axf_mainshow, axf_foodtypes, axf_goods, axf_user_info, \
    axf_shopcar


def index(reques):
    return render(reques,'base_main.html')

# 首页
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

# 闪购
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
    # 获取子分类
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

    userid = request.session.get('userid')
    goodsid = request.POST.get('goodsid')
    shopcar = axf_shopcar.objects.filter(user_id=userid).filter(goods_id=goodsid)


    data = {
        'title': '闪购',
        'foodtypes': foodtypes,
        'goodslist': goodslist,
        'typeid': typeid,
        'type': types,
        'childtypenames': childtypenames,
        'shopcar': shopcar,

    }
    return render(request, 'market.html', data)

def market(requetst):
    # 回转
    return redirect('/market_by_typeid/104749/0/0/')


def shopcar(request):
    userid = request.session.get('userid')
    data = {
        'title': '购物车',
    }

    if userid:
        shopcars = axf_shopcar.objects.filter(user=userid)
        data['shopcars'] = shopcars
        return render(request, 'shopcar.html', data)
    else:
        return redirect('/login/')

def login(request):
    return render(request,'login.html')

def dologin(requset):
    username = requset.POST.get('username')
    user = axf_user_info.objects.filter(user_name=username).first()

    requset.session['username'] = username
    requset.session['userid'] = user.id

    return redirect('/home/')

# 添加商品
def addshopcar(request):

    userid = request.session.get('userid')
    goodsid = request.POST.get('goodsid')


    data = {

    }
    # 判断用户是否登录
    if userid:
        shopcar = axf_shopcar.objects.filter(goods_id=goodsid).first()
        # 判断购物车有无此商品
        if shopcar:
            shopcar.goodsNumber += 1
            shopcar.save()
        else:
            shopcar = axf_shopcar()
            shopcar.user_id = userid
            shopcar.goods_id = goodsid
            shopcar.save()
        data['code'] = '0000'
        data['msg'] = '添加成功'
        data['num'] = shopcar.goodsNumber
    else:
        data['code'] = '0009'
        data['msg'] = '请登录'

    return JsonResponse(data)

# 删除物品
def subshopcar(request):
    userid = request.session.get('userid')
    goodsid = request.POST.get('goodsid')

    data = {

    }

    if userid:
        shopcar = axf_shopcar.objects.filter(goods_id=goodsid).first()
        if shopcar:
            if shopcar.goodsNumber ==1:
                shopcar.delete()
                data['num'] = 0
            else:
                shopcar.goodsNumber -= 1
                shopcar.save()
                data['num'] = shopcar.goodsNumber

        data['code'] = '0000'
        data['msg'] = '删除成功'

    else:
        data['code'] = '0009'
        data['msg'] = '请登录'

    return JsonResponse(data)


def shopcarselect(request):
    data = {}
    id = request.POST.get('id')
    print(id)
    check = request.POST.get('check')
    shopcar = axf_shopcar.objects.filter(pk=id).first()
    bl = check == 'true'
    shopcar.isSelecy = bl
    shopcar.save()
    return JsonResponse(data)