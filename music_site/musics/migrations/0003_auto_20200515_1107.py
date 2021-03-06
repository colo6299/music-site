# Generated by Django 3.0.6 on 2020-05-15 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0002_album_release_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
