# Generated by Django 3.1 on 2020-08-23 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0004_remove_cource_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cource',
            name='name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Имя'),
            preserve_default=False,
        ),
    ]
