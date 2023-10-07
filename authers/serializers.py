from rest_framework import serializers
from authers.models import Auther

class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auther
        fields = ('full_name', 'email', 'birth_date')