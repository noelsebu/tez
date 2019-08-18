from django.shortcuts import render
from rest_framework import status
from .models import Credentials
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
import requests
import json
from django.http import JsonResponse

# Create your views here.
@api_view(['GET', 'POST'])
def jira_list(request):
    if request.method == 'GET':
        with open('./test2.json') as json_file:
            data = json.load(json_file)
            return JsonResponse(data,safe=False)
       # print(response)
        """
      login = Credentials.objects.all()
      serializer = CredentialsSerializer(login,context={'request': request} ,many=True)
      return Response(serializer.data)
      """
    elif request.method == 'POST':
        print("hi")
        print(request.data)
        #user="kare9001"
        #passwd="Technl98"
        user= str(request.data['username'])
        passwd=str(request.data['password'])
        print(user)
        url="https://adlm.nielsen.com/jira/rest/api/2/search?jql=filter=62111&maxResults=1000"
        auth_values = (user, passwd)
        response=requests.get(url, auth=auth_values)
        response=response.json()
        output_file=open('./test2.json', 'w')
        i=0

        result = []
        #print(response)
        

        
        while i< len(response['issues']): 
            my_dict={}  
            my_dict['testid']=response['issues'][i]['key']
            print (my_dict['testid'])
            my_dict['testscript']=response['issues'][i]['fields']['customfield_10113']
            print (my_dict['testscript'])
            my_dict['automatable_reason']=response['issues'][i]['fields']['customfield_19300']
            print (my_dict['automatable_reason'])
            if(str(response['issues'][i]['fields']['customfield_11500'])=="None"):
                    my_dict['team_name']=response['issues'][i]['fields']['customfield_11500']
            else:
                    my_dict['team_name']=response['issues'][i]['fields']['customfield_11500']['value']

            print (my_dict['team_name'])

            
            #my_dict['automatable']=response['issues'][i]['fields']['customfield_15600']
            #print (my_dict['automatable'])
            result.append(my_dict)
            i=i+1 
        print(type(result))
        back_json=json.dumps(result)
        print(type(back_json))

        output_file.write(back_json)

        output_file.close()
        return Response(status=status.HTTP_201_CREATED)
        
        
        
        
        
        
        
        
        """
        while i < len(request.data):
            serializer = CredentialsSerializer(data=request.data[i])
            if serializer.is_valid():
                serializer.save()
                i=i+1
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else :
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """