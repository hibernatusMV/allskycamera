#!/bin/bash

# define maximum and minimum temperature
max_temp=18
min_temp=5

cur_temp=$( ./getTemp.sh )
stat=$( ./allskyheating.sh status )
t=$(date +%H:%M:%S)

echo "$t  Temp: $cur_temp -> $stat"

# checking temperature
if [ $cur_temp -ge $max_temp ] ; then
  if [ "$stat" == "Heizung ist an" ] ; then
    echo "$t  "
    ./allskyheating.sh off
    exit 1
  fi
fi

if [ $cur_temp -lt $min_temp ] ; then
  if [ "$stat" == "Heizung ist aus" ] ; then
    echo "$t  "
    ./allskyheating.sh on
    exit 1
  fi
fi
