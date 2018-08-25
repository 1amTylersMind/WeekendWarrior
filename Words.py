import sys, os, time, numpy as np, hashlib
import matplotlib.pyplot as plt
start = time.time()

# Basically run a small shell script from python to
# grab the word count of each Letters .csv list
os.system('cd BigData/words; ls | while read line;'
          'do python w3rd.py $line >> wordcount.txt; done')
# Need to copy that out of the BigData folder and back to topdir
# so I can read out the word counts recorded for each letter
os.system('cat $PWD/BigData/words/wordcount.txt >> data.txt')

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
# os.system('rm data.txt')
os.system('rm BigData/words/wordcount.txt')
print((str(words_read)) + " words read in " + str(dt) + " seconds ")
os.system('cat data.txt; rm data.txt')

# Now Encrypt all the words and measure entropy
print("Beginning Entropy Analysis. Starting With SHA")
shaT = time.time()
os.system('cd BigData/words; ls | while read line;'
          'do python fasthash.py $line sha; done')
os.system('clear')
Tsha256 = time.time() - shaT
print(str(words_read)+" Words Encrypted with SHA-256 in "+str(Tsha256)+" seconds")
# Now Do MD5
md5T = time.time()
os.system('cd BigData/words; ls | while read line;'
          'do python fasthash.py $line md5; done')
os.system('clear')
Tmd5 = time.time() - md5T
print(str(words_read)+" Words Encrypted with MD-5 in "+str(Tmd5)+" seconds")
sha5T = time.time()
os.system('cd BigData/words; ls | while read line;'
          'do python fasthash.py $line sha512; done')
os.system('clear')
print(str(words_read)+" Words Encrypted with SHA-512 in "+str(time.time() - sha5T)+" seconds")
Thex = time.time()
os.system('cd BigData/words; ls | while read line;'
          'do python fasthash.py $line hex; done')
os.system('clear')
print(str(words_read)+" Words Encoded with HEX in "+str(time.time() - Thex)+" seconds")

# print("Processing entropy of "+str(len(dataHEX))+" hex objects")
# print("Processing the entropy of "+str(len(dataMD5))+" MD5 objects")
# print("Processing the entropy of "+str(len(dataSHA256))+" SHA-256 objects")
# print("Processing the entropy of "+str(len(dataSHA512))+" SHA-512 objects")

# Clean up the redundant text files created above for the program
os.system('cd BigData/words; rm hex.txt sha256.txt md5.txt sha512.txt')
