# Generated by Django 2.2.7 on 2019-12-19 09:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20191130_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 9, 54, 55, 154804, tzinfo=utc), verbose_name='Срок действия безлимитного кода'),
        ),
    ]
