from PIL import ImageGrab
import os
import win32api, win32con
import time
import numpy
from numpy import array
import cv2
 
def screenGrab():
	box = (530,124,1061,653)
	#box = (530,125,550,150)
	im = ImageGrab.grab(box)
	im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
	return array(frame).tolist()
 
def get_first_point(img): #A compléter
	frame = array(img)
	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# define range of blue color in HSV
	lower_blue = numpy.array([110,50,50])
	upper_blue = numpy.array([130,255,255])
	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mask)
	#Affichage pour débugger 
	#cv2.imshow('frame',frame)
	#cv2.imshow('mask',mask)
	#cv2.imshow('res',res)
	#cv2.waitKey(0)
	
	return array(res)

def hold_left():
	win32api.keybd_event(0x25,0,0,0)

def hold_right():
	win32api.keybd_event(0x27,0,0,0)
	
def left():
	win32api.keybd_event(0x25,0,0,0)
	time.sleep(.05)
	win32api.keybd_event(0x25,0,win32con.KEYEVENTF_KEYUP,0)

def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	
def mouse_click():
	win32api.SetCursorPos((700, 380))
	leftClick()

def right():
	win32api.keybd_event(0x27,0,0,0)
	time.sleep(.05)
	win32api.keybd_event(0x27,0,win32con.KEYEVENTF_KEYUP,0)	

def main():
	numpy.set_printoptions(threshold=numpy.inf)
	screenGrab()
    #while(True):
	#	mouse_click()
	#	hold_right()
	#	time.sleep(1)
	#	up_right()
	#	hold_left()
	#	time.sleep(1)
	#	up_left()
	
def up_left():
	win32api.keybd_event(0x25,0,win32con.KEYEVENTF_KEYUP,0)

def up_right():
	win32api.keybd_event(0x27,0,win32con.KEYEVENTF_KEYUP,0)	
 
if __name__ == '__main__':
    main()