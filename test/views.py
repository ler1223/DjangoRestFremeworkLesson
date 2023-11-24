from django.shortcuts import render
from  rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from test.models import Unit
from test.serializers import UnitSerializer


class UnitAPIView(generics.ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
