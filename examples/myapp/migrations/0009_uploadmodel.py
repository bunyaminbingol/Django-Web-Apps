# Generated by Django 3.2.9 on 2022-01-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20211012_0356'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images')),
            ],
        ),
    ]
