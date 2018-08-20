import sys, os, time, numpy as np
import matplotlib.pyplot as plt
start = time.time()
os.system('cd BigData/words; ls | while read line; do python w3rd.py $line >> wordcount.txt; done')
os.system('cat $PWD/BigData/words/wordcount.txt >> data.txt; rm $PWD/BigData/words/wordcount.txt')
f = open('data.txt','r')
letters = []
N = []
Counts = {}
for line in f.readlines():
    N.append(int(line.split(' ')[0]))
    letters.append(line.split(' ')[1])
    Counts[line.split(' ')[1]] = line.split(' ')[0]
words_read = np.sum(np.array(N))

os.system('rm data.txt')
dt = time.time() - start
print((str(words_read)) +" Words read in "+str(dt)+" seconds ")

plt.bar(letters,N)
plt.show()