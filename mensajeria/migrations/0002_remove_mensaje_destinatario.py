# Generated by Django 5.0.6 on 2024-07-05 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='destinatario',
        ),
    ]