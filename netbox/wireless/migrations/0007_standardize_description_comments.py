# Generated by Django 4.1.2 on 2022-11-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wireless', '0006_unique_constraints'),
    ]

    operations = [
        migrations.AddField(
            model_name='wirelesslan',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wirelesslink',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
