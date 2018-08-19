#!/bin/bash

iwlist wlan0 scanning >> lanscan.txt
cat lanscan.txt | while read line;
 do
    echo $line
done
rm lanscan.txt
