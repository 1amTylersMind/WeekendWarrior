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
# ######################## PROCESSING HASH ENTROPY ######################## #

print("Processing entropy of "+str(words_read)+" hex objects")
hexAnal = time.time()
os.system('cd BigData/words; python EntropyAnalysis.py hex hex.txt')
print "Hex Analysis finished in "+str(time.time() - hexAnal)

print("Processing the entropy of "+str(words_read)+" MD5 objects")
md5Anal = time.time()
os.system('cd BigData/words; python EntropyAnalysis.py md5 md5.text')
print "MD5 Analysis finished in "+str(time.time() - md5Anal)

print("Processing the entropy of "+str(words_read)+" SHA-256 objects")
sha256Anal = time.time()
os.system('cd BigData/words; python EntropyAnalysis.py sha256 sha256.txt')
print "SHA-256 Analysis finished in "+str(time.time() - sha256Anal)

print("Processing the entropy of "+str(words_read)+" SHA-512 objects")
sha512Anal = time.time()
os.system(' cd BigData/words; python EntropyAnalysis.py sha512 sha512.txt')
print "SHA-512 Analysis finished in "+str(time.time() - sha512Anal)

# Clean up the redundant text files created above for the program
# os.system('cd BigData/words; rm hex.txt sha256.txt md5.txt sha512.txt')
