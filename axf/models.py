from django.db import models

# Create your models here.
class axf_base(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

class axf_wheel(axf_base):

    class Meta:
        db_table = 'axf_wheel'
# 导航
class axf_nav(axf_base):

    class Meta:
        db_table = 'axf_nav'

# 最火商品
class axf_mustbuy(axf_base):
    class Meta:
        db_table = 'axf_mustbuy'
# 商品
class axf_shop(axf_base):
    class Meta:
        db_table = 'axf_shop'
#
class axf_mainshow(axf_base):
    categoryid = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=20)
    productid1 = models.CharField(max_length=20)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=20)
    marketprice1 = models.CharField(max_length=20)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=20)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=20)
    marketprice2 = models.CharField(max_length=20)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=20)
    productid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=20)
    marketprice3 = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_mainshow'
# 商品类型
class axf_foodtypes(models.Model):
    typeid = models.CharField(max_length=20)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=0)
    class Meta:
        db_table = 'axf_foodtypes'
# 商品model
class axf_goods(models.Model):
    productid = models.CharField(max_length=20)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=200)
    productlongname = models.CharField(max_length=200)
    isxf = models.IntegerField(default=0)
    pmdesc = models.IntegerField(default=0)
    specifics = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    marketprice = models.FloatField(default=0)
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=10)
    storenums = models.IntegerField()
    productnum = models.IntegerField()
    class Meta:
        db_table = 'axf_goods'
# 用户信息
class axf_user_info(models.Model):
    user_name = models.CharField(max_length=64)
    user_pass = models.CharField(max_length=100)

    class Meta:
        db_table = 'axf_user_info'
# 购物车
class axf_shopcar(models.Model):
    user = models.ForeignKey('axf_user_info')
    goods = models.ForeignKey('axf_goods')
    goodsNumber = models.IntegerField(default=1)
    isSelecy = models.BooleanField(default=False)
    class Meta:
        db_table = 'axf_shopcar'


# 订单
class axf_order(models.Model):
    user = models.ForeignKey('axf_user_info')
    # 0：待支付   1：已支付  2：已发货   3：已收货  4：已评价   5：已退款
    status = models.IntegerField(default=0)
    createDate = models.DateTimeField(auto_now_add=True)
    orderNumber = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_order'
#订单详情
class axf_order_info(models.Model):
    order = models.ForeignKey('axf_order')
    goods = models.ForeignKey('axf_goods')
    goodsNumber = models.IntegerField(default=1)
    goodsmoney = models.FloatField(default=1)

    class Meta:
        db_table = 'axf_order_info'














