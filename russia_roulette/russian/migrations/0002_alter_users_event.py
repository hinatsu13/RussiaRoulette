# Generated by Django 4.2.16 on 2024-10-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('russian', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='event',
            field=models.ManyToManyField(null=True, to='russian.event'),
        ),
    ]
