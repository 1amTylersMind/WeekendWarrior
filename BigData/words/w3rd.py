import sys, hashlib


def main():
    if(len(sys.argv)>2):
        fname = sys.argv[1]+" "+sys.argv[2]
        f = open(fname,'r')
        words = list()
        for word in f.readlines():
            words.append(word)
        print(str(len(words))+" "+sys.argv[1]+" words found")


if __name__ == '__main__':
    main()
