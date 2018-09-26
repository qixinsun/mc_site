from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django import views
from .models import *
from .utils import *
from .forms import *
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from car.models import *
from usercenter.models import UserAccount
# Create your views here.


class RegisterView(views.View):

    def get(self, request):
        #删除激活过期用户
        evs = EmailVerify.objects.all()
        for ev in evs:
            if ev.is_expried():
                ev.user.delete()
        # 发送注册表单
        form = RegisterForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # print(data)
            if User.objects.filter(username=data['username']):
                return render(request, 'register.html', {
                    'form': form,
                    'error': '该用户名已被使用.'
                })

            if User.objects.filter(email=data['email']):
                return render(request, 'register.html', {
                    'form': form,
                    'error': '该邮箱已被注册.'
                })
            data.pop('repassword')
            user = User.objects.create_user(**data)
            ev = EmailVerify.objects.create(code=random_code(),
                                            user=user, s_type='注册')
            send_html_email(request, ev)           
            email = data['email']
            domain = email.split('@')[1]
            href = 'http://mail.'+domain

            return render(request, 'active.html', {'data': data,
                    'href': href
                })
        else:
            return render(request, 'register.html', {
                'form': form})

class LoginView(views.View):

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return redirect('/admin')
            else:
                return redirect('/car')
        form = LoginForm()
        s = request.META.get('HTTP_REFERER', '/')
        if 'car' in s or 'usercenter' in s:
            request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        else:
            request.session['login_from'] = ""
        # print(request.session['login_from'])
        return render(request, 'login.html', locals())

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        try:
            # print('wht')
            user = User.objects.get(Q(username=username) | Q(email=username))
        except ObjectDoesNotExist:
            # print('wht')
            return render(request, 'login.html', {
                'form': LoginForm(),
                'error': '请检查用户名和密码.'
            })

        if user:
            if not user.check_password(password):
                return render(request, 'login.html', {
                    'form': LoginForm(),
                    'error': '请检查用户名和密码.'
                })
            if user.is_superuser:
                login(request, user)
                return redirect('/admin/')
            else:
                if user.user_active:
                    login(request, user)
                    print('1')
                    if request.session['login_from'] != "":
                        return HttpResponseRedirect(request.session['login_from'])
                    else:
                        return redirect('/car')
                else:
                    print('2')
                    return render(request, 'login.html', {
                        'form': LoginForm(),
                        'error': '当前用户状态异常，不能登录.'
                    })
        else:
            print('fuck')
            return render(request, 'login.html', {
                'form': LoginForm(),
                'error': '请检查用户名和密码.'
            })
# class LoginView(views.View):

#     def get(self, request):
#         form = LoginForm()
#         return render(request, 'login.html', locals())

#     def post(self, request):
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')

#         try:
#             user = User.objects.get(Q(username=username) | Q(email=username))
#         except ObjectDoesNotExist:
#             return render(request, 'login.html', {
#                 'form': LoginForm(),
#                 'error': '请检查用户名和密码.'
#             })

#         if user:
#             if user.is_superuser:
#                 login(request, user)
#                 return redirect('/admin/')
#             if not user.check_password(password):
#                 return render(request, 'login.html', {
#                     'form': LoginForm(),
#                     'error': '请检查用户名和密码.'
#                 })
#             else:
#                 if user.user_active:
#                     login(request, user)
#                     return redirect('/car/')
#                 else:
#                     return render(request, 'login.html', {
#                         'form': LoginForm(),
#                         'error': '当前用户状态异常，不能登录.'
#                     })
#         else:
#             return render(request, 'login.html', {
#                 'form': LoginForm(),
#                 'error': '请检查用户名和密码.'
#             })


def logout_view(request):
    logout(request)
    return redirect('/car')


def user_active_view(request, code):
    try:
        ev = EmailVerify.objects.get(code=code)
    except ObjectDoesNotExist:
        return render(request, 'active_result.html', {
            'error': '激活链接过期, 您需要重新注册.'
        })
    if ev.is_expried():
        ev.user.delete()
        return render(request, 'active_result.html', {
            'error': '激活链接过期, 您需要重新注册.'
        })

    user = ev.user
    ev.delete()
    user.user_active = True
    user.save()
    Favorite.objects.create(favorite_user=user)
    UserAccount.objects.create(user=user)
    return render(request, 'active_result.html',{'user': user})


@login_required
def logined(request):
    return HttpResponse("ok")


def index(request):
    return redirect('/car')


def forget_pass(request):
    if request.method == 'GET':
        return render(request, 'find.html')
    elif request.method == 'POST':
        email = request.POST.get('mail', '')
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return render(request, 'find.html', {'error': '输入邮箱不存在，请检查输入'})
        ev = EmailVerify.objects.create(code=random_code(),
                                            user=user, s_type='找回密码')
        send_html_email(request, ev)
        domain = email.split('@')[1]
        href = 'http://mail.'+domain

        return render(request, 'forget.html', {'user': user,
                'href': href
            })


def new_pass(request, code):
    if request.method == 'GET':
        return render(request, 'reset.html')
    elif request.method == 'POST':
        newpwd = request.POST.get('newpwd', '')
        rnewpwd = request.POST.get('rnewpwd', '')
        if newpwd != rnewpwd:
            return render(request, 'reset.html',{'error': '两次密码输入不一致'})
        else:
            try:
                ev = EmailVerify.objects.get(code=code)
            except ObjectDoesNotExist:
                return render(request, 'reset.html',{'error': '当前链接失效，请重新请求.'})
            if ev.is_expried():
                ev.delete()
                return render(request, 'reset.html',{'error': '当前链接失效，请重新请求.'})
            else:
                user = ev.user
                user.set_password(newpwd)
                user.save()
                ev.delete()
                return redirect('/login/')
