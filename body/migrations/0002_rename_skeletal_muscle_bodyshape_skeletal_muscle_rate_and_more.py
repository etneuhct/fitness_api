# Generated by Django 4.0 on 2021-12-12 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bodyshape',
            old_name='skeletal_muscle',
            new_name='skeletal_muscle_rate',
        ),
        migrations.AddField(
            model_name='bodyshape',
            name='bmi',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
