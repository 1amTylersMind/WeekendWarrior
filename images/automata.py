import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.ndimage as ndi


class CheckerMachine:
    W = 0
    H = 0
    white = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=int)
    black = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=int)
    checkerLH = np.concatenate((np.concatenate((white, black, white), 0),np.concatenate((black, white, black), 0)), 1)
    checkerRH = np.concatenate((np.concatenate((black, white, black), 0),np.concatenate((white, black, white), 0)), 1)
    Checker0 = np.concatenate((checkerLH,checkerRH),1)
    Checker1 = np.concatenate((checkerRH,checkerLH),1)
    Check = np.concatenate((Checker0,Checker1),0)
    Ch3ck = np.concatenate((Checker1,Checker0),0)
    CHECK = np.concatenate((Check,Ch3ck),1)
    CH3CK = np.concatenate((np.concatenate((Ch3ck,Check),1),np.concatenate((Check,Ch3ck),1)),0)
    CH33CK = np.concatenate((np.concatenate((Check, Ch3ck), 1),np.concatenate((Ch3ck, Check), 1)), 0)
    Checkerlib = [white, black, checkerRH, checkerLH, Checker0 ,Checker1, Check, Check, Ch3ck, CHECK,CH3CK,CH33CK]

    def __init__(self,matrix):
        self.W = matrix.shape[0]
        self.H = matrix.shape[1]

        # self.animate_Checkers(self.Checkerlib)
        self.animate_cell_library()

    def animate_Checkers(self,shapes):
        images = []
        i0 = np.concatenate((np.concatenate((self.white,self.black,self.white,self.black),0),
             np.concatenate((self.black,self.white,self.black,self.white),0)),1)

        images.append(plt.imshow(i0,'gray'))

        fig = plt.figure()
        ani = animation.ArtistAnimation(fig,images,interval=300,
                                        blit=True,repeat_delay=1000)
        plt.show()

    def animate_cell_library(self):
        f = plt.figure()
        plt.title('Checker Crawler')
        shapes = []
        for im in self.Checkerlib:
            img = plt.imshow(im,'gray',animated=True)
            shapes.append([img])
           # shapes.append([self.edge_convolve(im)])
        ani = animation.ArtistAnimation(f,shapes,interval=300,
                                        blit=True, repeat_delay=1000)
        plt.show()

    def edge_convolve(self,image):
        image = image.astype(float) / 255
        mask = np.array([[0,1,0],[1,0,1],[0,1,0]])
        edges = ndi.convolve(image,mask)
        # plt.imshow(edges)
        # plt.show()
        return edges




def main():
    CheckerMachine(np.zeros((400,400),dtype=int))


if __name__ == '__main__':
    main()
