import json
import requests



print("hello")
#Reads Details from password config
with open('./password.json') as json_file:
    dummy = json.load(json_file)
    user= str(dummy['username'])
    passwd=str(dummy['password'])
    url=str(dummy['url'])
json_file.close()
auth_values = (user, passwd)
response = requests.get(url, auth=auth_values)
#get response from the jira api
response=response.json()

result = [] #makes an empty list to retrive the relevant information


########################################################################################################################
#sets flag variables to 0 to  make sure  that  NONE type is not  returned

#sets iterators to zero
i = 0
j=0


p=[] #this list will contain the table headers required to be displayed on the web app
q=[] #this list will contain the path of the table headers in the response of jira api  from which the attribute can be derived



result=[]
with open('./key_config.json') as json_file: #reads the config file of  the jira api
    data = json.load(json_file)
    while i< 2:#len(response['issues']):
        
        jira={}
        flag=[0]
        print("in jira response")
        while j < (len(data)):
            for (k, v) in data.items():
                for item in v:
                    print(item)
                    p.append(item)
            #p.append((str(data[str(j)].keys()))[3:-2]) #retrives table header
            #print(p)
            
            #print((data[str(j)].values())[0])
            q=((list((data[str(j)].values())))[0]) #retrives the path of table header
            
        ##########################################################################################################################    
        #checks for none type    
            if (len(q)>=0 and response[q[0]] is None):
                flag.append(1)
            elif (len(q)>=1 and response[q[0]][i] is None ):
                flag.append(1)
            elif (len(q)>=2 and response[q[0]][i][q[1]] is None ):
                flag.append(1)
            elif (len(q)>=3 and response[q[0]][i][q[1]][q[2]] is None ):
                flag.append(1)
            elif (len(q)>=4 and response[q[0]][i][q[1]][q[2]][q[3]] is None ):
                flag.append(1)
            elif (len(q)>=5 and response[q[0]][i][q[1]][q[2]][q[3]][q[4]] is None ):
                flag.append(1)
            elif (len(q)>=6 and response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]] is None ):
                flag.append(1)
            elif (len(q)>=7 and response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]] is None ):
                flag.append(1)
            elif (len(q)>=8 and response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]][q[7]] is None):
                flag.append(1)
            elif (len(q)>=9 and response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]][q[7]][q[8]] is None ):
                flag.append(1)
            
            
            #####################################################################################################################################################3
	    #response is parsesd through and takes only the required attributes	
            if(len(q)==1):
                if(sum(flag)==0):    
                    jira[p[j]]=response[q[0]]
                else:
                    jira[p[j]]="None"

            
            elif(len(q)==2):
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]]
                else:
                    jira[p[j]]="None"
            
            
            elif(len(q)==3):
                if(sum(flag)==0) :
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]]
                else:
                    jira[p[j]]="None"
            
            
            elif(len(q)==4):
                if(sum(flag)==0):
                   jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]]
                else:
                    jira[p[j]]="None"
            
            
            
            elif(len(q)==5):
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]]
                else:
                    jira[p[j]]="None"
            
            
            
            elif(len(q)==6):
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]]     
                else:
                    jira[p[j]]="None"


            elif(len(q)==7):
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]]     
                else:
                    jira[p[j]]="None"



            elif(len(q)==8):
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]][q[7]]     
                else:
                    jira[p[j]]="None"                
            
            
            elif(len(q)==9):
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]][q[7]][q[8]]     
                else:
                    jira[p[j]]="None"
            
            elif(len(q)==10):
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]][q[7]][q[8]][q[9]]     
                else:
                    jira[p[j]]="None"
            ########################################################################################################################################
            j=j+1
            
            flag=[]
      
        j=0
        i=i+1
        result.append(jira) #all details are retrived for a single object and is appended to the result.to acces the next object it is itterated in the i while loop
print(result) 
output_file=open('./retrivejira.json', 'w')
back_json=json.dumps(result, output_file)
output_file.write(back_json)   #result is dumped to a file
json_file.close()

