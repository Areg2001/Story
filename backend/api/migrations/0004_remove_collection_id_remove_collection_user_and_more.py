# Generated by Django 4.2.3 on 2023-08-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='id',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='user',
        ),
        migrations.RemoveField(
            model_name='story',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='story',
            name='id',
        ),
        migrations.AddField(
            model_name='collection',
            name='col_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]