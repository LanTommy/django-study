from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField('书名', max_length=50, default='', unique=True)
    pub = models.CharField('出版社', max_length=100, null=False, default='未知')
    price = models.DecimalField('价格', max_digits=7, decimal_places=2)
    market_price = models.DecimalField('零售价', max_digits=7, decimal_places=2, default=0.0)
    is_active = models.BooleanField('是否活跃，0：不活跃；1：活跃',default=True)

    class Meta:
        db_table = 'book'
        verbose_name = '图书表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s__%s__%s__%s__%s' % (self.title, self.pub, self.price, self.market_price,self.is_active)


class Author(models.Model):
    name = models.CharField('姓名', max_length=11, null=False, default='')
    age = models.IntegerField('年龄', default=1)
    email = models.EmailField('邮箱', null=True)

    class Meta:
        db_table = 'author'
        verbose_name = '作者表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s__%s__%s' % (self.name, self.age, self.email)
