from django.shortcuts import redirect
import re

def login_middleware(get_response):

    def middleware(request):

        if re.match(r'^/usercenter/.*', request.path):
            if not request.user.is_authenticated:
                return redirect('/login/')

        response = get_response(request)
        return response

    return middleware