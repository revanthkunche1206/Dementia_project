# Generated by Django 5.0.3 on 2024-11-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dementia', '0003_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='amst_Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('time', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('recognize_people', models.CharField(max_length=255)),
                ('dob', models.CharField(max_length=20)),
                ('ww1', models.IntegerField()),
                ('count_backwards', models.CharField(max_length=255)),
                ('repeat_address', models.CharField(max_length=255)),
            ],
        ),
    ]
