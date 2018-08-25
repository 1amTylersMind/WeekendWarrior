import numpy as np, sys, os, hashlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.io as io
from scipy.misc import imsave
import scipy.ndimage as ndi


class ImageProcessor:

    MODE = -1
    width = 0
    height = 0

    def __init__(self, opt):

        if opt == 'create':
            iMatrix = self.create_image()
            print str(len(iMatrix))+" frames of " + \
                str(self.width)+'x'+str(self.height)

    def create_image(self):
        self.width = int(input('Enter Image Width: '))
        self.height = int(input('Enter Image Height: '))

        # Display the type of images that can be created
        selection = self.display_creation_menu()

        # Handling the random image sequence option first
        if selection == 'random':
            fig = plt.figure()
            plt.title(str(self.width)+'x'+str(self.height)+' Random Seed ')
            imgs = []
            for i in range(int(self.width*self.height)):
                randomMatrix = \
                    self.spawn_random_image(self.width, self.height)
                randImg = plt.imshow(randomMatrix,'gray',animated=True)
                imgs.append([randImg])

            ani = animation.ArtistAnimation(fig,imgs,interval=30,
                                            blit=True,repeat_delay=1000)
            plt.show()
            ani.save('random.gif',dpi=80,writer='imagemagick')
            return imgs

        # Handling the visual crypto option next
        if selection == 'crypto':
            fig = plt.figure()
            ims = []


    @staticmethod
    def spawn_random_image(W, H):
        matrix = np.ones((W, H)).flatten()
        seed = np.random.randn((W*H))
        matrix = np.array((matrix*seed/255).reshape((W, H)))
        return matrix

    @staticmethod
    def display_creation_menu():
        print " [1] 'random' "
        print " [2] 'crypto' "
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
