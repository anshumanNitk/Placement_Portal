# Generated by Django 4.1.2 on 2023-04-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_inc_val'),
    ]

    operations = [
        migrations.AddField(
            model_name='inc',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='inc',
            name='val',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
