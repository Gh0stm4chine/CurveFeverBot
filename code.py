from PIL import ImageGrab
import os
import win32api, win32con
import time
import numpy
from numpy import array
 
def screenGrab():
	#box = (530,124,1061,653)
	box = (530,125,550,150)
	im = ImageGrab.grab(box)
	im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
	return array(im).tolist()
 

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
	print screenGrab()
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