# Generated by Django 3.2 on 2021-04-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210421_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Заголовок поста'),
        ),
    ]
