from rest_framework import serializers

from .models import Dancer

class DancerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dancer
        fields = ('name', 'forms')