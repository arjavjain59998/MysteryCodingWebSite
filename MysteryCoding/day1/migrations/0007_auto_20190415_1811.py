# Generated by Django 2.2 on 2019-04-15 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day1', '0006_remove_day11_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day11',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
