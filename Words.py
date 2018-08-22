import sys, os, time, numpy as np, hashlib
import matplotlib.pyplot as plt
start = time.time()
# Basically run a small shell script from python to
# grab the word count of each Letters .csv list
os.system('cd BigData/words; ls | while read line;'
          'do python w3rd.py $line >> wordcount.txt; done')
# Need to copy that out of the BigData folder and back to topdir
# so I can read out the word counts recorded for each letter
os.system('cat $PWD/BigData/words/wordcount.txt >> data.txt;'
          'rm $PWD/BigData/words/wordcount.txt')
# Create a file, and some variables for storing the word count data
f = open('data.txt','r')
letters = []
N = []
Counts = {}

for line in f.readlines():
    N.append(int(line.split(' ')[0]))
    letters.append(line.split(' ')[1])
    Counts[line.split(' ')[1]] = line.split(' ')[0]
words_read = np.sum(np.array(N))
dt = time.time() - start
os.system('rm data.txt')
print((str(words_read)) + " words read in " + str(dt) + " seconds ")

# This bar plot isn't showing all of the letters for some reason
plt.bar(np.array((letters)),N)
plt.show()

print ("Testing Entropy of all "+str(words_read)+" words as hex")
# Now get the encrypted word data and start the clock(s)
timer = time.time()
os.system('cd BigData/words; ls | while read line;'
          'do python fasthash.py hex $line >> hex.txt; done')
hextime = time.time() - timer
print ("Testing Entropy of all "+str(words_read)+" words sha256 hashed hex")
timer1 = time.time()
os.system('cd BigData/words; ls | while read line;'
          'do python fasthash.py sha256 $line >> sha256.txt; done')
sha256time = time.time() - timer1
print ("Testing Entropy of all "+str(words_read)+" words as md5 hashed hex")
timer2 = time.time()
os.system('cd BigData/words; ls | while read line;'
          'do python fasthash.py md5 $line >> md5.txt; done')
md5time = time.time() - timer2
timer3 = time.time()
#os.system('cd BigData/words; ls | while read line;'
#          'do python fasthash.py sha1 $line >> sha1.txt; done')
sha1time = time.time() - timer3
timer4 = time.time()
os.system('cd BigData/words; ls | while read line;'
          'do python fasthash.py sha512 $line >> sha512.txt; done')
sha3time = time.time() - timer4
print("________** TIMERS **________")
print("HEX: "+str(hextime)+" seconds")
print("SHA-256: "+str(sha256time)+" seconds")
print("MD5: "+str(md5time)+" seconds")
print("SHA-512: "+str(sha3time)+" seconds")
os.system('cd BigData/words; rm hex.txt sha256.txt md5.txt sha512.txt')