#!/bin/bash

temp=$( vcgencmd measure_temp | awk -F 'temp=' '{print $2}' )
temp=${temp:0:4}
echo "$temp °C"
