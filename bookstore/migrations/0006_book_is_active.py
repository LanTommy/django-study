# Generated by Django 2.2.9 on 2023-01-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_auto_20230105_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否活跃，0：不活跃；1：活跃'),
        ),
    ]
