# Generated by Django 3.1.6 on 2021-02-20 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210202_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=40, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='last_name'),
        ),
    ]
