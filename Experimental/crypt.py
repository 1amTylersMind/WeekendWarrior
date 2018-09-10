import hashlib, sys, os, time
from itertools import permutations, combinations, compress


class CuriousCounter:
    alpha = ["a", "b", "c", "d", "e",
             "f", "g", "h", "i", "j",
             "k", "l", "m", "n", "o",
             "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y",
             "z"]

    Alpha = ["A", "B", "C", "D", "E",
             "F", "G", "H", "I", "J",
             "K", "L", "M", "N", "O",
             "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y",
             "Z"]

    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    special = ["~","`","!","@","#","$","%","^","&","*","(",")"
        ,"-","_","=","+","[","{","]","}","\\","|",";",":","'",
        ",","<",".",">","/","?"]
    CharLib = {}

    def __init__(self,TargetString):
        index = 0
        for string in self.alpha:
            self.CharLib[index] = string
            index += 1
        for letter in self.Alpha:
            self.CharLib[index] = letter
            index += 1
        for num in self.nums:
            self.CharLib[index] = num
            index += 1
        for thing in self.special:
            self.CharLib[index] = thing
            index += 1
        # I didn't realize all string characters are 1 byte each
        # In both utf-8 or ascii!?
        self.N = self.CRACK(TargetString)

    def CRACK(self, target):
        start = time.time()
        length = len(list(target))
        N = 0
        for string in permutations(self.alpha, length):
            N += 1
            if target == ''.join(string):
                print "FOUND TARGET:\n" + ''.join(string)+" ["+str(time.time() - start)+"s]"
                return str(time.time() - start)
        print "This one is tricky. Give me more time!"
        for guess in permutations(self.CharLib.values(), length):
            if target == ''.join(guess):
                print "FOUND TARGET:\n" + ''.join(guess)+" ["+str(time.time() - start)+"s]"
                return N


def stringList2Bytes(text):
    UTF_counts = {}
    for element in text:
        UTF_counts[str2bytesUTF(element)] = element
    ASCII_counts = {}
    for indice in text:
        ASCII_counts[str2bytesASCII(indice)] = text
    return UTF_counts, ASCII_counts


def str2bytesUTF(text):
    return len(text.encode('utf-8'))


def str2bytesASCII(text):
    return len(text.encode('ascii'))


def main():
    print('# This will work for any word without repeated letters')
    print('# The time increases exponentially with word length')
    print("For Example:\n")
    print("zen [0.00228500366211s]")
    print("leak [0.0238671302795s]")
    print("worms [0.858510017395s]")
    print("random [14.2917180061s]")
    print("zfdsae [21.243997097s]")

    N3 = CuriousCounter('zen')
    N4 = CuriousCounter('leak')
    N5 = CuriousCounter('worms')
    N6 = CuriousCounter('random')
    n6 = CuriousCounter('zfdsae')
    N7 = CuriousCounter('longest')
    # N8 = CuriousCounter('practice')
    print(str(N3+N4+N5+N6+n6+N7+n7)+" Guesses Made in Total.")


if __name__ == '__main__':
    main()
