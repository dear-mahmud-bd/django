# Generated by Django 5.0.1 on 2024-03-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_useraddress_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
