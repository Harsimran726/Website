# Generated by Django 5.0.1 on 2024-03-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
