from django.db import models
from authen.models import *
# Create your models here.
# 车辆的车型


class CarType(models.Model):
    type_name = models.CharField(max_length=50, verbose_name='类型名称')
    type_desc = models.CharField(max_length=50, verbose_name='类型描述', null=True)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name_plural = verbose_name = '车辆类型'
# 车辆的品牌


class CarBrand(models.Model):
    barnd_name = models.CharField(max_length=50, verbose_name='品牌名称')
    barnd_desc = models.CharField(
        max_length=50, verbose_name='品牌描述', null=True)

    def __str__(self):
        return self.barnd_name

    class Meta:
        verbose_name_plural = verbose_name = '车辆品牌'
# 专区


class CarSpecialArea(models.Model):
    spec_area_name = models.CharField(max_length=50, verbose_name='专区名称')
    spec_area_desc = models.CharField(
        max_length=100, verbose_name='专区描述', null=True)

    def __str__(self):
        return self.spec_area_name

    class Meta:
        verbose_name_plural = verbose_name = '车辆专区'

# 车辆的信息


class Car(models.Model):

    # CarId = models.CharField(max_length=20,primary_key=True,verbose_name='车辆id')
    car_name = models.CharField(max_length=100, verbose_name='车辆名称')
    car_price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='车辆价格')
    car_body_work = models.CharField(max_length=40, verbose_name='车身结构')
    car_l_w_h = models.CharField(max_length=40, verbose_name='长/宽/高')
    car_engine = models.CharField(max_length=40, verbose_name='发动机')
    car_gear_box = models.CharField(max_length=40, verbose_name='变速箱')
    car_drive_way = models.CharField(max_length=40, verbose_name='驱动方式')
    car_fuel_type = models.CharField(max_length=20, verbose_name='燃料类型')
    car_oil_cons = models.CharField(max_length=20, verbose_name='综合油耗')
    car_color = models.CharField(max_length=220, verbose_name='车辆配色')
    car_href_pic = models.ImageField(
        upload_to='static/cars/hrefs/', verbose_name='车辆图片')
    car_ld_pic = models.ImageField(
        upload_to='static/cars/liangdian', verbose_name='车型亮点')
    car_is_active = models.BooleanField(verbose_name='在售', default=True)
    car_type = models.ForeignKey(CarType, verbose_name='车型')
    car_brand = models.ForeignKey(CarBrand, verbose_name='品牌')
    car_spec_area = models.ForeignKey(
        CarSpecialArea, verbose_name='所属专区', null=True)

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = verbose_name_plural = '车辆信息'


class CarImage(models.Model):
    car_img = models.ImageField(
        upload_to='static/cars/car_images/', verbose_name='车辆图片')
    car = models.ForeignKey(Car, verbose_name='所属车辆')

    def __str__(self):
        return self.car.car_name

    class Meta:
        verbose_name = verbose_name_plural = '车辆图片'

# 预约单信息
class ResevationList(models.Model):
    active = (
        ('0', '等待处理'),
        ('1', '预约成功'),
    )
    resevation_list_name = models.CharField(max_length=50,verbose_name = '预约单名称')
    a_user_name = models.CharField(max_length=50,verbose_name = '预约用户名')
    a_user_telephone = models.CharField(max_length=20,verbose_name ='预约用户联系方式')
    sale_name = models.CharField(max_length=50,verbose_name ='销售员姓名')
    sale_telephone = models.CharField(max_length=20,verbose_name ='销售员联系方式')
    meet_place = models.CharField(max_length=100,verbose_name='预约地点')
    resevation_time = models.DateTimeField(auto_now = True,verbose_name='预约单生成时间')
    meet_time = models.DateField(verbose_name='预约时间')
    resevation_car = models.ForeignKey(Car, verbose_name='预约的车辆')
    resevation_is_active = models.BooleanField(
        default=False, verbose_name='预约成功')
    resevation_uname = models.ForeignKey(
        User, verbose_name='所属用户', null=True)
    def __str__(self):
        return self.resevation_list_name

    class Meta:
        verbose_name_plural = verbose_name = '预约单'
#收藏夹详细信息 
class Favorite(models.Model):
    favorite_car = models.ManyToManyField(Car, verbose_name='收藏的车辆')
    favorite_user = models.OneToOneField(User, verbose_name='所属用户')

    def __str__(self):
        return self.favorite_user.username

    class Meta:
        verbose_name = verbose_name_plural = '收藏夹'

class ImportData(models.Model):
    file = models.FileField(upload_to='File', verbose_name=u'车辆信息')

    class Meta:
        verbose_name = verbose_name_plural = '导入车辆数据'
        ordering = ['file']

    def __str__(self):
        return str(self.file)

class ImportDataFro(models.Model):
    file = models.FileField(upload_to='File', verbose_name=u'车辆类型')

    class Meta:
        verbose_name = verbose_name_plural = '导入车辆类型品牌专区'
        ordering = ['file']

    def __str__(self):
        return str(self.file)

class ImportDataImages(models.Model):
    file = models.FileField(upload_to='File', verbose_name=u'车辆类型')

    class Meta:
        verbose_name = verbose_name_plural = '导入车辆详细图片'
        ordering = ['file']

    def __str__(self):
        return str(self.file)

# 轮播类
class Carousel(models.Model):
    pic = models.ImageField(upload_to='static1/carousels/', verbose_name='轮播图片')
    intro1 = models.CharField(max_length=200, verbose_name='标语1')
    intro2 = models.CharField(max_length=200, verbose_name='标语2')
    is_use = models.BooleanField(default=False, verbose_name='是否显示')

    def __str__(self):
        return self.intro1
    
    class Meta:
        verbose_name = verbose_name_plural = '轮播管理'


class CarPrice(models.Model):
    car = models.OneToOneField(Car, verbose_name='所属车辆')
    shoufu = models.IntegerField('首付（元）', default=4920)
    yuegong = models.IntegerField('月供（元）', default=3547)
    qishu = models.IntegerField('期数', default=12)
    weikuan = models.IntegerField('尾款', default=120000)

    def __str__(self):
        return self.car.car_name
    
    class Meta:
        verbose_name = verbose_name_plural = '分期价格管理'




