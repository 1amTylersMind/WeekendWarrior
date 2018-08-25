import numpy as np, sys, os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.misc import imsave


class ImageProcessor:

    MODE = -1

    def __init__(self, opt):

        if opt == 'create':
            iMatrix = self.create_image()
            print iMatrix.shape

    def create_image(self):
        width = int(input('Enter Image Width: '))
        height = int(input('Enter Image Height: '))
        # mat = np.zeros((width, height),dtype=int)
        # f = plt.figure()
        # plt.imshow(mat, 'gray')
        selection = self.display_creation_menu()
        if selection == 'random':
            fig = plt.figure()
            imgs = []
            for i in range(int(width*height)):
                randomMatrix = \
                    self.spawn_random_image(width, height)
                randImg = plt.imshow(randomMatrix,'gray',animated=True)
                imgs.append([randImg])

            # plt.imshow(randomMatrix, 'gray')
            # plt.show()
            ani = animation.ArtistAnimation(fig,imgs,interval=30,
                                            blit=True,repeat_delay=1000)
            plt.show()
        return mat

    @staticmethod
    def spawn_random_image(W, H):
        matrix = np.ones((W, H)).flatten()
        seed = np.random.randn((W*H))
        matrix = np.array((matrix*seed).reshape((W, H)))
        return matrix

    @staticmethod
    def display_creation_menu():
        print " [1] 'random' "
        print " [2] 'exotic' "
        print " [3] '3D-random' "
        return input(' Enter a selection: ')

    def sigmoid(self,x):
        return 1/(1+np.power(np.e, -1*x))


def usage():
    print " Incorrect Usage! "
    print " python ImageProcessor.py <mode> "
    print " <mode> : -create, -read, -random"


def main():
    menuOpts = {'-create': 1, '-read': 2, '-random': 3}
    if len(sys.argv) < 2:
        usage()
    else:
        opt = sys.argv[1]
        if opt in menuOpts.keys():
            print("Running " + opt.split('-')[1] + " Mode")
            ImageProcessor(opt.split('-')[1])

if __name__ == '__main__':
    main()
