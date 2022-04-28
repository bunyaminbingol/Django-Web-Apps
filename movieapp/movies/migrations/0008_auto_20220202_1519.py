# Generated by Django 3.2.9 on 2022-02-02 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20220202_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_added',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='video',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
    ]
