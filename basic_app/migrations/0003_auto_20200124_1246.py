# Generated by Django 3.0.2 on 2020-01-24 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20200124_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='additional_driver_01_d_dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rental',
            name='additional_driver_01_d_lic_exp',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rental',
            name='additional_driver_02_d_dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rental',
            name='additional_driver_02_d_lic_exp',
            field=models.DateField(),
        ),
    ]