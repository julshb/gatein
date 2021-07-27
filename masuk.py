#script proses checkin di gate parkir
#juliver@pinisi-elektra.com

#25 July 2021
#0. pantau port sensor -- (On Progress)
#1. ambil foto kendaraan (DONE)
#2. cetak struk dengan barcode (DONE)
#3. kirim data ke server -- (ON Progress)



import os
import sys
import re
import time
import datetime

now=datetime.datetime.now()
ticketno=now.strftime("%y%m%d%H%M%S")
tgl=now.strftime("%d %b %Y")
jam=now.strftime("%H:%M:%S")


#nyalain kamera dan ambil foto
os.system('fswebcam -d v4l2:/dev/video0 -r 800x600 --jpeg 100 -D 1 --save /home/pinisi/img/%Y%m%d%H%M%S.jpg')


#start--cetak--struk
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

panda.barcode("{B"+tTime, "CODE128", function_type="B")
panda.text("\n")
panda.set(align='center')
panda.text("PASTIKAN KENDARAAN ANDA TERKUNCI")
panda.set(align='center')
panda.text("\nTIKET JANGAN SAMPAI HILANG")
panda.text("\nPOWERED BY: TMDSPark\n\n")
panda.cut()
#end--cetak--struk


