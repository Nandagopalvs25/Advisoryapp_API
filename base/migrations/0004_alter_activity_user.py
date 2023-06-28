# Generated by Django 4.2.1 on 2023-06-28 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_activity_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to=settings.AUTH_USER_MODEL),
        ),
    ]
