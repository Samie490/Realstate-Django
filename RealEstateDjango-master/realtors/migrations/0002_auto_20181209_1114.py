# Generated by Django 2.1.4 on 2018-12-09 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Realtors',
            new_name='Realtor',
        ),
    ]