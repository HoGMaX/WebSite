# Generated by Django 3.1 on 2020-08-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_agreement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='agreement',
            field=models.BooleanField(default=True),
        ),
    ]