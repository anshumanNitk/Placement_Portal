# Generated by Django 4.1.2 on 2023-04-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_remove_inc_id_alter_inc_val'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inc',
            name='val',
            field=models.CharField(default=0, max_length=100, primary_key=True, serialize=False),
        ),
    ]
