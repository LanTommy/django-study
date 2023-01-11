from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *


# Create your views here.

def all_book(request):
    # all_book = Book.objects.all()
    all_book = Book.objects.filter(is_active=True)
    return render(request, 'bookstore/bookstore.html', locals())


def update_book(request,book_id):
    try:
        this_book = Book.objects.get(id=book_id,is_active=True)
    except Exception as e:
        print('--update book is error\n%s' % (e))
        return HttpResponse('<h3>查无此数据</h3><a href="/bookstore/all_book">返回图书馆</a>')
    if request.method == 'GET':
        return render(request, 'bookstore/update.html', locals())
    elif request.method == 'POST':
        price = request.POST['price']
        market_price = request.POST['market_price']
        if price == '':
            this_book.price = 0
            this_book.market_price = market_price
            return HttpResponseRedirect('/bookstore/all_book')
        elif market_price == '':
            this_book.price = price
            this_book.market_price = 0
            this_book.save()
            return HttpResponseRedirect('/bookstore/all_book')
        elif price.isdigit() or market_price.isdigit():
            this_book.price = price
            this_book.market_price = market_price
            this_book.save()
            return HttpResponseRedirect('/bookstore/all_book')
        else:
            return HttpResponseRedirect(f'/bookstore/update_book/{book_id}')


def delete_book(request):
    book_id = request.GET.get('b_id')
    if not book_id:
        return HttpResponse('出错啦，请刷新页面重试')
    try:
        del_book = Book.objects.get(id=book_id,is_active=True)
    except Exception as e:
        print(e)
        return HttpResponse('严重错误')
    del_book.is_active = False
    del_book.save()
    return HttpResponseRedirect('/bookstore/all_book')