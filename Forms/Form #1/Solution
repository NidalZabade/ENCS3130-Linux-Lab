#!/bin/sh

while true; do
	echo "Enter Binary number: "
	read binary
	temp=$(echo $binary | tr -d 0-1)
	echo $temp
	if [ -z "$temp" ]; then 
		echo "ibase=2;obase=10000;$binary"|bc
	else
		echo "Invalid input"
	fi
	echo "continue c, quit q"
	read grade

	if [ "$grade" = "q" ]; then 
		break
	elif [ "$grade" = "c" ]; then
		continue
	fi	
	break
done
