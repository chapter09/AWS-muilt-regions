#!/bin/bash

while true
do
	iperf -c 54.207.54.205 -p 10086 > /dev/null &
	iperf -c 54.209.228.40 -p 10086 > /dev/null &
done
    
