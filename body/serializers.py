from rest_framework import serializers

from body.models import BodyShape


class BodyShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyShape
        fields = (
            'id', "date", "bmi", "weight", "body_fat", "muscle_mass", "visceral_fat", "body_water", "bone_mass", "bmr",
            "protein_rate", "skeletal_muscle_rate", "subcutaneous_fat", "lean_body_mass")

