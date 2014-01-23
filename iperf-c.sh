#!/bin/bash

while true
do
	iperf -c $1 -i 1 -p 10086
	sleep 300
done
    
