# Generated by Django 3.0.2 on 2020-01-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200128_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
