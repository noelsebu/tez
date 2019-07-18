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
flag=[0]
#sets iterators to zero
i = 0
j=0


p=[] #this list will contain the table headers required to be displayed on the web app
q=[] #this list will contain the path of the table headers in the response of jira api  from which the attribute can be derived



result=[]
with open('./key_config.json') as json_file: #reads the config file of  the jira api
    data = json.load(json_file)
    while i< len(response['issues']):
        
        jira={}
            
        while j < (len(data)):
            
            p.append(str(data[str(j)].keys())[3:-2]) #retrives table header
            q=((data[str(j)].values())[0]) #retrives the path of table header
            
        ##########################################################################################################################    
        #checks for none type
        def flagmaker(len, testlist=[]):    
	    if (len>=0 and testlist is None):
                flag.append(1)
            elif (len>=1 and testlist is None ):
                flag.append(1)
            elif (len>=2 and testlist is None ):
                flagmaker(len-1,testlist)    
                '''
            elif (len>=2 and testlist is None ):
                flag.append(1)
            elif (len>=3 and testlist is None ):
                flag.append(1)
            elif (len>=4 and testlist is None ):
                flag.append(1)
            elif (len>=5 and testlist is None ):
                flag.append(1)
            elif (len>=6 and testlist is None ):
                flag.append(1)
            elif (len>=7 and testlist is None ):
                flag.append(1)
            elif (len>=8 and testlist is None):
                flag.append(1)
            elif (len>=9 and testlist is None ):
                flag.append(1)
            '''
            
            #####################################################################################################################################################3
	    #response is parsesd through and takes only the required attributes	
            if(len(q)==1):
                flagmaker(len(q),response[q[0]])
                if(sum(flag)==0):    
                    jira[p[j]]=response[q[0]]
                

            
            elif(len(q)==2):
                flagmaker(len(q),response[q[0]][i][q[1]])
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]]
                
            
            
            elif(len(q)==3):
                flagmaker(len(q),response[q[0]][i][q[1]][q[2]])
                if(sum(flag)==0) :
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]]
                
            
            
            elif(len(q)==4):
                flagmaker(len(q),response[q[0]][i][q[1]][q[2]][q[3]])
                if(sum(flag)==0):
                    jira[p[j]]=[q[0]][i][q[1]][q[2]][q[3]]
                
            
            
            
            elif(len(q)==5):
                flagmaker(len(q),response[q[0]][i][q[1]][q[2]][q[3]][q[4]])
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]]
                
            
            
            
            elif(len(q)==6):
                flagmaker(len(q),response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]])
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]]     
                

            elif(len(q)==7):
                flagmaker(len(q),response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]])
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]]     
                


            elif(len(q)==8):
                flagmaker(len(q),response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]][q[7]])
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]][q[7]]     
                                
            
            
            elif(len(q)==9):
                flagmaker(len(q),response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]][q[7]][q[8]])
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]][q[7]][q[8]]     
                            
            elif(len(q)==10):
                flagmaker(len(q),response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]][q[7]][q[8]][q[9]])
                if(sum(flag)==0):
                    jira[p[j]]=response[q[0]][i][q[1]][q[2]][q[3]][q[4]][q[5]][q[6]][q[7]][q[8]][q[9]]     
               
            ########################################################################################################################################
            j=j+1
      
        j=0
        i=i+1
        result.append(jira) #all details are retrived for a single object and is appended to the result.to acces the next object it is itterated in the i while loop
print(result) 
output_file=open('./retrivejira.json', 'w')
back_json=json.dumps(result, output_file)
output_file.write(back_json)   #result is dumped to a file
json_file.close()