# Generated by Django 4.1.2 on 2023-04-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=25)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
