# Generated by Django 4.2.1 on 2023-06-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_date_activity_end_date_activity_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.CharField(default='MOOC', max_length=100),
            preserve_default=False,
        ),
    ]
