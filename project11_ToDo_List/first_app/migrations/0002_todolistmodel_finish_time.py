# Generated by Django 5.0.1 on 2024-03-16 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodel',
            name='finish_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
