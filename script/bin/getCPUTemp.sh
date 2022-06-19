#!/bin/bash

cpu=$( cat /sys/class/thermal/thermal_zone0/temp )
cpu=$(( cpu/100 )); len=${#cpu};
out=${cpu:0:$(( len-1 ))};
frac=${cpu:$(( len-1 )):99}
cpuT="$out.$frac °C"

echo $cpuT
