# Generated by Django 3.1 on 2020-09-12 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20200912_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='director',
        ),
    ]
