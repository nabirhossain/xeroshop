# Generated by Django 2.0.8 on 2018-09-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180915_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]
