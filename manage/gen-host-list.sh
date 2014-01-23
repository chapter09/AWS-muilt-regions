#!/bin/bash
regions=$(ec2-describe-regions | cut -f2)

for region in $regions; do
  echo $region >> host_list.log
  ec2-describe-network-interfaces --region $region >> host_list.log
#      ec2-import-keypair --region $region --public-key-file $publickeyfile $keypair
  done
