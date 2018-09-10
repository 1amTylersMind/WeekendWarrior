import sys,os,time, numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.ndimage as ndi
"""
Assuming sample size of audio is 44100khz, 
"""


def color_examples(seed):
    img_test = ndi.convolve(seed, np.ones((3, 3)), origin=0)

    plt.imshow(img_test, 'flag')
    plt.title('flag')
    plt.show()

    plt.imshow(img_test, 'prism')
    plt.title('prism')
    plt.show()

    plt.imshow(img_test, 'hsv')
    plt.title('hsv')
    plt.show()

    plt.imshow(img_test, 'gnuplot')
    plt.title('gnunplot')
    plt.show()

    plt.imshow(img_test, 'jet')
    plt.title('jet')
    plt.show()

    plt.imshow(img_test, 'hot')
    plt.title('hot')
    plt.show()


def handle_args(args):
    if '-ex' in args:
        color_examples(np.random.rand(400).reshape((20,20)))


def usage():
    print "Incorrect Usage! "
    # add suggestions as they're developed

def main():
    if len(sys.argv)<2:
        usage()
    else:
        handle_args(sys.argv)


if __name__ == '__main__':
    main()


