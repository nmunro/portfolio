# Generated by Django 2.0 on 2017-12-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proverbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proverb',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
