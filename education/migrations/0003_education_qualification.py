# Generated by Django 2.0 on 2017-12-28 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_education_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='qualification',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]