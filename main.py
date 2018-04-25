import requests

import util

INFO_FILE = "info.txt"


USER_NAME = util.setinfo('USER_NAME')
PASSWORD =  util.setinfo('PASSWORD')

TIME_OUT = 1

 
r = requests.get('https://www.gumtree.co.za/login.html', timeout = TIME_OUT)

login_details = {"email": USER_NAME, "password": PASSWORD}
s = requests.post('https://www.gumtree.co.za/login', timeout = TIME_OUT, data = login_details)

print (s.cookies)
next = requests

