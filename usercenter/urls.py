from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^info/$', info, name='info'),
    url(r'^yuyue/$', ReserverList, name='yuyue'),
    url(r'^dianping/$', dianping, name='dianping'),
    url(r'^safe/$', safe, name='safe'),
    url(r'^mima/$', mima, name='mima'),
    url(r'^fav/$', fav, name='fav'),
    url(r'^xiaoxi/$', xiaoxi, name='xiaoxi'),
    url(r'^deleteFavo/([0-9]+)$', deleteFavo, name = 'deleteFavo'),
    url(r'^duibi$', duibi_view, name = 'duibi'),
    url(r'^zijin/$', zijin, name='zijin'),
    url(r'^jilu/$', jilu, name='jilu'),
    url(r'^goumai/$', goumai, name='goumai'),
    url(r'^bycar/(\d+)/$', buy_car, name='buycar'),
]
