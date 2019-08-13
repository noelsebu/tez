from .models import Credentials
from rest_framework import serializers

class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Credentials
        fields=('username','password')