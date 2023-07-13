#!/usr/bin/python

from picamera import PiCamera
import time
#import argparse

import board
import neopixel

#from ids import IDS


#date = time.strftime("%Y-%m-%d", time.localtime())
#d_time = time.strftime("_%H_%M_%S", time.localtime())

#ids = IDS()
#devID=ids.devID

#sesID=ids.sesID

#TestID = input("please scan a command RFID\n")[-8:]


camera = PiCamera()
camera.resolution = (1920, 800)
camera.framerate = 30
camera.brightness= 45
pixels = neopixel.NeoPixel(board.D18, 128)
for i in range(64):
	pixels[i] = (15, 6, 0)
for i in range(64,128):
        pixels[i] = (27, 0, 0)
camera.stop_preview()
camera.start_preview()
#file_name= "/home/pi/video/Soc_" + date + d_time + "_BOX_" + devID + "_S" + str(sesID) + "_" + color + ".h264"
#print(file_name)
#camera.start_recording(file_name)
time.sleep(120)
#camera.stop_recording()
camera.stop_preview()
for i in range(len(pixels)):
	pixels[i] = (0, 0, 0)

