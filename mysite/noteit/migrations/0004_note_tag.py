# Generated by Django 5.0.3 on 2024-03-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteit', '0003_remove_long_folder_remove_short_folder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
