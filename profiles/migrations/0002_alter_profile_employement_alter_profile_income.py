# Generated by Django 4.1.7 on 2023-04-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='employement',
            field=models.CharField(choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Enterpreneur', 'Enterpreneur')], default='True', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='income',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
