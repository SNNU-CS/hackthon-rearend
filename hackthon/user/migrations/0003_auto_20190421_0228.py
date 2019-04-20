# Generated by Django 2.2 on 2019-04-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190421_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.TextField(choices=[('M', '男'), ('F', '女'), ('U', '未知')], default='M'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nick_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='open_id',
            field=models.TextField(),
        ),
    ]
