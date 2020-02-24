#!/bin/bash

function rpi-rw() {
	sudo mount -o remount,rw /
	sudo mount -o remount,rw /boot
}

addons='button-shutdown
	battery-shutdown
	power-shutdown'
