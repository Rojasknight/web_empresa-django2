# Generated by Django 2.1.2 on 2018-11-26 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20181126_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='Orden'),
        ),
    ]
