from rest_framework import serializers

from sport.models import Biking, Dumbbell, Abdo


class BikingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Biking
        fields = ['date']
        read_only_fields = ('date', )

    def to_representation(self, instance):
        return {'date': (instance.date.timestamp())}


class DumbbellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dumbbell
        fields = ('date',)


class AbdoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abdo
        fields = ('date',)


