# Generated by Django 4.2 on 2024-02-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('multitenancy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
