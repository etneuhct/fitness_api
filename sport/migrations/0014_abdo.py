# Generated by Django 3.2.8 on 2022-03-11 21:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0013_alter_dumbbell_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abdo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
