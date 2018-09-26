from django.db import models
from authen.models import *
from car.models import *

# Create your models here.
# 消息记录
class Notice(models.Model):
    user = models.ForeignKey(User, verbose_name='所属用户')
    content = models.CharField(max_length=200, verbose_name='通知内容')
    n_time = models.DateTimeField(auto_now=True, verbose_name='通知时间')

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = verbose_name_plural = '消息记录'


# 用户账户信息
class UserAccount(models.Model):
    user = models.OneToOneField(User, verbose_name='所属用户')
    yue = models.IntegerField('账户余额', default=0)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = verbose_name_plural = '用户账户'


# 账户记录
class AccountRecord(models.Model):
    user = models.ForeignKey(User, verbose_name='所属用户')
    p_type = models.CharField(max_length=30, verbose_name='类型')
    p_intro = models.CharField(max_length=200, verbose_name='附加说明')
    amount = models.IntegerField('交易金额')
    p_time = models.DateTimeField(auto_now=True, verbose_name='操作时间')

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = verbose_name_plural = '账户记录'


# 购买记录
class PayRecord(models.Model):
    car = models.ForeignKey(Car, verbose_name='车型')
    user = models.ForeignKey(User, verbose_name='所属用户')
    is_paied = models.BooleanField(verbose_name='是否付清', default=True)
    p_type = models.CharField(max_length=30, verbose_name='付款方式')
    cost = models.IntegerField('本次支付金额', null=True)
    costed = models.IntegerField('已支付金额', null=True)
    pay_time = models.DateTimeField('付款时间',auto_now=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = verbose_name_plural = '购买记录'
