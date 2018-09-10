import sys, os, time, numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.ndimage as ndi


class Animator:

    @staticmethod
    def generate_seed_image(max,width,height):
        arr = np.random.randint(0,max,width*height).reshape(width,height)
        plt.imshow(arr,'gray')
        plt.title('Random Seed')
        plt.show()
        return arr

    @staticmethod
    def filter_testing(imat):
        f0 = [[0,1,0],[1,1,1],[0,1,0]]
        f1 = [[1,0,1],[0,1,0],[1,0,1]]
        i0 = ndi.convolve(imat,f0,origin=0)
        i1 = ndi.convolve(imat,f1,origin=0)
        return i0, i1

    @staticmethod
    def blur_image(imageMatrix):
        filter1 = [[1,1,1],[1,0,1],[1,1,1]]
        return ndi.convolve(imageMatrix,filter1,origin=0)

    @staticmethod
    def sharpen_image(imat,level):
        sharpfilter = [[-1,-1,-1],[-1,level,-1],[-1,-1,-1]]
        return ndi.convolve(imat,sharpfilter,origin=0)

    @staticmethod
    def animate_matrices(matrices,speed):
        print "Putting together animation of " + str(len(matrices)) + " Generations"
        start = time.time()
        imgs = []
        f = plt.figure()
        for matrix in matrices:
            i = plt.imshow(matrix,'gray')
            imgs.append([i])
        a = animation.ArtistAnimation(f,imgs,interval=speed,
                                      blit=True,repeat_delay=2000)
        print "Finished Rendering Animation in "+str(time.time() - start)+" seconds"
        plt.show()

    @staticmethod
    def render_matrices(matrices, speed, color):
        print "Putting together animation of " + str(len(matrices)) + " Generations"
        start = time.time()
        imgs = []
        f = plt.figure()
        for matrix in matrices:
            conv = ndi.convolve(matrices,np.ones((4,4)),color)
            i = plt.imshow(matrix, 'prism')
            imgs.append([i])
        a = animation.ArtistAnimation(f, imgs, interval=speed,
                                      blit=True, repeat_delay=2000)
        print "Finished Rendering Animation in " + str(time.time() - start) + " seconds"
        plt.show()

    @staticmethod
    def displayImage(imat,isColor,Name):
        if isColor:
            plt.imshow(imat)
            plt.title(Name)
            plt.show()
        else:
            plt.imshow(imat,'gray')
            plt.title(Name)
            plt.show()


''' --------------------------------------------AUTOMATA------------------------------------------- '''


class Automata:

    @staticmethod
    def LIFEmode(imat,nGen):
        n = 0
        Generations = []
        start = time.time()
        while n<nGen:
            imat = np.array(imat,dtype=int)
            neighbors = ndi.convolve(imat, [[1, 1, 1], [1, 0, 1], [1, 1, 1]], origin=0)
            for y in range(imat.shape[1]):
                for x in range(imat.shape[0]):
                    if imat[x, y] & (neighbors[x, y] > 3 or neighbors[x, y] < 2):
                        imat[x, y] = False
                    else:
                        if neighbors[x, y] == 3:
                            imat[x, y] = True
            Generations.append(np.array(imat,dtype=int))
            n += 1
        print "Finished Simulating "+str(n)+" Generations in "+str(time.time()-start)+"s"
        return Generations

    @staticmethod
    def simulateLife():
        width = int(input('Enter Width:'))
        height = int(input('Enter Height:'))
        nGen = int(input('Enter Number of Generations: '))
        time = int(input('Enter time scale for each generation in ms:'))
        seed = np.random.rand(width*height).reshape((width,height)) > 0.7

        Animator.animate_matrices(Automata.LIFEmode(seed,nGen),time)

    @staticmethod
    def NumericLifeAnimator(matrices, speed):
        start = time.time()
        f = plt.figure()
        images = []
        MAGIC = [[-1,-1,-1,-1,-1],[-1,-1,0,-1,-1],[-1,-1,-1,-1,-1]]
        for matrix in matrices:
            conv = ndi.convolve(matrix,MAGIC,origin=0)
            images.append([plt.imshow(conv,'hsv')])
        print "Finished rendering in "+str(time.time() - start)+" seconds"
        a = animation.ArtistAnimation(f,images,interval=speed,
                                      blit=True,repeat_delay=2000)
        plt.show()

'----------------------------------__EXPERIMENTAL_AUTOMATA__------------------------------------------'


class crawler:

    width = 0
    height = 0
    LifeSpan = 0

    def __init__(self):
        self.Matrix = self.initialize()

        plt.title('INITIAL STATE')
        plt.imshow(self.Matrix,'gray_r')
        plt.show()
        f = plt.figure()
        imgs = []
        for gen in range(self.LifeSpan):
            self.Matrix = self.start_crawling(self.Matrix)
            imgs.append([plt.imshow(self.Matrix,'gray_r')])
        a = animation.ArtistAnimation(f,imgs,interval=60,
                                      blit=True,repeat_delay=1000)
        plt.show()


    def initialize(self):
        self.width = int(input('Enter Width;'))
        self.height = int(input('Enter Height: '))
        self.LifeSpan = int(input('Enter N Generations to simulate: '))
        matrix = np.random.rand(self.width*self.height).reshape((self.width,self.height)) > .5
        matrix = np.array(matrix,dtype=int)
        return matrix

    def start_crawling(self,state):
        crawlfilt = [[0,1, 1,0],
                     [-1, 1, 1, -1],
                     [-1, 1, 1, -1],
                     [0,1, 1,0]]
        conv=ndi.convolve(state,crawlfilt,origin=0)
        for y in range(self.height):
            for x in range(self.width):
                if state[x,y] == 1 & conv[x,y]<=6 or conv[x,y]==1:
                    state[x,y] = 0
        return state


def main():
    if len(sys.argv) < 2:
        seed = Animator.generate_seed_image(255, 255, 255)
        blurred_seed = Animator.blur_image(seed)
        sharper_seed = Animator.sharpen_image(seed, 5)
        testFilter0, testFilter1 = Animator.filter_testing(seed)

        nGen = (input("How many Generations for Conway's Game of Life? (or 'custom'):\n"))
        if nGen == 'custom':
            Automata.simulateLife()
        else:
            nGen = int(nGen)
            conSeed = np.random.rand(32400).reshape((180, 180)) > 0.7

            print "Initializing Conway GOL [Special Image Filter]\n* " + \
                  str(nGen) + " Generations\n* Shape " + str(conSeed.shape)
            Animator.animate_matrices(Automata.LIFEmode(conSeed, nGen), 30)

        # If the user is still there, try running some more Automata!
        ans = str(input("Still There? [y/n]\n"))
        if ans == 'y' or ans == 'Y':
            print "OK, Buckle up Buckeroo! "
            conSeed = np.random.rand(32400).reshape((180, 180)) > 0.4
            Automata.NumericLifeAnimator(Automata.LIFEmode(conSeed, 1000), 30)
    else:
        opt = sys.argv[1]
        print opt
        if opt == 'custom':
            brick = np.zeros((10,10))
            cell = np.ones((10,10))
            row0 = np.concatenate((brick,cell,brick,cell,cell,brick),1)
            row2 = np.concatenate((cell,brick,cell,brick,cell,brick),1)
            Animator.animate_matrices(Automata.LIFEmode(np.concatenate((row0,row2),0),500),30)
            Animator.animate_matrices(Automata.LIFEmode(row2,500), 30)
            Animator.animate_matrices(Automata.LIFEmode(row0,500), 30)
        if opt == 'crawler':
            crawler()

if __name__ == '__main__':
    main()