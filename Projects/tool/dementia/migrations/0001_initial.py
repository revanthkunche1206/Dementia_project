# Generated by Django 5.0.3 on 2024-11-20 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmstAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('time', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('recognize_people', models.CharField(max_length=255)),
                ('dob', models.CharField(max_length=20)),
                ('sunrise', models.CharField(max_length=20)),
                ('ww1', models.IntegerField()),
                ('count_backwards', models.CharField(max_length=255)),
                ('repeat_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_dob', models.DateField()),
                ('patient_age', models.IntegerField()),
                ('date', models.DateField()),
                ('mobile_num', models.CharField(max_length=15)),
                ('town_city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('test', models.CharField(max_length=255)),
                ('additional_tests', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MmseAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('season', models.CharField(max_length=20)),
                ('day', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('state', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=100)),
                ('floor', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=100)),
                ('backward', models.CharField(max_length=100)),
                ('recall', models.CharField(max_length=100)),
                ('objects_outside', models.CharField(max_length=100)),
                ('phrase', models.CharField(max_length=255)),
            ],
        ),
    ]
