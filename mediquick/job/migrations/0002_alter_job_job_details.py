# Generated by Django 5.0.4 on 2024-05-12 14:40

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_details',
            field=tinymce.models.HTMLField(),
        ),
    ]