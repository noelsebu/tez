from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import os
import subprocess

def index(request):
    cmd = "ls -tr /home/noel/testmate1/attr-qa-api-ui-auto/reports | tail -1"
    ps=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)    
    output = ps.communicate()[0]
    htmlloc = str(output)[2:-3]
    fileloc = "/home/noel/testmate1/attr-qa-api-ui-auto/reports/" + htmlloc
    with open(fileloc) as f:
        with open("/home/noel/ang/tez/backend/py3/src/main/reports/templates/reports/index.html", "w") as f1:
            for line in f:
                f1.write(line)
    return render(request,'reports/index.html')