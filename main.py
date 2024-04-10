#!/usr/bin/python3

import time
import subprocess
import board
import neopixel
import os
import sys
import shutil

from ids import IDS

os.system("clear")
## check available space on disk
free=shutil.disk_usage("/")[2]
freegb=free/(1024*1024*1024)
if (freegb<2.5):
    print ("The disk is full\n")
    print ("The disk is full\n")
    exit()
else:
    print (str(round(freegb,1)) +"Gb free")

## make sure drive is not write protected
try:
    with open('/home/pi/testdisk', 'w') as f:
        pass
except IOError as x:
    print (x.strerror)
    sys.exit("disk is not writable")

## collection session meta data
date = time.strftime("%Y-%m-%d", time.localtime())
d_time = time.strftime("_%H_%M_%S", time.localtime())
print ("current date_time:"+date+d_time)
ids = IDS()
devID=ids.devID
sesID=ids.sesID

pixels = neopixel.NeoPixel(board.D18, 128)
for i in range(128):
   pixels[i] = (10, 10, 10)

# collect info on color preference of the test subject
PrefID=input("Please scan the pattern/color preference of the fish, use yellow/blue if unknown\n")[-2:]
while PrefID != "ef" and PrefID != "62" and PrefID != "5d":
   print (PrefID)
   print("RFID is not correct, please scan either grid/yellow,  circle/blue, or  yellow/blue for unknown preference\n")
   PrefID = input("Please scan the pattern/color preference of the fish\n")[-2:]

if PrefID[-2:] == "ef": #0087b4ef
   Pref="Unknown"
if PrefID[-2:] == "62": #0084cb62
   #Pref="Blue"
   Pref="Circle"
if PrefID[-2:] == "5d": #002d2e5d
   #Pref = "Yellow"
   Pref="Grid"

# start camera 
os.system("raspivid --framerate 24 -t 600000 & ")


# which light to turn on?
TestID = input("please scan an RFID for the pattern/color of the LEDs\n")[-2:]
while TestID != "ef" and TestID != "62" and TestID != "5d": 
   print (TestID)
   print("RFID is not correct, please rescan")
   TestID = input("please scan an RFID for the pattern/color of the LEDs\n")[-2:]

os.system("killall raspivid")

if TestID[-2:] == "ef": #0087b4ef
   color="BI"
   #a,b,c,d,e,f = 15,11,0,0,0,18
   a,b,c,d,e,f = 15,15,15,15,15,15
	
if TestID[-2:] == "62": #0084cb62
   #color="BL"
   color="Circle"
   #a,b,c,d,e,f= 0,0,18,0,0,18
   a,b,c,d,e,f = 15,15,15,15,15,15
if TestID[-2:] == "5d": #002d2e5d
   #color = "YL"
   color="Grid"
   #a,b,c,d,e,f = 15,11,0,15,11,0
   a,b,c,d,e,f = 15,15,15,15,15,15

if Pref == "Unknown" and color !="BI":
   sys.exit("Fish with unknown pattern/color preference must be tested with both patterns/colors, please restart")

#pixels = neopixel.NeoPixel(board.D18, 128)
#for i in range(64):
#	pixels[i] = (a, b, c)
#for i in range(64,128):
#    pixels[i] = (d, e, f)

file_name= "/home/pi/video/CPP_" + devID + "-S" + str(sesID) + "-" + date + d_time + "-prefer-" + Pref +"-floor-" + color + ".h264"
print(file_name)
#msec=15*60*1000
msec=20*60*1000
os.system("raspivid --framerate 30 -hf -br 50 -pts " + file_name +".time.txt" + " -t "+ str(msec) + " -o " + file_name)
print("raspivid --framerate 30 -hf -br 50 -pts " + file_name +".time.txt" + " -t "+ str(msec) + " -o " + file_name)

ids.sessionIncrement()
time.sleep(1)

#stop if it is preference test, otherwise continue conditioning test
light=input('Please scan BI key to turn off light or other key to continue conditioning \n')[-2:]
if light[-2:] == "ef":
   for i in range(128):
      pixels = neopixel.NeoPixel(board.D18, 128)
      pixels[i] = (0, 0, 0)
      sys.exit("Preference test finished")


# collect info on color preference of the test subject
sesID=ids.sesID
PrefID=input("Please scan the pattern/color preference of the fish \n")[-2:]
while PrefID != "62" and PrefID != "5d":
   print (PrefID)
   print("RFID is not correct, please scan either grid/yellow or  circle/blue for conditioning. \n")
   PrefID = input("Please scan the pattern/color preference of the fish\n")[-2:]

if PrefID[-2:] == "62": #0084cb62
   #Pref="Blue"
   Pref="Circle"
if PrefID[-2:] == "5d": #002d2e5d
   #Pref = "Yellow"
   Pref="Grid"

# start camera 
os.system("raspivid --framerate 24 -t 600000 & ")

# which light to turn on?
TestID = input("please scan an RFID for the pattern/color of the LEDs\n")[-2:]
while TestID != "62" and TestID != "5d": 
   print (TestID)
   print("RFID is not correct, please rescan")
   TestID = input("please scan an RFID for the pattern/color of the LEDs\n")[-2:]

os.system("killall raspivid")

if TestID[-2:] == "62": #0084cb62
   #color="BL"
   color="Circle"
if TestID[-2:] == "5d": #002d2e5d
   #color = "YL"
   color="Grid"

file_name= "/home/pi/video/CPP_" + devID + "-S" + str(sesID) + "-" + date + d_time + "-prefer-" + Pref +"-floor-" + color + ".h264"
print(file_name)
#msec=15*60*1000
msec=20*60*1000
os.system("raspivid --framerate 30 -hf -br 50 -pts " + file_name +".time.txt" + " -t "+ str(msec) + " -o " + file_name)
print("raspivid --framerate 30 -hf -br 50 -pts " + file_name +".time.txt" + " -t "+ str(msec) + " -o " + file_name)

ids.sessionIncrement()
time.sleep(1)

light=input('Please scan any key to turn off light\n')[-2:]
time.sleep(1)
for i in range(128):
   pixels[i] = (0, 0, 0)
print("Conditioning finished")

#subprocess.call(['./convert_video.sh', str(file_name)])
