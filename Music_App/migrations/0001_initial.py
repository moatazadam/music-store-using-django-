# Generated by Django 4.0.6 on 2023-08-11 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Rap', 'Rap'), ('Pop', 'Pop'), ('Jazz', 'Jazz'), ('Hip-Hop', 'Hip-Hop')], max_length=50)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music_App.artist')),
            ],
        ),
    ]