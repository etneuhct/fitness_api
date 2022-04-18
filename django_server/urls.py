from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from body.views import BodyShapeViewSet
from sport.views import BikingViewSet, BikingStatView, DumbbellViewSet, AbdoViewSet

router = DefaultRouter()
router.register(r'biking', BikingViewSet, basename='biking')
router.register(r'body-shape', BodyShapeViewSet, basename='body-shape')
router.register('dumbbell', DumbbellViewSet, basename='dumbbell')
router.register('abdo', AbdoViewSet, basename='abdo')

urlpatterns = [
    url(r"biking-stats", BikingStatView.as_view(), name='biking-stats'),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
