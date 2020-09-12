# Generated by Django 3.1 on 2020-09-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='movieNm',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='nationAlt',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='openDt',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='repGenreNm',
        ),
        migrations.AddField(
            model_name='hotel',
            name='director',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='hotel',
            name='image',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='hotel',
            name='link',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='hotel',
            name='pubDate',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='hotel',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='hotel',
            name='userRating',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]