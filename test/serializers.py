from rest_framework import serializers
from test.models import Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('content', 'cat_id')
