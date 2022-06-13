from django.db import models
from login.models import Company, User
# Create your models here.


class Store(models.Model):
    store_status = (
        (0, 'open'),
        (1, 'close'),
        (2, 'delete'),
    )
    name = models.CharField(max_length=255, verbose_name='store_name')
    intro = models.CharField(max_length=500, null=True, verbose_name='store_description')
    open_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=store_status)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Goods(models.Model):
    gd_name = models.CharField(max_length=255, verbose_name='goods_name')
    gd_price = models.FloatField(verbose_name='goods_price')
    gd_stock = models.IntegerField(default=0, verbose_name='goods_stock')
    gd_count = models.IntegerField(default=0, verbose_name='sold_count')
    gd_dsc = models.IntegerField(max_length=500, null=True, verbose_name='goods_description')
    gd_add_time = models.DateTimeField(auto_now_add=True, verbose_name='add time')
    gd_store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='store_name')


class GoodsImg(models.Model):
    path = models.ImageField(upload_to="static/images", default="static/images")
    intro = models.TextField('description', null=True, blank=True)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)


class ShopCart(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    cart_add_time = models.DateTimeField(auto_now_add=True)
    sum_cost = models.FloatField(default=0, verbose_name='total_cost')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='order_time')
    sum_cost = models.FloatField(default=0, verbose_name='total_cost')
    recv_name = models.CharField(max_length=100, verbose_name='receiver_name')
    recv_phone = models.CharField(max_length=50, verbose_name='receiver_phone')
    recv_address = models.CharField(max_length=255, verbose_name='receiver_address')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderItem(models.Model):
    goods_id = models.IntegerField()
    goods_img = models.CharField(max_length=255)
    goods_name = models.CharField(max_length=255)
    goods_price = models.FloatField()
    goods_count = models.IntegerField()
    goods_price_all = models.FloatField(verbose_name='total cost')

