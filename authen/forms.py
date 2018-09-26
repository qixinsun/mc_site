from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        error_messages={
            'required': '用户名不能为空'
        },
        widget=forms.TextInput(
            attrs={
                'placeholder': '请输入用户名'
            }
        )
    )
    password = forms.RegexField(
        '^(?=.*[0-9])(?=.*[a-zA-Z])[0-9a-zA-Z!@#$\%\^\&\*\(\)]{8,32}',
        label='密码',
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '请输入密码，密码同时包含数字和密码'
            }
        ),
        error_messages={'required': '密码不能为空.',
                        'invalid': '密码必须同时包含数字和字母',
                        'min_length': "密码长度不能小于8个字符",
                        'max_length': "密码长度不能大于32个字符"
                        }
    )
    repassword = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '请重复输入密码'
            }
        ),
        error_messages={'required': '确认密码不能为空'})
    email = forms.CharField(
        label='电子邮件',
        error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'},
        widget=forms.EmailInput(
            attrs={
                'placeholder': '请输入电子邮件'
            }
        )
    )
    # phone = forms.RegexField(
    #     '^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$',
    #     label='手机',
    #     error_messages={
    #         'required': '手机号不能为空.',
    #         'invalid': '手机号格式错误.'
    #     }
    # )

    def clean(self):
        pwd = self.cleaned_data.get('password')
        if pwd:
            rpwd = self.cleaned_data.get('repassword')
            if pwd != rpwd:
                from django.core.exceptions import ValidationError

                raise ValidationError('两次密码输入不一致')


class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        error_messages={
            'required': '用户名不能为空'
        },
        widget=forms.TextInput(
            attrs={
                'placeholder': '请输入用户名或邮箱'
            }
        )
    )
    password = forms.CharField(
        label='密码',
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '请输入密码'
            }
        ),
        error_messages={'required': '密码不能为空.',
                        'invalid': '密码必须同时包含数字和字母',
                        'min_length': "密码长度不能小于8个字符",
                        'max_length': "密码长度不能大于32个字符"
                        }
    )
