import sys, os, time
"""
If I want to make the Sonic Program into something portable, I'll need
to be able to access some basic system information efficiently. So
this little script does that.
"""
def getProgsAvailable():
    os.system('ls /usr/bin >> progs.txt')
    programs = []
    for line in open('progs.txt', 'r').readlines():
        programs.append(line.replace('\n',''))
    os.system('rm progs.txt')
    return programs


def getHostname():
    os.system('hostname >> hostname.txt')
    name = open('hostname.txt', 'r').readlines().pop().replace('\n','')
    os.system('rm hostname.txt')
    return name


def getIPinfo():
    os.system('ifconfig >> config.txt')
    inetdata = open('config.txt', 'r')
    ipdata = []
    for line in inetdata.readlines():

        try:
            ipdata.append(line.replace('\n','').split('inet ')[1].split('netmask')[0])
        except:
            pass
    os.system('rm config.txt')
    return ipdata


def checkNetConnected():
    os.system('route >> inetroute.txt')
    routedata = []
    for line in open('inetroute.txt', 'r').readlines():
        routedata.append(line.replace('\n',''))
        print line.replace('\n','')
    os.system('rm inetroute.txt')
    return routedata

def main():
    start = time.time()
    programs = getProgsAvailable()
    print str(len(programs)) + " programs found in usr/bin "

    name = getHostname()
    print "This Machine's Host Name is : " + name
    print "OS is "+os.name

    ips = getIPinfo()
    print "IP/MAC Addresses Associated w. this machine: "
    for ip in ips:
        print " * "+ip
    netconnect = checkNetConnected()
    if len(netconnect) < 4:
        print "No Route to Internet"

    print " Finished ["+str(time.time() - start) + "s elapsed]"


if __name__ == '__main__':
    main()
