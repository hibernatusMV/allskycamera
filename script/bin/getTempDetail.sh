#!/bin/bash

temp=$( tail -1 /sys/bus/w1/devices/28-011455a5d7aa/w1_slave | awk -F 't=' '{print $2}' )
temp=`echo "scale=2; $temp / 1000" | bc`
echo "$temp °C"
