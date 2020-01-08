# Generated by Django 2.1.5 on 2019-12-19 16:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20191219_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='discount',
        ),
        migrations.AddField(
            model_name='itemprice',
            name='discount',
            field=models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Скидка %'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 16, 59, 39, 709692, tzinfo=utc), verbose_name='Срок действия безлимитного кода'),
        ),
    ]