const fs = require('fs'); 
var http = require('https');
console.log("hw");
var request = require('request');
//  Basic Authentication credentials   
var username = "vajo8001"; 
var password = "Joan@dsp0";
var authenticationHeader = "Basic " + new Buffer(username + ":" + password).toString("base64");
request(   
{
url : "https://adlm.nielsen.com/jira/rest/api/2/search?jql=filter=62111&maxResults=1000",
headers : { "Authorization" : authenticationHeader }  
},
 function (error, response, body) {
 console.log(body);
 var jsonContent = JSON.stringify(jsonObj);
console.log(jsonContent);
 
fs.writeFile("./output.json", jsonContent, 'utf8', function (err) {
    if (err) {
        console.log("An error occured while writing JSON Object to File.");
        return console.log(err);
    }
 
    console.log("JSON file has been saved.");
}); 
}  );  