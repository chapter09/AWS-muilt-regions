#!/bin/sh
./vxargs.py -a hosts_list -o ./log -P 16 ssh -o StrictHostKeyChecking=no ubuntu@{} 'fn=`hostname`;iperf -s -p 10086 > $fn.log'
