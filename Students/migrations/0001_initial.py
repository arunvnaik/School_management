# Generated by Django 5.0.7 on 2024-07-26 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
