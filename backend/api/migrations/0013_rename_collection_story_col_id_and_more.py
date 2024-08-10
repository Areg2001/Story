# Generated by Django 4.2.3 on 2023-08-14 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0012_rename_user_collection_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='collection',
            new_name='col_id',
        ),
        migrations.AlterField(
            model_name='collection',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection', to=settings.AUTH_USER_MODEL),
        ),
    ]