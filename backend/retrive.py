import requests
import json

output_file=open('./test2.json', 'w')
#output_file=open('./test.json', 'w')
print("hello")
vari="maxResults"
#Reads Details from password config
with open('./password.json') as json_file:
    data = json.load(json_file)
    user= str(data['username'])
    passwd=str(data['password'])
    url=str(data['url'])
     


json_file.close()

# Sample Basic Auth Url with login values as username and password   
# Make a request to the endpoint using the correct auth values
auth_values = (user, passwd)
response = requests.get(url, auth=auth_values)
#get response from the jira api
response=response.json()

print(response[vari])
print(response['issues'][1]['key'])
i = 0

###########################################################################################

###################################################################################
'''
'''
    # Convert JSON to dict and print
#print(response.json())
result = []
while i< len(response['issues']): 
   my_dict={}  
   my_dict['testid']=response['issues'][i]['key']
   print (my_dict['testid'])
   my_dict['testscript']=response['issues'][i]['fields']['customfield_10113']
   print (my_dict['testscript'])
   my_dict['automatable_reason']=response['issues'][i]['fields']['customfield_19300']
   print (my_dict['automatable_reason'])
   if(str(response['issues'][i]['fields']['customfield_11500'])=="None"):
        my_dict['team']=response['issues'][i]['fields']['customfield_11500']
   else:
        my_dict['team']=response['issues'][i]['fields']['customfield_11500']['value']

   print (my_dict['team'])

   
   #my_dict['automatable']=response['issues'][i]['fields']['customfield_15600']
   #print (my_dict['automatable'])
   result.append(my_dict)
   i=i+1 
back_json=json.dumps(result, output_file)
output_file.write(back_json)

output_file.close() 
print("bye")
