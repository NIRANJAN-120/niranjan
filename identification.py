db={'username':'poojitha','password':'123456'}
user=input('enter your user name \n')
password=input('enter your password \n')
if user==db['username'] and password==db['password']:
    print('sucessfully logged in')
else:
    print('wrong details')
 
