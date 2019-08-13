from django.shortcuts import render
from rest_framework import status
from .models import Credentials
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
      login = Credentials.objects.all()
      serializer = CredentialsSerializer(login,context={'request': request} ,many=True)
      return Response(serializer.data)
    elif request.method == 'POST':
        print("hi")
        print(request.data)
        while i < len(request.data):
            serializer = CredentialsSerializer(data=request.data[i])
            if serializer.is_valid():
                serializer.save()
                i=i+1
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else :
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)