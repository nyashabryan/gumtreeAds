import requests

import util


USER_NAME = util.setinfo('USER_NAME')
PASSWORD =  util.setinfo('PASSWORD')

print (USER_NAME)
print (PASSWORD)
TIME_OUT = 1

 
r = requests.get('https://www.gumtree.co.za/login.html', timeout = TIME_OUT)

login_details = {"email": USER_NAME, "password": PASSWORD}
s = requests.post('https://www.gumtree.co.za/login', timeout = TIME_OUT, data = login_details)

print (s.text)

COOKIE_JAR = s.cookies
next = requests.get('https://www.gumtree.co.za/', cookies = COOKIE_JAR, timeout = TIME_OUT)

print (next.text)


