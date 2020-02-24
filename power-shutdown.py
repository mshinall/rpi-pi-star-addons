#!/usr/bin/python -d
# -*- coding: utf-8 -*-

import os
import RPi.GPIO as GPIO

pin = 22
mins = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		GPIO.wait_for_edge(pin, GPIO.FALLING)
		print("External power off. Shutting down in " + str(mins) + " minutes...")
		os.system("sudo shutdown " + str(mins))
		GPIO.wait_for_edge(pin, GPIO.RISING)
		print("External power on. Cancelling shutdown...")
		os.system("sudo shutdown -c")
except:
	pass
finally:
	GPIO.cleanup()
