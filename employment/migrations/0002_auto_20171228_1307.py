# Generated by Django 2.0 on 2017-12-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='ended',
            field=models.DateField(null=True),
        ),
    ]
