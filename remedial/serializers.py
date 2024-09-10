from rest_framework import serializers

from .models import Remedial


class RemedialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remedial
        fields = '__all__'
