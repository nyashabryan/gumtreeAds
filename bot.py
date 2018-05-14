import requests

import util
import time


USER_NAME = util.setinfo('USER_NAME')
PASSWORD =  util.setinfo('PASSWORD')
COOKIE_JAR = 0

print (USER_NAME)
print (PASSWORD)
TIME_OUT = 1
TIME_DELAY = 2

def login():
    global COOKIE_JAR
    r = requests.get('https://www.gumtree.co.za/login.html', timeout = TIME_OUT)
    login_details = {"email": USER_NAME, "password": PASSWORD}
    s = requests.post('https://www.gumtree.co.za/login', timeout = TIME_OUT, data = login_details)

    #print (s.text)

    COOKIE_JAR = s.cookies
    next = requests.get('https://www.gumtree.co.za/', cookies = COOKIE_JAR, timeout = TIME_OUT)

def post():
    data = {
        "locationId": "3100029",
        "UserName": "Tony Painters",
        "Email": "tonypainters18@gmail.com",
        "Phone": "0788542920",
        "Title": "An Ad for days",
        'machineId': "a0319b7d-3ef9-4cd5-8635-8bbeded39955-16234b60357",
        "Description": "This a well made DSTv Ad. Automated. Good.",
        "latitude": "-33.9271027",
        "longitude": "18.45608919999995",
        "adminAreaName": "Western Cape",
        "addressConfidenceLevel": "ROOFTOP",
        "countryCode": "ZA",
        "street": "Bromwell Street",
        "locality": "Cape Town",
        "Address": "68 Bromwell St, Woodstock, Cape Town, 7915, South Africa"
    }

    r = requests.post("https://www.gumtree.co.za/post.html", cookies = COOKIE_JAR, timeout = TIME_OUT, data = data)

    print (r.status_code)

login()
time.sleep(30)
post()
