import json
import requests
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



print("hello")
url="http://localhost:4200/api/test"

response = requests.get(url)
i=0
response=response.json()
#subprocess.call(["cd" ,"attrqa_java"])
with cd("./attrqa_java"):
    subprocess.call(['git' , 'pull'])
    file1 = open("./testjava.xml","w")
    startingheaders =['<?xml version="1.0" encoding="UTF-8"?> \n','<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">\n',
    '<suite name="SuiteName"> \n','<test  name="ValidToken"> \n','<classes>']
    endingfooter=['</classes> \n','</test> \n','</suite> \n']     
    file1.writelines(startingheaders)
    while i< len(response[0]):
        file1.write('<class name="'+response[0][i]['testscript'] +'"/>')
        file1.write("\n")
        i=i+1 
    file1.writelines(endingfooter)
    file1.close()
    subprocess.call(['mvn' ,'clean', 'test' ,'-Dsurefire.suiteXmlFiles=testjava.xml', '-DlogToMongo=y']) 
    
    



