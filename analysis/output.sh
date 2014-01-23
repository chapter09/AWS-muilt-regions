#!/bin/bash

find $1 -type f -name '*.log' -print | while read filename; do
  echo "$filename"
  cat "$filename"
  echo
done > $2.log
