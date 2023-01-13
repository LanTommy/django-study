from django.http import HttpResponse
from django.shortcuts import render


def set_cookies(request):
    resp = HttpResponse('set cookies is ok')
    resp.set_cookie('uname', 'lan', 500)
    return resp


def get_cookies(request):
    value = request.COOKIES.get('uname','uname is null')
    return HttpResponse(f'value is {value}')


def del_cookies(request):
    resp = HttpResponse('del is ok')
    resp.delete_cookie('uname')
    return resp


def set_session(request):
    request.session['uname'] = 'lxy'
    return HttpResponse('set session is ok')


def get_session(request):
    value = request.session['uname']
    return HttpResponse(f'session value is {value}')
