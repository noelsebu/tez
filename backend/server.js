import express from 'express';
const app = express();


console.dir("he");
app.get('/', (_req, res) => res.send("Hello world"));
app.listen(9000, () => console.log("express is running")); 

 
var http = require('https');

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
 
}  );  
