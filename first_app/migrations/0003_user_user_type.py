# Generated by Django 2.2.4 on 2022-10-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20221004_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(default='user', max_length=10),
        ),
    ]
