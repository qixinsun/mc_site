from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    url(r'^$', index),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^active/([\d\w]{50})/$', user_active_view, name='user_active'),
    # url(r'01_login/$', logined),
    # url(r'accounts/login/$', auth_views.LoginView.as_view()),
    url(r'^forget/$', forget_pass, name='forget'),
    url(r'^newpass/([\d\w]{50})/$', new_pass, name='new_pass')
]
