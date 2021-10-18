# Generated by Django 3.2.7 on 2021-10-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sam', '0016_auto_20211016_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='contact_mobile',
            field=models.BigIntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cr_no',
            field=models.BigIntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='credit_lim_am',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='credit_lim_dur',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='expired_on',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='land_phone',
            field=models.BigIntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.BigIntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='open_balance',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='vat_reg_no',
            field=models.BigIntegerField(max_length=15),
        ),
    ]