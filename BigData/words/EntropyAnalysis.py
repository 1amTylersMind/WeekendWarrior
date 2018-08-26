import sys, os, hashlib
import numpy as np, matplotlib.pyplot as plt
import matplotlib.animation as animation
import sklearn as skl


def usage():
    print "Incorrect Usage!"
    print " python EntropyAnalysis.py <cipher> <data.txt> "
    print "Ciphers: SHA256, SHA512, MD5 or HEX Encoding"


def getFileContent(fname):
    data = []
    for line in open(fname,'r').readlines():
        data.append(line)
    return data


def main():
    if len(sys.argv) < 2:
        usage()
    else:
        cipher = sys.argv[1]
        fname = sys.argv[2]
        print "Analyzing "+cipher+" Entropy in file "+fname
        hashes = getFileContent(fname)
        print(str(len(hashes))+" Hashes Found")


if __name__ == "__main__":
    main()
