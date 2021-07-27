import time
import datetime

noloket = '01'
now=datetime.datetime.now()
ticketno=now.strftime("%y%m%d%H%M%S")+noloket
tgl=now.strftime("%d %b %Y")
tIN=now.strftime("%Y-%m-%d %H:%M:%S")



import requests,json
from requests.structures import CaseInsensitiveDict

#url = "https://api-sprk.pinisi-elektra.com/api/v1/users/login"
url_ci = "https://api-sprk.pinisi-elektra.com/api/hardware/v1/parking-vehicles/in"


test_file = open("car.jpg", "rb")
header_check = CaseInsensitiveDict()
header_check["Accept"] = "application/json"
header_check["Device-Code"] = "51J1-68DD-IFK3-19HE"
#xyheader_check["Authorization"] ='Bearer '+token
param_ci = {
 "category_id":'3',
 "license_plate":'B123456',
 "client_time":tIN,
 "bill_no":ticketno
}
pic = {"photo_check_in": test_file}

post_ci = requests.post(url_ci, headers=header_check, data=param_ci, files=pic)

#print(token)

print (post_ci.text)
