# Generated by Django 4.1.2 on 2023-04-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_delete_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('branch', models.CharField(default=None, max_length=50)),
                ('resume', models.FileField(default=None, max_length=250, upload_to='dashboard/')),
                ('compname', models.CharField(default=None, max_length=50)),
                ('roles', models.CharField(default=None, max_length=50)),
                ('salary', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]