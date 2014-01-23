#!/bin/bash

d=`date +%F-%s`;
mkdir -p ./feedback/$d;
./vxargs.py -a $1 -P 100 -o log/ scp -o StrictHostKeyChecking=no ubuntu@{}:'ip*.log' feedback/$d/;
