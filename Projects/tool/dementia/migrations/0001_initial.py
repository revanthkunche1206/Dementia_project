# Generated by Django 5.0.3 on 2024-11-15 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('tests', models.CharField(max_length=255)),
                ('additional_tests', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
