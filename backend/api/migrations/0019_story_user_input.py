# Generated by Django 4.2.3 on 2023-08-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_story_generated_context'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='user_input',
            field=models.TextField(default=''),
        ),
    ]