#!/bin/bash

hex=$( ./dec2hex.sh $1 )
hexOut='0x'$hex
echo $hexOut
#EOF
