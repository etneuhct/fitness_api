from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from body.models import BodyShape
from body.serializers import BodyShapeSerializer


class BodyShapeViewSet(ModelViewSet):
    serializer_class = BodyShapeSerializer
    queryset = BodyShape.objects.all().order_by('date')
    permission_classes = (AllowAny, )
