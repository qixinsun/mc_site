from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # user_name = models.CharField(max_length=30, verbose_name='用户名')
    # phone = models.CharField(max_length=11, verbose_name='联系方式')
    email = models.EmailField(verbose_name='电子邮件', unique=True)
    user_active = models.BooleanField(verbose_name='用户可用', default=False)
    image = models.ImageField(upload_to='static/user/images', default='static/user/images/default.png',verbose_name='用户头像')

    class Meta:
        verbose_name = verbose_name_plural = '用户'


class EmailVerify(models.Model):
    code = models.CharField(max_length=100, verbose_name='验证码')
    user = models.OneToOneField(
        User, to_field='email', on_delete=models.CASCADE)
    s_type = models.CharField(max_length=4, verbose_name='类型')
    s_time = models.DateTimeField(verbose_name='发送时间', auto_now=True)

    def __str__(self):
        return '%s(%s)' % (self.user.email, self.s_type)

    def is_expried(self):
        from datetime import datetime, timezone
        return (datetime.now(tz=timezone.utc)-self.s_time).seconds >= 60*30

    class Meta:
        verbose_name = verbose_name_plural = '邮箱验证'

