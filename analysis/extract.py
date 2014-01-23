#!/usr/bin/python

import os
import sys
import re
from xlwt import *

host_map = {}

def main(opts):
  global host_map
  w = Workbook()

  peer_list = open('%s'%opts[1])
  for line in peer_list.readlines():
    if line.startswith('#'):
      continue
    line = line.strip().split(':')
    host_map[line[0]] = (line[1], line[2])
  
  path = opts[2]
  for f in os.listdir(path):
    if f.strip()[-3:] == 'log':
      print 'Parsing File %s'%(path+'/'+f)
      extract(path+'/'+f, f[:-4], w)

  w.save('./%s.xls'%os.path.basename(opts[2]))
  print '---EXTRACT FINISHED---\n'

def extract(f, me, workbook):
  global host_map
  my_info = host_map[me]
  ws = workbook.add_sheet(my_info[0]+'-'+my_info[1])
  print '\tAdd Sheet %s'%(my_info[0]+'-'+my_info[1])

  ip_to_col = build_colname(ws, me)

  id_to_ip = {}
  ip_bw_counter = {}

  fd = open(f)
  col_index = 0
  for line in fd.readlines():
    if line.find('10086 connected') > -1:
      # [ 11] local 172.31.12.155 port 10086 connected with ...
      peer_id = int(re.match(r'^\[(.+?)\]', line).group(1).strip())
      addrs = re.findall(r"((\d+\.){3}\d+)", line)
      id_to_ip[peer_id] = addrs[1][0]

    elif line.find('SUM') > -1:
      continue

    elif line.find('Mbits/sec') > -1:
      peer_id = int(re.match(r'^\[(.+?)\]', line).group(1).strip())
      bw = float(re.search(r'(\d+\.\d+.)Mbits/sec', line).group(1).strip())
      peer_ip = id_to_ip[peer_id]

      if ip_bw_counter.has_key(peer_ip):
        ip_bw_counter[peer_ip] += 1
      else:
        ip_bw_counter[peer_ip] = 1

      ws.write(ip_bw_counter[peer_ip], ip_to_col.index(id_to_ip[peer_id])+1, bw)

def build_colname(ws, me):
  global host_map
  ip_to_col = []

  ws.write(0, 0, 'Time')
  for h in host_map.keys():
    if h == me or host_map[h][1] == host_map[me][1]:
      continue
    else:
      peer = host_map[h]
      ip_to_col.append(peer[0])
      ws.write(0, ip_to_col.index(peer[0])+1, peer[0]+'-'+peer[1])
  return ip_to_col


if __name__ == '__main__':
  print 'Analysis Start...'
  main(sys.argv)


