#!/bin/sh

while true; do
	echo "Enter a string: (q to quit) "
	read temp
	if [ "$temp" = "q" ]; then break;fi
	string=$(echo "$temp"| tr '[:upper:]' '[:lower:]' | tr -d " ")
	p=1
	temp=$(echo "$string" | cut -c$p )
	allString=$(echo "$string" | cut -c$p --complement)
	until [ -z "$temp" ]; do

		if echo "$allString" | grep "$temp" > /dev/null; then
			p=$((p+1))
			temp=$(echo "$string" | cut -c$p )
			allString=$(echo "$string" | cut -c$p --complement)
			continue
		else
			echo $temp
			break
		fi
	done
done
