# Generated by Django 4.1.1 on 2022-09-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='review',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='watched',
            field=models.TextField(),
        ),
    ]