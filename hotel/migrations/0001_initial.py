# Generated by Django 3.1 on 2020-09-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movieNm', models.CharField(default='', max_length=100)),
                ('openDt', models.CharField(default='', max_length=100)),
                ('nationAlt', models.CharField(default='', max_length=30)),
                ('repGenreNm', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
