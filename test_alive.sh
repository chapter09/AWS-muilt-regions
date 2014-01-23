#!/bin/bash

./vxargs.py -a hosts_list -o ./log -P 16 ssh ubuntu@{} "uptime"
