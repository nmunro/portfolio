# Generated by Django 2.0 on 2018-01-01 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0005_auto_20171229_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='current',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
