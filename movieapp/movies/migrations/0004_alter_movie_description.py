# Generated by Django 3.2.9 on 2022-02-02 11:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20220202_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]