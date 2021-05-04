from django.shortcuts import render
from rest_framework import viewsets

from .serializers import DancerSerializer
from .models import Dancer


class DancerViewSet(viewsets.ModelViewSet):
    queryset = Dancer.objects.all().order_by('name')
    serializer_class = DancerSerializer