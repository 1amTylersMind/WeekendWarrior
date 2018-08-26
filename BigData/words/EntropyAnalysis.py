import sys, os, hashlib
import numpy as np, matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import stats


class EntropyAnalysis:
    modes = ['sha256','sha512','md5','hex']
    OptMode = ''
    freqdata = {}

    def __init__(self,opt,datastream):
        if opt in self.modes:
            self.OptMode = opt
        self.freqdata, freqSequence = self.count_letter_frequency(datastream)
        # Visualize the distribution of hashed character frequency
        data, fit = self.visualize_frequency(self.freqdata)
        # Now use the freqSequence to try and watch this distribution accumulate over time.
        # Want to compare how quickly they get 'flat'. and quantify at each step:
        #   [1] - How flat dist. is, (Slope of Bin counts in arbitrary order)
        #   [2] - How much did the flatness change since last hash, and what's the
        #   [3] - What's abs(max-min) of letter frequency values.

    def visualize_frequency(self,fdata):
        index = 0
        freqdata = {}
        freqmath = []
        for k in fdata.keys():
            freqdata[index] = fdata[k]
            freqmath.append(fdata[k])
            index += 1
        data = np.array(freqmath)
        Max = data.max()
        Min = data.min()
        err, offset, slope = stats.chi.fit(data)
        fit = {'slope': slope, 'offset': offset, 'error': err}
        print "Std.Dev. = " + str(data.std())
        print "Max-Min = " + str(data.max() - data.min())
        print "Mean Value of Counts: " + str(data.mean())
        print "Chi-Sq. Fit - Slope: " + str(fit['slope'])
        print "Error in Fit : " + str(fit['error'])

        # fig = plt.figure()
        hist = plt.bar(freqdata.keys(), freqdata.values(), color='g')
        plt.title(self.OptMode+' Letter Frequency')
        plt.xlabel('Character')
        plt.ylabel('N Counts')
        plt.axis([0, len(fdata.keys()), Min, Max + 10])
        plt.plot(data,color='r')
        plt.grid(True)
        plt.title(self.OptMode+' Letter Frequency')
        plt.show()


        plt.show()
        return data, fit

    def count_letter_frequency(self,data):
        bins = {'0':0,'1':0,'2':0,
                '3':0,'4':0,'5':0,
                '6':0,'7':0,'8':0,
                '9':0,'a':0,'b':0,'c':0,
                'd':0,'e':0,'f':0}
        binhistory = []
        for line in data:
            for element in list(line):
                if element in bins.keys():
                    bins[element] += 1
                    # Get the Slope of the hist(bins) at
                    # this instant!
                    binhistory.append(bins)
        return bins, binhistory


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
        EntropyAnalysis(cipher,hashes)

if __name__ == "__main__":
    main()
