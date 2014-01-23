#!/bin/sh
./vxargs.py -a hosts_list -o ./log -P 50 ssh -o StrictHostKeyChecking=no ubuntu@{} "killall iperf"
