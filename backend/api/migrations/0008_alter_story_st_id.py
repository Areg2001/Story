# Generated by Django 4.2.3 on 2023-08-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_collection_user_id_alter_story_col_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='st_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]