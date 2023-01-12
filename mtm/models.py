from django.db import models

# Create your models here.
class Coder(models.Model):
    # 代码人员 一
    name = models.CharField('姓名',max_length=50)
    # 反向属性规则，一对象.多对象_set.all()

class Code(models.Model):
    # 代码 多
    title = models.CharField('代码名称',max_length=50)
    coders = models.ManyToManyField(Coder)