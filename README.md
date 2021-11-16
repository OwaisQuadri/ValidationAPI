# ValidationAPI
Django rest API to perform facial recognition for IoT Smart Doorbell's expo project. will soon be deployed on heroku.


how to use:
- each image must be posted using base64 encoding
- to enter known users into database:  
{  
    "name":"",  
    "face":"",  
    "known":true  
}  
- to detect known users in an image:  
{  
    "face":"",  
    "known":false  
}  
