import os, sys
import socket
import subprocess

#host_map = {
#    "ip-172-31-31-93": ("54.193.26.119", 'california'),
#    "ip-172-31-31-92": ("54.193.67.252", 'california'),
#    "ip-172-31-5-233": ("54.194.219.19", 'ireland'),
#    "ip-172-31-5-232": ("54.194.219.8", 'ireland'),
#    "ip-172-31-9-112": ("54.199.128.226", 'tokyo'),
#    "ip-172-31-9-113": ("54.199.164.39", 'tokyo'),
#    "ip-172-31-42-119": ("54.200.105.10", 'oregon'),
#    "ip-172-31-42-118": ("54.200.75.61", 'oregon'),
#    "ip-172-31-12-155": ("54.206.66.219", 'sydney'),
#    "ip-172-31-12-156": ("54.206.72.60", 'sydney'),
#    "ip-172-31-24-12": ("54.207.54.205", 'paulo'),
#    "ip-172-31-24-13": ("54.207.54.206", 'paulo'),
#    "ip-172-31-18-249": ("54.209.228.40", 'virginia'),
#    "ip-172-31-18-250": ("54.236.224.34", 'virginia'),
#    "ip-172-31-6-162": ("54.254.233.84", 'singapore'),
#    "ip-172-31-6-161": ("54.254.233.84", 'singapore'),
#    }

host_map = {}
me = socket.gethostname()
err = open('%s.err'%me, 'w+')
test = int(sys.argv[2])

peer_list = open('%s'%sys.argv[1])
for line in peer_list.readlines():
  line = line.strip().split(':')
  host_map[line[0]] = (line[1], line[2])

for entry in host_map.keys():
  if entry == me or host_map[entry][1] == host_map[me][1]:
    continue
  else:
    dst = host_map[entry]
    if test:
      p = subprocess.Popen(['sh', 'iperf-c-test.sh',\
          dst[0]], stdout=subprocess.PIPE)
    else:
      p = subprocess.Popen(['sh', 'iperf-c.sh', \
          dst[0]], stdout=subprocess.PIPE)


    
