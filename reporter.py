#!/bin/env/python
import os, sys, time, socket

def get_nx_info(iface):
    """
    Get the IP and MAC addresses of the local machine
    :param iface:
    :return IP, MAC:
    """
    os.system('touch nxinfo.txt')
    os.system('ifconfig '+iface+' >> nxinfo.txt')
    nxtxt = open('nxinfo.txt', 'r')
    unused = 0
    IP=""
    for line in nxtxt.readlines():
        try:
            IP = line.split('inet ')[1].split('netmask')[0]
            print("IP "+IP)
        except:
            unused += 1
        try:
            MAC = line.split("ether ")[1].split("  ")[0]
            print(iface+" MAC: " + MAC)
        except:
            unused += 1
    os.system('rm nxinfo.txt')
    return IP, MAC


def get_localhost_name():
    os.system('touch host.txt')
    os.system('hostname >> host.txt')
    name = open('host.txt','r').readlines().pop().replace('\n','')
    os.system('rm host.txt')
    print("Hostname: "+name)
    return name


def main():
    if os.name == "nt":
        print("OS: Windows")
    else:
        print("OS: "+os.name)

        hostname = get_localhost_name()
        ip, wlanmac = get_nx_info('wlan0')
        i, ethmac = get_nx_info('eth0')


if __name__ == '__main__':
    main()
