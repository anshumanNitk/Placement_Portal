# Generated by Django 4.1.2 on 2023-04-28 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_inc_alter_job_branch_alter_job_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inc',
            name='id',
        ),
        migrations.AlterField(
            model_name='inc',
            name='val',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
