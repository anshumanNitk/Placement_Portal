# Generated by Django 4.1.2 on 2023-05-01 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0017_alter_job_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydata',
            name='poc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]