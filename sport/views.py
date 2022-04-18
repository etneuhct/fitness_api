from django.db.models import Count
from django.db.models.functions import TruncHour, TruncDate, TruncDay, TruncYear
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from sport.models import Biking, Dumbbell, Abdo
from sport.serializers import BikingSerializer, DumbbellSerializer, AbdoSerializer


class BikingViewSet(viewsets.ModelViewSet):
    serializer_class = BikingSerializer
    permission_classes = [AllowAny]
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Biking.objects.all()


class BikingStatView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        data = Biking.objects.all()\
            .annotate(value=TruncDate("date"))\
            .values('value')\
            .annotate(count=Count('id')).values('value', 'count')
        return Response(data=data)


class DumbbellViewSet(viewsets.ModelViewSet):
    serializer_class = DumbbellSerializer
    permission_classes = [AllowAny]
    http_method_names = ('get', 'post', 'patch', 'delete')
    queryset = Dumbbell.objects.all()

    @action(detail=False, methods=['post'])
    def bulk(self, request):
        serializer = DumbbellSerializer(data=self.request.data, many=True)
        serializer.is_valid(raise_exception=True)
        exercises = serializer.data
        Dumbbell.objects.bulk_create(
            [Dumbbell(date=exercise['date']) for exercise in exercises]
        )
        return Response()


class AbdoViewSet(viewsets.ModelViewSet):
    serializer_class = AbdoSerializer
    permission_classes = [AllowAny]
    http_method_names = ('get', 'post', 'patch', 'delete')
    queryset = Abdo.objects.all()

    @action(detail=False, methods=['post'])
    def bulk(self, request):
        serializer = AbdoSerializer(data=self.request.data, many=True)
        serializer.is_valid(raise_exception=True)
        exercises = serializer.data
        Abdo.objects.bulk_create(
            [Abdo(date=exercise['date']) for exercise in exercises]
        )
        return Response()
