#!/bin/bash

# GPIO setup
if ! [ -d "/sys/class/gpio/gpio17" ] ; then
echo "17" > /sys/class/gpio/export
sudo chmod 222 /sys/class/gpio/gpio17/direction
#  if ! [ -d "/sys/class/gpio/gpio17" ] ; then
#   echo "Fehler beim erstellen von /sys/class/gpio/gpio17/"
#	exit 1
#  fi
echo "out" > /sys/class/gpio/gpio17/direction
fi

function switch_on {
  gpio write 0 1
}

function switch_off {
  gpio write 0 0
}

function getStatus {
status=$( cat /sys/class/gpio/gpio17/value )

if [ $status -eq 0 ] ; then
  echo "Heizung ist aus"
else
  echo "Heizung ist an"
fi
}

if [ $# -eq 0 ] ; then
    echo "Bitte Parameter angeben: $0 on/off/status"
    exit 1
fi

if [ "$1" = "on" ] ; then
  echo "Schalte AllSky Heizung ein!"
  switch_on
elif [ "$1" = "off" ] ; then
  echo "Schalte AllSky Heizung aus!"
  switch_off
elif [ "$1" = "status" ] ; then
  getStatus
fi
