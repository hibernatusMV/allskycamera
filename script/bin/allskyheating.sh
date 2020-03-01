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
  echo "Heating is off"
else
  echo "Heating is on"
fi
}

if [ $# -eq 0 ] ; then
    echo "Argument missing: $0 on/off/status"
    exit 1
fi

if [ "$1" = "on" ] ; then
  echo "Switching AllSky heating on!"
  switch_on
elif [ "$1" = "off" ] ; then
  echo "Switching AllSky heating off!"
  switch_off
elif [ "$1" = "status" ] ; then
  getStatus
fi
