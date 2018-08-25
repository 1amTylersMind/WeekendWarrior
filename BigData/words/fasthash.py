import sys,os, hashlib


def main():
    if(len(sys.argv)>2 ):
        fname = sys.argv[1]+" "+sys.argv[2]
        try:
            if fname.split('.')[1] == '.txt' or fname.split('.')[1] == ',py':
                exit(code=0)
            f = open(fname, 'r')
            words = list()
            for word in f.readlines():
                words.append(word)
                if len(sys.argv) == 4:
                    cipher = sys.argv[3]
                    fname = sys.argv[1] + " " + sys.argv[2]
                    f = open(fname, 'r')
                    if cipher == 'sha':
                        crypt0 = hashlib.sha256(word).hexdigest()
                        os.system('echo ' + crypt0 + ' >> sha256.txt')
                    if cipher == 'md5':
                        crypt1 = hashlib.md5(word).hexdigest()
                        os.system('echo ' + crypt1 + ' >> md5.txt')
                    if cipher == 'hex':
                        os.system('echo ' + word.encode('hex') + '>> hex.txt')
                    if cipher == 'sha512':
                        os.system('echo ' + hashlib.sha512(word).hexdigest() + '>> sha512.txt')
            if (len(sys.argv) < 4):
                print(str(len(words)) + " " + sys.argv[1] + " words found")
            else:
                print(str(len(words)) + " " + sys.argv[1] + " words Encrypted with " + sys.argv[3].upper())
        except IOError or IndexError:
            pass


if __name__ == '__main__':
    main()
