# Weekend Warrior
Working during the week doesn't leave me as much time to mess around 
as I would like. Making this space to manage the little projects I mess with 
on the weekends. 

# reporter.py
This is a python script that enumerates the name, IP address and MAC address
 of the local machine in addition to the ip addresses of all machines on the local
 network. I also wrote this because I wanted to compare how much faster it is to
 accomplish this task with a single scapy command, compared with an exhaustive
 ping search (the trade of being the arp command creates very noticeable network
 traffic compared to the quiter pings). 
 
# Words.py
I've been thinking a lot recently about entropy, and so I thought it might be
interesting to apply that perspective to first plain english (for a reference),
and then various cryptographic hashes of the same english words with different ciphers. 

What I think will be most interesting is to see the incremental change from low
to high entropy by trying different things like moving from plain text, to hex, 
to something that's actually the hex output of a hash. 
![Words](https://raw.githubusercontent.com/1amTylersMind/WeekendWarrior/master/WordsOut.png)

Before I actually start comparing the entropy of all EOWL hashes, I wanted to time the actual speed of the hashing itself. 
This picture shows three trials, where surprisingly the python hex encoding is the slowest process and the SHA-256 encryption is the fastest. The Hex time is not really all that slow, considering the size of the data but it's interesting.
