# Generated by Django 3.2.7 on 2021-09-22 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sam', '0010_alter_user_mobile_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mobile_no',
            new_name='mobile',
        ),
    ]
