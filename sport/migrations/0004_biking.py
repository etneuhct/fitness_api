# Generated by Django 4.0 on 2021-12-11 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0003_delete_biking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('resistance', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
