# Generated by Django 2.0.6 on 2018-06-12 04:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]