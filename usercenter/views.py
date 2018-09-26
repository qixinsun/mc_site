from django.shortcuts import render,redirect
from authen.models import *
from car.models import *
from .models import *
from django.contrib import auth
from django.http import HttpResponse
import os
# Create your views here.


def index(request):
    user = request.user
    print(user.image)
    return render(request, 'usercenter/index.html')


def info(request):
    if request.method == 'GET':
        return render(request, 'usercenter/info.html')
    elif request.method == 'POST':
        upfile = request.FILES.get('pic', None)
        if upfile:
            houzhui = upfile.name.split('.')[-1]
            disk_path = 'static1/upload/usericon/'
            filepath = os.path.join(disk_path, str(request.user.id)+'.'+houzhui)
            des = open(filepath, 'wb+')
            for chunk in upfile.chunks():
                des.write(chunk)
                des.close()
            user = request.user
            user.image = filepath
            user.save()
        
        return redirect('/usercenter/info/')



def ReserverList(request):
    reser_list = ResevationList.objects.filter(resevation_uname=request.user)
    return render(request, 'usercenter/yuyue.html', locals())

def dianping(request):
    return render(request, 'usercenter/dianping.html')

def safe(request):
    return render(request, 'usercenter/safe.html')


def mima(request):
    if request.method == "POST":
        user = request.user
        old = request.POST.get('oldPwd')
        new1 = request.POST.get('newPwd')
        new2 = request.POST.get('confirmPwd')
        print(old)
        if old == "" or new1 == "" or new2 == "":
            result = '请输入完整信息'
        elif new1 != new2:
            result = '请确保密码和确认密码一致'
        elif user.check_password(old):
                user.set_password(new1)
                user.save()
                result = '修改密码成功'
        else:
            result = '原始密码错误'
        print(result)
        return render(request, 'usercenter/mima.html', locals())
    else:
        user = request.user
        return render(request, 'usercenter/mima.html')

def fav(request):
    s = Favorite.objects.get(favorite_user=request.user)
    # print(s)
    allCar = s.favorite_car.all()
    # print(allCar[1].car_href_pic)
    return render(request, 'usercenter/fav.html', locals())

def xiaoxi(request):
    notices = Notice.objects.filter(user=request.user)[::-1]
    count = len(notices)
    return render(request, 'usercenter/xiaoxi.html', locals())

def deleteFavo(request, num_id):
    user = request.user
    fav = Favorite.objects.get(favorite_user=user)
    delete_car = Car.objects.get(id=num_id)
    fav.favorite_car.remove(delete_car)
    Notice.objects.create(user=request.user, content='用户 '+request.user.username+' 已取消收藏 '+delete_car.car_name)
    return redirect('/usercenter/fav')

def duibi_view(request):
    cars = request.POST.getlist('car')
    # print(cars)
    result = []
    for car in cars:
        i = Car.objects.get(id=car)
        result.append(i)
    # print(result)
    return render(request, 'usercenter/duibi.html', locals())


def zijin(request):
    if request.method == 'GET':
        return render(request, 'usercenter/zijin.html')
    else:
        m = request.POST.get('addmoney', '')
        if m != '':
            m = int(m)
            uz = request.user.useraccount
            uz.yue = uz.yue + m
            uz.save()
            AccountRecord.objects.create(user=request.user, p_type='充值', p_intro='用户账户充值',
                amount=m)
        return redirect('/usercenter/zijin/')


def jilu(request):
    records = AccountRecord.objects.filter(user=request.user)[::-1]
    count = len(records)
    return render(request, 'usercenter/jilu.html', locals())


def goumai(request):
    records = PayRecord.objects.filter(user=request.user)[::-1]
    count = len(records)
    return render(request, 'usercenter/goumai.html', locals())


def buy_car(request, carid):
    car = Car.objects.get(id=carid)
    ua = request.user.useraccount
    if ua.yue < car.car_price*10000:
        return HttpResponse('余额不足！')
    ua.yue = ua.yue - car.car_price*10000
    ua.save()
    AccountRecord.objects.create(user=request.user,
    p_type='消费',
    p_intro = '购买 '+car.car_name,
    amount = car.car_price*10000)
    PayRecord.objects.create(car = car,
    user=request.user,
    p_type='全款',
    )
    return HttpResponse('购买成功！')
