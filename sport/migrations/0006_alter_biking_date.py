# Generated by Django 4.0 on 2021-12-18 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0005_alter_biking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biking',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
