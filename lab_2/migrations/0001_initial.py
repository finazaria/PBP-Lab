# Generated by Django 3.2.7 on 2021-09-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=30)),
                ('From', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=250)),
            ],
        ),
    ]
