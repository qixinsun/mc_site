from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^detail/(\d+)$', detail, name='car_detail'),
    url(r'^addFav/(\d+)$', addFav, name= 'addFav'),
    url(r'^compare/', compare, name="compare"),
    url(r'^get_cars/$', get_cars_by_brand, name='get_cars_by_brand'),
    url(r'^deletFav/(\d+)$',deleteFav,name='deleteFav'),
    url(r'^filter/$', filter_cars, name='filter'),
    url(r'^get_filter_cars/', get_filter_cars, name='filter_cars'),
]
