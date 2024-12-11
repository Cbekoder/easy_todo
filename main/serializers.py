from rest_framework import serializers
from .models import Reja

class RejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reja
        fields = '__all__'
