# Generated by Django 5.0.3 on 2024-03-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteit', '0010_alter_note_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(blank=True, to='noteit.tag'),
        ),
    ]
