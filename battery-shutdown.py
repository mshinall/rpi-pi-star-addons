#!/usr/bin/python -d
# -*- coding: utf-8 -*-

import datetime
import os
import RPi.GPIO as GPIO

pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	GPIO.wait_for_edge(pin, GPIO.FALLING)
	now = datetime.datetime.now()
	date = now.strftime("%Y-%m-%d %H:%M:%S")
	print(date + " - Low Battery. Shutting down now!")
	os.system("sudo shutdown now")
except:
	pass
finally:
	GPIO.cleanup()
