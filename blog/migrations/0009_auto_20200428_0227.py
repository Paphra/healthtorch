# Generated by Django 3.0.5 on 2020-04-27 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200428_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='questioncomment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
