#!/bin/sh
#./vxargs.py -a hosts_list -o ./log -P 16 ssh -o StrictHostKeyChecking=no ubuntu@{} 'python iperf-main.py peer_list 1'
./vxargs.py -a hosts_list -o ./log -P 16 ssh -o StrictHostKeyChecking=no ubuntu@{} 'python iperf-main.py peer_list 0'
