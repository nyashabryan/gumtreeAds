import requests


INFO_FILE = "info.txt"

def setinfo(name):
    with open(INFO_FILE, "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.split(': ')[0] == name:
            return line.split(': ')[1][:-1]
    return "None "


USER_NAME = setinfo('USER_NAME')
PASSWORD =  setinfo('PASSWORD')

TIME_OUT = 1

 
r = requests.get('https://www.gumtree.co.za/login.html', timeout = TIME_OUT)

login_details = {"email": USER_NAME, "password": PASSWORD}
s = requests.post('https://www.gumtree.co.za/login', timeout = TIME_OUT, data = login_details)

print (s.cookies)


