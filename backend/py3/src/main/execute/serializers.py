from .models import Testcases,Selected
from rest_framework import serializers

class TestcasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Testcases
        fields=('selected')
        

class SelectedSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Selected
        fields = ('team_name','testid','automatable_reason','testscript')

    