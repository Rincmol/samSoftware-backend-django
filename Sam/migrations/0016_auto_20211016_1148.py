# Generated by Django 3.2.7 on 2021-10-16 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sam', '0015_alter_customer_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employee',
            table='sam_employee',
        ),
        migrations.AlterModelTable(
            name='group',
            table='sam_group',
        ),
        migrations.AlterModelTable(
            name='job',
            table='sam_job',
        ),
        migrations.AlterModelTable(
            name='ledger',
            table='sam_ledger',
        ),
        migrations.AlterModelTable(
            name='supplier',
            table='sam_supplier',
        ),
    ]
