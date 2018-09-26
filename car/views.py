from django.shortcuts import render, redirect
from .models import *
from car.models import *
from django.http import JsonResponse, HttpResponseRedirect
import random
from usercenter.models import Notice
# Create your views here.


def index(request):
    # cars = Car.objects.all()
    # return render(request, 'index.html', locals())
    rm_area = CarSpecialArea.objects.get(spec_area_name='热卖专区')
    jd_area = CarSpecialArea.objects.get(spec_area_name='经典专区')
    zx_area = CarSpecialArea.objects.get(spec_area_name='最新车型')
    cars = Car.objects.all()
    carousels = Carousel.objects.filter(is_use=True)
    rm_cars = Car.objects.filter(car_spec_area=rm_area)
    cars1 = rm_cars[::3]
    cars2 = rm_cars[1::3]
    cars3 = rm_cars[2::3]
    return render(request, 'index.html', locals())


def detail(request, car_id):
    if request.method == 'GET':
        user = request.user
        exist = False
        car = Car.objects.get(id=car_id)
        if user.is_authenticated:
            # car = Car.objects.get(id=car_id)
            # print(car)
            fav = Favorite.objects.get(favorite_user=user)
            result = fav.favorite_car.filter(id=car_id)
            # print(result)
            if result.exists():
                exist = True
        a = Car.objects.values('id')
        b = []
        for i in a:
            b.append(i['id'])
        interestNumber = random.sample(b, 3)
        interestcar = []
        for i in interestNumber:
            interestcar.append(Car.objects.get(id=i))
            # print(interestcar)
        car_imgs = CarImage.objects.filter(car=car)
        return render(request, 'detail.html', locals())
    if request.method == 'POST':
        r_name = request.POST.get('r_name', '')
        a_u_name = request.POST.get('a_u_name', '')
        a_u_phone = request.POST.get('a_u_phone', '')
        sale_name = request.POST.get('sale_name', '')
        sale_phone = request.POST.get('sale_phone', '')
        r_place = request.POST.get('r_place', '')
        r_date = request.POST.get('r_date', '')
        car_name = Car.objects.filter(id=car_id)[0]
        ResevationList.objects.create(
            resevation_list_name=r_name,
            a_user_name=a_u_name,
            a_user_telephone=a_u_phone,
            sale_name=sale_name,
            sale_telephone=sale_phone,
            meet_place=r_place,
            meet_time=r_date,
            resevation_time=r_date,
            resevation_car=car_name,
            resevation_uname=request.user)
        Notice.objects.create(user=request.user, content='用户'+request.user.username+' 已预约 '+car_name.car_name+' .')
        return HttpResponseRedirect("/car/detail/"+str(car_id))
    else:
        return HttpResponse("预约失败！")


def addFav(request, car_id):
    user = request.user
    if user.is_authenticated:

        fav = Favorite.objects.filter(favorite_user=user)
        if not fav:
            Favorite.objects.create(favorite_user=user)
        fav = Favorite.objects.get(favorite_user=user)
        add_car = Car.objects.get(id=car_id)
        fav.favorite_car.add(add_car)
        Notice.objects.create(user=request.user, content='用户 '+request.user.username+' 已收藏 '+add_car.car_name)
        return redirect('/car/detail/' + car_id)
    else:
        return redirect('/login')


def compare(request):
    car1_id = request.GET.get('car1', '')
    car2_id = request.GET.get('car2', '')
    car3_id = request.GET.get('car3', '')
    car4_id = request.GET.get('car4', '')
    brands = CarBrand.objects.all()
    try:
        car1 = Car.objects.get(id=car1_id)
    except Exception as e:
        pass
    try:
        car2 = Car.objects.get(id=car2_id)
    except Exception as e:
        pass
    try:
        car3 = Car.objects.get(id=car3_id)
    except Exception as e:
        pass
    try:
        car4 = Car.objects.get(id=car4_id)
    except Exception as e:
        pass

    return render(request, 'duibi.html', locals())


def get_cars_by_brand(request):
    brand_id = request.POST.get('brand', '')
    cars = Car.objects.filter(car_brand=brand_id)
    objs = []
    for car in cars:
        obj = {}
        obj['id'] = car.id
        obj['name'] = car.car_name
        objs.append(obj)
    return JsonResponse({"res": objs})


def deleteFav(request, num_id):
    user = request.user
    fav = Favorite.objects.get(favorite_user=user)
    delete_car = Car.objects.get(id=num_id)
    fav.favorite_car.remove(delete_car)
    Notice.objects.create(user=request.user, content='用户 '+request.user.username+' 已取消收藏 '+delete_car.car_name)
    return redirect('/car/detail/' + num_id)


def filter_cars(request):
    # c_b = CarBrand.objects.get(barnd_name=a)
    # cars = Car.objects.filter(car_brand=c_b)
    brands = CarBrand.objects.all()
    types = CarType.objects.all()
    return render(request, 'filter.html', locals())


def get_filter_cars(request):
    kw = request.GET.get('kw', '')
    if kw:
        from django.db.models import Q
        cars = Car.objects.filter(
            Q(car_brand__barnd_name__contains=kw) |
            Q(car_type__type_name__contains=kw) |
            Q(car_name__contains=kw)
        )
    else:
        a = request.GET.get('a', '')
        b = request.GET.get('b', '')
        c = request.GET.get('c', '')
        d = request.GET.get('d', '')
        e = request.GET.get('e', '')
        if d == '':
            cars = Car.objects.filter(car_brand__barnd_name__contains=a,
                                      car_type__type_name__contains=e,
                                      )
        else:
            import re
            ran = re.match(r'(\d+)-(\d+)\w+', d)
            if not ran:
                cars = Car.objects.filter(car_brand__barnd_name__contains=a,
                                          car_type__type_name__contains=e,
                                          car_price__gt=d[:2]
                                          )
            else:
                cars = Car.objects.filter(car_brand__barnd_name__contains=a,
                                          car_type__type_name__contains=e,
                                          car_price__gt=ran.group(1),
                                          car_price__lt=ran.group(2))
    data = []
    for car in cars:
        obj = {}
        obj['name'] = car.car_name
        obj['price'] = car.car_price
        obj['pic'] = '/' + str(car.car_href_pic)
        obj['id'] = car.id
        data.append(obj)
    return JsonResponse({'data': data})
