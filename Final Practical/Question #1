#!/bin/sh
echo "Enter first 4 bit number"
read binary1
temp=$(echo $binary1 | tr -d 0-1)
if [ -z "$temp" ]; then
	echo "$binary1"
else
	echo "Invalid input The input should be only 0 or 1"
	exit 0
fi
echo "Enter second 4 bit number"
read binary2
temp2=$(echo $binary2 | tr -d 0-1)
if [ -z "$temp2" ]; then
	echo "$binary2"
else
	echo "Invalid input The input should be only 0 or 1"
	exit 0
fi
total=$(echo "ibase=2;obase=2; $binary1+$binary2"|bc)
echo "$total"
