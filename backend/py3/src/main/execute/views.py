from django.shortcuts import render
from rest_framework import status
from .models import Testcases,Selected
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import *
from django.views.decorators.csrf import csrf_exempt

import json
import os
import subprocess
import time

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
@csrf_exempt


def testcases_list(request):
        if (request.method == 'POST'):
            time.sleep(3)
            #print(request.session['mie'])
            
            
            print(request.data[0])
            print(request.data[0]['testid'])
            i=0
            testscriptjava=[]   
            testscriptpy=[]
            
            #test for java or python cases
             
            
            while i < len(request.data):
                word=str(request.data[i]['testscript'])
                if (word.find('attrqa') != -1): 
                    print ("Contains given substring ")
                    testscriptjava.append(request.data[i]['testscript']) #append to java testcases
                else:
                    testscriptpy.append(request.data[i]['testscript']) #appends to python testcases
                i=i+1
            print(testscriptjava)
            i=0
            if testscriptjava: #execute java cases
                with cd("/home/noel/testmate1/attr-qa-api-ui-auto"):
                    j=0
                                    
                    
                    #subprocess.call(['git', 'clone',giturl])
                    file1 = open("./testjava.xml","w")
                    startingheaders =['<?xml version="1.0" encoding="UTF-8"?> \n','<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">\n',
                    '<suite name="SuiteName"> \n','<test  name="ValidToken"> \n','<classes>']
                    endingfooter=['</classes> \n','</test> \n','</suite> \n']     
                    file1.writelines(startingheaders)
                    while j < len(testscriptjava):
                        file1.write('<class name="'+testscriptjava[j] +'"/>')
                        file1.write("\n")
                        j=j+1 
                    file1.writelines(endingfooter)
                    file1.close()
                    subprocess.call(['mvn' ,'clean', 'test' ,'-Dsurefire.suiteXmlFiles=testjava.xml', '-DlogToMongo=y'])
                    cmd = "ls -tr /home/noel/testmate1/attr-qa-api-ui-auto/reports | tail -1"
                    ps=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)    
                    output = ps.communicate()[0]
                    htmlloc = str(output)[2:-3]
                    fileloc = "/home/noel/testmate1/attr-qa-api-ui-auto/reports/" + htmlloc
                    with open(fileloc) as f:
                        with open("/home/noel/ang/tez/backend/py3/src/main/execute/templates/execute/index.html", "w") as f1:
                            for line in f:
                                f1.write(line)
                    return render(request,'execute/index.html')
                    
            if testscriptpy:
                print("execute py cases")                    
                
                
                ###
            while i < len(request.data):
                    serializer = SelectedSerializer(data=request.data[i])
                    if serializer.is_valid():
                        serializer.save()
                        i=i+1
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else :
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
            
                                   
        elif request.method == 'GET':
                cmd = "ls -tr /home/noel/testmate1/attr-qa-api-ui-auto/reports | tail -1"
                ps=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)    
                output = ps.communicate()[0]
                htmlloc = str(output)[2:-3]
                fileloc = "/home/noel/testmate1/attr-qa-api-ui-auto/reports/" + htmlloc
                with open(fileloc) as f:
                    with open("/home/noel/ang/tez/backend/py3/src/main/execute/templates/execute/index.html", "w") as f1:
                        for line in f:
                            f1.write(line)
                return render(request,'execute/index.html')
            
@csrf_exempt
@api_view(['POST','GET'])
def users(request):
    if (request.method == 'POST'):
        request.session['mie']=(request.data['mie'])
        
        print(request.session['mie'])
        user=request.data['username']
        password=request.data['password']

        with cd("/home/noel/testmate1/attr-qa-api-ui-auto"):
            
            
            giturl= "https://"+user+":"+password+"@github.com"+"/nielsen-analytics/attr-qa-api-ui-auto"
            subprocess.call(['git','reset','--hard'])
            subprocess.call(['git' , 'pull',giturl])
            
            file1 = open("./testjava.xml","w")
            startingheaders =['<?xml version="1.0" encoding="UTF-8"?> \n','<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">\n',
                    '<suite name="SuiteName"> \n','<test  name="ValidToken"> \n']
            file1.writelines(startingheaders)
            if(str(request.data['mie'])!="none"):
                mie_token=str(request.data['mie'])
                token_headers='<parameter name="authToken" value="' + mie_token + '"></parameter>'
                class_headers='<classes> \n <class name="attrqa.tests.authtoken.AuthorizationToken_MIE" /> \n'
                file1.write(token_headers)
                file1.write(class_headers)
            if(str(request.data['token'])!="none"):
                    token=str(request.data['token'])
                    token_headers='<parameter name="authToken" value="' +token+ '"></parameter> \n'
                    class_headers='<classes> \n <class name="attrqa.tests.authtoken.AuthorizationToken" /> \n'
                    file1.write(token_headers)
                    file1.write(class_headers)

        
        return Response(request.data, status=status.HTTP_200_OK)
    
