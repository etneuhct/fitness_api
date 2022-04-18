# Generated by Django 4.0 on 2021-12-12 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BodyShape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('weight', models.IntegerField()),
                ('body_fat', models.IntegerField()),
                ('muscle_mass', models.IntegerField()),
                ('visceral_fat', models.IntegerField()),
                ('body_water', models.IntegerField()),
                ('bone_mass', models.IntegerField()),
                ('bmr', models.IntegerField()),
                ('protein_rate', models.IntegerField()),
                ('skeletal_muscle', models.IntegerField()),
                ('subcutaneous_fat', models.IntegerField()),
                ('lean_body_mass', models.IntegerField()),
            ],
        ),
    ]