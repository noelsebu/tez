from django.shortcuts import render
from rest_framework import status
from .models import Testcases,Selected
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
import json
import os
import subprocess

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)



# Create your views here.
@api_view(['GET', 'POST'])
def testcases_list(request):
    """
    List all testcases, or create a new testcase.
    """
    if request.method == 'GET':
      testcases = Selected.objects.all()
      serializer = SelectedSerializer(testcases,context={'request': request} ,many=True)
      return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data[0])
        print(request.data[0]['testid'])
        i=0
        testscript=[]
        while i < len(request.data):
            testscript.append(request.data[i]['testscript'])
            i=i+1
        print(testscript)
        i=0

        with cd("/home/noel/testmate1/attr-qa-api-ui-auto"):
            j=0
            user="surajvbhattathiri"
            
            password="df2f61908446e0e7f3d2520143ff4954e8cec648"
            
            giturl= "https://"+user+":"+password+"@github.com"+"/nielsen-analytics/attr-qa-api-ui-auto"
            
            subprocess.call(['git' , 'pull',giturl])
            #subprocess.call(['git', 'clone',giturl])
            file1 = open("./testjava.xml","w")
            startingheaders =['<?xml version="1.0" encoding="UTF-8"?> \n','<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">\n',
            '<suite name="SuiteName"> \n','<test  name="ValidToken"> \n','<classes>']
            endingfooter=['</classes> \n','</test> \n','</suite> \n']     
            file1.writelines(startingheaders)
            while j < len(testscript):
                file1.write('<class name="'+testscript[j] +'"/>')
                file1.write("\n")
                j=j+1 
            file1.writelines(endingfooter)
            file1.close()
            subprocess.call(['mvn' ,'clean', 'test' ,'-Dsurefire.suiteXmlFiles=testjava.xml', '-DlogToMongo=y']) 

        
        
        ###
        while i < len(request.data):
            serializer = SelectedSerializer(data=request.data[i])
            if serializer.is_valid():
                serializer.save()
                i=i+1
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else :
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)           
            


