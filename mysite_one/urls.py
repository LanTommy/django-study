"""mysite_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/
    path('', views.home_view),
    # http://127.0.0.1:8000/page/1
    path('page/1', views.page_1_view),
    # http://127.0.0.1:8000/page/2
    path('page/2', views.page_2_view),
    # http://127.0.0.1:8000/page/3-n
    path('page/<int:pg>', views.page_n_view),
    # http://127.0.0.1:8000/page/整数2/[add/sub/mul]/整数2
    re_path(r'^page/(?P<x>\d{1,2})/(?P<s>\w+)/(?P<y>\d{1,2})$', views.page_calc2_view),
    # http://127.0.0.1:8000/page/整数/[add/sub/mul]/整数
    path('page/<int:int1>/<str:str>/<int:int2>', views.page_calc_view),
    # http://127.0.0.1:8000/birthday/年/月/日
    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$',views.birthday_view),
    # http://127.0.0.1:8000/birthday/月/日/年
    re_path(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})$',views.birthday_view),
    # http://127.0.0.1:8000/test_request
    path('test_request',views.test_request),
    path('test_get_post',views.test_get_post),
    # http://127.0.0.1:8000/calc
    path('calc',views.calc),
    # http://127.0.0.1:8000/test_html
    path('test_html',views.test_html),
    # http://127.0.0.1:8000/calc_html
    path('calc_html',views.calc_vies),

    path('base',views.base_view, name='bs'),
    path('music/<int:int>',views.music_view, name='mp3'),
    path('movie',views.movie_view),

    path('test_static',views.test_static),
    #分布式路由
    path('music/',include('music.urls')),
    path('news/',include('news.urls')),
    path('sport/',include('sport.urls')),
    # 查看所有书籍
    path('bookstore/',include('bookstore.urls')),
]
