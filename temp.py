import os, sys

f = open("./temp")

for line in f.readlines():
  l = line.split(':')
  print l[1][:-2]+":", l[0]+","
