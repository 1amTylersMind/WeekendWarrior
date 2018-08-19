#!/bin/bash
for x in {1..254..1}; do
    ping -c 1 192.168.1.$x;
done