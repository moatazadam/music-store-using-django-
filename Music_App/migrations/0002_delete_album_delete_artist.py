# Generated by Django 4.0.6 on 2023-08-11 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music_App', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]
