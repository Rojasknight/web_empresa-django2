# Generated by Django 2.1.2 on 2018-11-27 01:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20181126_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='contenido',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
