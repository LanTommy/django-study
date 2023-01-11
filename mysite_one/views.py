from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def home_view(request):
    html = '<h1>这是我的首页</h1>'
    return HttpResponse(html)


def page_1_view(request):
    html = '<h1>这是第一个页面</h1>'
    return HttpResponse(html)


def page_2_view(request):
    html = '<h1>这是第二个页面</h1>'
    return HttpResponse(html)


def page_n_view(request, pg):
    html = '<h1>这是第%s个页面</h1>' % (pg)
    return HttpResponse(html)


def page_calc_view(request, int1, str, int2):
    if str not in ['add', 'sub', 'mul']:
        return HttpResponse('您输入的操作符不在str中')

    html = ''
    if str == 'add':
        res = int1 + int2
        # html = '以上page计算出的结果是：%s + %s=%s' % (int1, int2, res)
        html = '<a href="https://www.baidu.com">以上page计算出的结果是：%s + %s=%s</a>' % (int1, int2, res)
        return HttpResponse(html)
    elif str == 'sub':
        res = int1 - int2
        html = '以上page计算出的结果是：%s - %s=%s' % (int1, int2, res)
        return HttpResponse(html)
    elif str == 'mul':
        res = int1 * int2
        html = '以上page计算出的结果是：%s x %s=%s' % (int1, int2, res)
    return HttpResponse(html)


def page_calc2_view(request, x, s, y):
    if s not in ['add', 'sub', 'mul']:
        return HttpResponse('您输入的操作符不在str中')

    html = ''
    if s == 'add':
        res = int(x) + int(y)
        # html = '以上page计算出的结果是：%s + %s=%s' % (int1, int2, res)
        html = '<a href="https://www.baidu.com">以上page计算出的结果是两位数：%s + %s=%s</a>' % (x, y, res)
        return HttpResponse(html)
    elif s == 'sub':
        res = int(x) - int(y)
        html = '以上page计算出的结果是两位数：%s - %s=%s' % (x, y, res)
        return HttpResponse(html)
    elif s == 'mul':
        res = int(x) * int(y)
        html = '以上page计算出的结果是两位数：%s x %s=%s' % (x, y, res)
    return HttpResponse(html)


def birthday_view(request, y, m, d):
    html = '当前生日是：%s年%s月%s日' % (y, m, d)
    return HttpResponse(html)


def test_request(request):
    print(request.path_info)
    print(request.method)
    print(request.GET)
    print(request.get_full_path())
    # return HttpResponse('test is ok')
    return HttpResponseRedirect('page/1')


POST_FORM = '''
<form method='post' action='/test_get_post'>
    用户名：<input type='text' name='uname'>
    <input type='submit' value='提交'>
</form>
'''


def test_get_post(request):
    if request.method == 'GET':
        print(request.GET)
        # print(request.GET['a'])
        print(request.GET.getlist('a'))
        print(request.GET.get('c', 'no c'))
        return HttpResponse(POST_FORM)
    elif request.method == 'POST':
        # 处理用户数据
        print('uname is ', request.POST['uname'])
        return HttpResponse('post is ok')
    else:
        pass
    return HttpResponse('test get post is ok')


def calc(request):
    res = '不存在此操作符'
    if request.method == 'GET':
        if request.GET.get('s', 'no s') == 'add':
            res = int(request.GET['x']) + int(request.GET['y'])
        elif request.GET.get('s', 'no s') == 'sub':
            res = int(request.GET['x']) - int(request.GET['y'])
        elif request.GET.get('s', 'no s') == 'mul':
            res = int(request.GET['x']) * int(request.GET['y'])
    elif request.method == 'POST':
        # 处理用户数据
        pass
    else:
        pass
    return HttpResponse('计算器的结果是：%s' % (res))


def test_html(request):
    from django.shortcuts import render
    dic = {'username': 'LanXinYue', 'password': 123456}
    dic['x'] = 11
    dic['list'] = ['tom','sqq','owo']
    dic['scrit'] = '<script>alert(111)</script>'
    return render(request, 'test_html.html', dic)


def calc_vies(request):
    from django.shortcuts import render
    if request.method == 'GET':
        return render(request, 'calc_html.html')
    elif request.method == 'POST':
        # 计算
        x = request.POST['x']
        y = request.POST['y']
        op = request.POST['op']
        res = 0
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if op == 'add':
                res = x + y
            elif op == 'sub':
                res = x - y
            elif op == 'mul':
                res = x * y
            elif op == 'div':
                res = x / y
        elif x.isspace() or y.isspace():
            res = -1
            print('no space')
        elif len(x) == 0 or len(y) == 0:
            res = -2
            print('no null')
        else:
            print('no num')
        # dic = {}
        # dic['x'] = x
        # dic['y'] = y
        # dic['op'] = op
        return render(request, 'calc_html.html', locals())  # locals()可以将局部变量全部封装到字典里面，省得自己去写字典


def base_view(request):
    lis = ['wo']
    return render(request,'base.html', locals())

def music_view(request,int):
    return render(request,'music.html')

def movie_view(request):
    # 302跳转
    url = reverse('bs')
    return HttpResponseRedirect(url)
    # return render(request,'movie.html')


'---------------------------------------------------------------------------------------------------------------------'
def test_static(request):
    return render(request, 'test_static.html')