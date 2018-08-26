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

# Here's The output of Encoding the EOWL in Hex, and looking at the letter frequency
![hexdata](https://raw.githubusercontent.com/1amTylersMind/WeekendWarrior/master/hexData.png)

# Looking at the Letter Frequency of Hashing each word in EOWL with MD5
![md5data](https://raw.githubusercontent.com/1amTylersMind/WeekendWarrior/master/md5Data.png)

# Looking at the letter frequency of Hashing each word in EOWL with SHA-256
![sha256data](https://raw.githubusercontent.com/1amTylersMind/WeekendWarrior/master/sha256Data.png)

# Looking at the letter frequency of Hashing each world in the EOWL with SHA-512 
![sha512data](https://raw.githubusercontent.com/1amTylersMind/WeekendWarrior/master/sha512Data.png)

# Here's a vieo of the results of hashing the entire ~130K word EOWL with MD5, SHA-256, SHA-512 and HEX encoding.  
[video of the hashing (boring and slow)](https://www.youtube.com/embed/-RhIH4T0Z2k)
