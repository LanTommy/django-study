# Generated by Django 2.2.9 on 2023-01-05 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_author'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]