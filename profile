#!/bin/bash

function rpi-rw() {
	sudo mount -o remount,rw /
	sudo mount -o remount,rw /boot
}

addons='battery-shutdown'
