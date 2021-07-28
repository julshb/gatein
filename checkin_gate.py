import os
import sys
import re
import time
import datetime


import requests,json
from requests.structures import CaseInsensitiveDict

#URL API  for sending data masuk parkir
url_ci = "https://api-sprk.pinisi-elektra.com/api/hardware/v1/parking-vehicles/in"
noloket = '01'
now=datetime.datetime.now()
ticketno=now.strftime("%y%m%d%H%M%S")+noloket
tgl=now.strftime("%d %b %Y")
tIN=now.strftime("%Y-%m-%d %H:%M:%S")


tTime=now.strftime("%y%m%d%H%M%S")
#tgl=now.strftime("%d %b %Y")
jam=now.strftime("%H:%M:%S")


#put camera ON then take a picture
os.system('fswebcam -d v4l2:/dev/video0 -r 800x600 --jpeg 100 -D 1 --save /home/pinisi/img/mobil.jpg')



from escpos.printer import *
panda = Usb(0x0483,0x5840,0,0,0x03)
panda.set()
panda.set(align='center')
panda.text("\nPARKING TICKET\n\n")

panda.set(align='left', text_type='B')
panda.text("TMD Spark Parking Building\n")

def printItem(first, second):
  panda.set(align='left', text_type='B')
  panda.text(first)
  panda.set(text_type='NORMAL')
  panda.text(str(second) + "\n")

printItem("TICKET NO	: ", ticketno)
printItem("Date		: ", tgl)
printItem("Time		: ", jam)

panda.text("\n")

panda.barcode("{B"+ticketno, "CODE128", function_type="B")
panda.text("\n")
panda.set(align='center')
panda.text("PASTIKAN KENDARAAN ANDA TERKUNCI")
panda.set(align='center')
panda.text("\nTIKET JANGAN SAMPAI HILANG")
panda.text("\nPOWERED BY: TMDSPark\n\n")
panda.cut()

#send to server
foto_mobil = open("/home/pinisi/img/mobil.jpg", "rb")
header_check = CaseInsensitiveDict()
header_check["Accept"] = "application/json"
header_check["Device-Code"] = "51J1-68DD-IFK3-19HE"
#xyheader_check["Authorization"] ='Bearer '+token
param_ci = {
 "category_id":'3',
 "client_time":tIN,
 "bill_no":ticketno
}
pic = {"photo_check_in": foto_mobil}

post_ci = requests.post(url_ci, headers=header_check, data=param_ci, files=pic)

#print(token)
#print (post_ci.text)

