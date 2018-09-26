import random
from django.core.mail import EmailMessage
from django.template import loader
# from .models import EmailVerify
from mc_site.settings import DEFAULT_FROM_EMAIL


def random_code(length=50):
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    code = ''
    for i in range(length):
        code += chars[random.Random().randint(0, len(chars) - 1)]
    return code


def send_html_email(request, ev):
    if ev.s_type == '注册':
        html_content = loader.render_to_string(
            'register_active.html',
            # 传入的参数
            {
                'code': ev.code,
                'username': ev.user.username,
                'email': ev.user.email,
                'host': request.get_host()
            }
        )
        msg = EmailMessage('MC网用户注册激活链接', html_content,
                           DEFAULT_FROM_EMAIL, [ev.user.email, ])
        msg.content_subtype = 'html'
        msg.send()
    elif ev.s_type == '找回密码':
        html_content = loader.render_to_string(
            'mail_forget.html',
            # 传入的参数
            {
                'code': ev.code,
                'username': ev.user.username,
                'email': ev.user.email,
                'host': request.get_host()
            }
        )
        msg = EmailMessage('MC网用户找回密码链接', html_content,
                           DEFAULT_FROM_EMAIL, [ev.user.email, ])
        msg.content_subtype = 'html'
        msg.send()
