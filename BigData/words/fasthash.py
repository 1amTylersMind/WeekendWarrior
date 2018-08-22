import sys, os, hashlib
"""
<<FAST_HASH>>
"""


def hasher(mode, text):
    if mode == 'sha256':
        return hashlib.sha256(text).hexdigest()
    if mode == 'md5':
        return hashlib.md5(text).hexdigest()
    if mode == 'sha1':
        return hashlib.sha384(text).hextdigest()
    if mode == 'sha3':
        return hashlib.sha512(text).hexdigest()
    if mode == 'hex':
        return text.encode('hex')


def main():
    opt = sys.argv[1]
    msg = sys.argv[2]
    print(hasher(opt,msg))


if __name__ == '__main__':
    main()