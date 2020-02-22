from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import MagicCard, MagicSet


class MagicCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MagicCard
        fields = ['name', 'set', 'cmc', 'collector_number']


class MagicSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MagicSet
        fields = ['name', 'set_code', 'type', 'block']
