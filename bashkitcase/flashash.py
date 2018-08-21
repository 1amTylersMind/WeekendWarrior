import hashlib, sys, os, time

def usage():
    print("Incorrect Usage!")

def main():
    if len(sys.argv) < 2:
        usage()
    else:
        Mode = sys.argv[1].split('-')[1]
        clear = sys.argv[2]
        CipherOps = {'sha':'SHA-256',"md5":'MD5'}

        print("Encrypting cleartext with "+Mode)

        if Mode == 'sha':
            digest = hashlib.sha256(clear).hexdigest()
            print(digest)
        if Mode == 'md5':
            digest = hashlib.md5(clear).hexdigest()
            print(digest)


if __name__ == '__main__':
    main()
