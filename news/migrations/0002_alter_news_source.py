# Generated by Django 4.1.7 on 2023-03-21 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
