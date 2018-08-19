#!/bin/bash
for ip in 192.168.1.{1..10}; do ping -c 1 -t 1 $ip