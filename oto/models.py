from django.db import models

# Create your models here.
class Author(models.Model):
    # wife 反向属性
    name = models.CharField('姓名',max_length=11)

class Wife(models.Model):

    name = models.CharField('姓名',max_length=11)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)