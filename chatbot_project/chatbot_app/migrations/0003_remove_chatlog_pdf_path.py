# Generated by Django 5.0.3 on 2024-03-07 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_app', '0002_alter_chatsession_session_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatlog',
            name='pdf_path',
        ),
    ]
