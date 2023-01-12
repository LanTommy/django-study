from django.db import models

# Create your models here.
class PubLisher(models.Model):
    # 出版社 一
    name = models.CharField('出版社名称',max_length=50)
    # 反向属性规则，一对象.多对象_set.all()

class Book(models.Model):
    # 书名 多
    title = models.CharField('书名',max_length=50)
    publisher = models.ForeignKey(PubLisher,on_delete=models.CASCADE)