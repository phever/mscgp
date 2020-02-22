from django.shortcuts import render
from rest_framework import viewsets
from api.models import MagicSet, MagicCard
from api.serializers import MagicCardSerializer, MagicSetSerializer


class MagicSetViewSet(viewsets.ModelViewSet):
    queryset = MagicSet.objects.all()
    serializer_class = MagicSetSerializer


class MagicCardViewSet(viewsets.ModelViewSet):
    queryset = MagicCard.objects.all()
    serializer_class = MagicCardSerializer
