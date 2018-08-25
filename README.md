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



# Here's a vieo of the results of hashing the entire ~130K word EOWL with MD5, SHA-256,
# SHA-512 and HEX encoding. You might be surprised by the end times. I was.  
<iframe width="560" height="315" src="https://www.youtube.com/embed/-RhIH4T0Z2k" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
