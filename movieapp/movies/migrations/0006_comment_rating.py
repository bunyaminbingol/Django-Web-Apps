# Generated by Django 3.2.9 on 2022-02-02 11:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20220202_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(5)]),
            preserve_default=False,
        ),
    ]
