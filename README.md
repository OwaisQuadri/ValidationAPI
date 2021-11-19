# ValidationAPI

Django rest API to perform facial recognition for IoT Smart Doorbell's expo project. Can be found online deployed on Heroku using <a href="https://validation--api.herokuapp.com/">this</a> link

how to use:

- each image must be posted using base64 encoding
- use an "Authorization: Basic BASIC_AUTH_TOKEN" header
  - where BASIC_AUTH_TOKEN is your base64 encoded "username:password"
- to enter known users into database, send this POST request to the base URL:  
  {  
   "name":"",  
   "face":"",  
   "known":true  
  }
- to detect known users in an image, send this POST request to the base URL:
  {  
   "face":"",  
   "known":false  
  }
- to delete a known user, send a GET request to "/delete/name/"
- to view a known user's image, go to "/media/images/known/name.png" on a browser

Demo:  
https://drive.google.com/file/d/1Q6IkDUuqMbJJMDlL2oAemlod0cG-wVNz/view?usp=sharing
