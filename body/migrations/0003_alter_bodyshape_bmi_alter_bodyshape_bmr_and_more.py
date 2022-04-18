# Generated by Django 4.0 on 2021-12-12 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0002_rename_skeletal_muscle_bodyshape_skeletal_muscle_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyshape',
            name='bmi',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='bmr',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='body_fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='body_water',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='bone_mass',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='date',
            field=models.DateTimeField(unique=True),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='lean_body_mass',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='muscle_mass',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='protein_rate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='skeletal_muscle_rate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='subcutaneous_fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='visceral_fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bodyshape',
            name='weight',
            field=models.FloatField(),
        ),
    ]