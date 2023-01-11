from django.contrib import admin
from .models import *


# Register your models here.

class BookManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['id', 'title', 'pub', 'price', 'market_price', 'is_active']
    # 控制list_display中的字段 哪些字段可以链接到修改页
    list_display_links = ['title']
    # 添加过滤器
    list_filter = ['title', 'pub']
    # 添加搜索框
    search_fields = ['title', 'pub']
    # 添加可以在列表页编辑的字段
    list_editable = ['price', 'market_price']


class AuthorManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['id', 'name', 'age']
    # 控制list_display中的字段 哪些字段可以链接到修改页
    list_display_links = ['name']
    # 添加过滤器
    list_filter = ['name', 'age']
    # 添加搜索框
    search_fields = ['name']
    # 添加可以在列表页编辑的字段
    list_editable = ['age']

admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
