# Generated by Django 5.0.3 on 2024-11-15 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dementia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorinfo',
            old_name='tests',
            new_name='test',
        ),
    ]
