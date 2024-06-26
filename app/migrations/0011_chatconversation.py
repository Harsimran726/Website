# Generated by Django 5.0.1 on 2024-03-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_query_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatConversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_message', models.CharField(max_length=10000, null=True)),
                ('user_message', models.CharField(max_length=10000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
