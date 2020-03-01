#!/bin/bash

temp=$( tail -1 /sys/bus/w1/devices/28-0114557a81aa/w1_slave | awk -F 't=' '{print $2}' )
temp=`echo "scale=3; $temp / 1000" | bc`
echo $temp
