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
            IP = line.split('inet ')[1].split("  ")[0]
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
    os.system('sudo su')
    os.system('touch host.txt')
    os.system('hostname >> host.txt')
    name = open('host.txt','r').readlines().pop().replace('\n','')
    os.system('rm host.txt')
    print("Hostname: "+name)
    return name


def find_hosts():
    start = time.time()
    os.system('cd bashkitcase; su root ./pings.sh >> localhosts.txt')
    f = open('localhosts.txt', 'r')
    unused = list()
    found = list()
    index = 1
    for line in f.readlines():
        try:
            ping = line.split('ttl')[0]
        except:
            list.append(index)
        index += 1
    os.system('cd bashkitcase; rm lanscan.txt')
    dt = time.time() - start
    print("Scan finished in "+str(dt)+"s.")
    print(str(len(found))+" live hosts found")
    return found, dt


def quick_host_discovery():
    start = time.time()
    os.system('cd bashkitcase; python arper.py >> arps.txt; cat arps.txt')
    f = open('arps.txt','r')
    hosts = list()
    for line in f.readlines():
        hosts.append(line)
    dt = time.time() - start;
    print("Scan Finished in "+str(dt)+"s. ")
    print(str(len(hosts))+" live hosts found")
    os.system('cd bashkitcase; rm arps.txt')
    return hosts. dt


def main():
    if os.name == "nt":
        print("OS: Windows")
    else:
        print("OS: "+os.name)
        print("----------------------------------------------")
        # Now do the really fast scan to compare the speed
        ppl,t0 = quick_host_discovery()
        print("----------------------------------------------")
        try:
            ip, wlanmac = get_nx_info('wlan0')
            i, ethmac = get_nx_info('eth0')
        except UnboundLocalError:
            print("Couldn't get MAC and IP")
        print("----------------------------------------------")
        try:
            lanppl, t1 = find_hosts()
            DT = t0 - t1
            print("Exhaustive Ping scan took "+DT+"s longer")
        except KeyboardInterrupt:
            print("Killed Scan")
        print("----------------------------------------------")
        try:
            hostname = get_localhost_name()
        except:
            print("Couldnt get hostname")
        print("----------------------------------------------")


if __name__ == '__main__':
    main()
