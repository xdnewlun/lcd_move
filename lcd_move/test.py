import signal as sig
import RPi.GPIO as gpio
from time import  sleep
from lcd import LCD
from screen import Screen

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(5, gpio.IN)
gpio.setup(12, gpio.IN)

run = True

def on_exit(a,b):
    global run
    run = False
    
sig.signal(sig.SIGINT,on_exit)
print("Ctrl+C to exit")

# see comments in lcd.py
lcd = LCD(22,21,17,23,25,24)

# change these line to test
# 1st line = 0
# 2nd line = 1
#lcd.set_cursor(0,2) # line,column
#lcd.send_string('Xander Newlun')

screen = Screen(['Dog', 'Cat', 'Moose', 'Potatoes'], lcd)
screen.display();

is_press = False

while run:
	if gpio.input(5) == False:
		if is_press == False:
			screen.moveDown()
			screen.display()
			is_press = True
		else:
			print('STOP')
	elif gpio.input(5) == True:
		is_press = False
	elif gpio.input(12) == False:
		print("Button")

while run:
    sleep(1)
    
lcd.close()
print('Done')