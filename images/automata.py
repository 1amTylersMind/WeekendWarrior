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
        # ani.save('CheckerCrawler.gif')

    def edge_convolve(self,image):
        image = image.astype(float) / 255
        mask = np.array([[0,1,0],[1,0,1],[0,1,0]])
        edges = ndi.convolve(image,mask)
        # plt.imshow(edges)
        # plt.show()
        return edges


class StateMachine:
    W = 0
    H = 0
    STATE = [[]]
    StateData = []
    N = 0

    def __init__(self, width, height):
        self.W = width
        self.H = height
        self.STATE = np.ones((width, height),dtype=int)
        # Now try another style of automata

    def test_transfrom(self, nFrames,style,flag):
        self.StateData.append(self.STATE)
        for i in range(nFrames):
            self.STATE = self.transform(style,flag)
            self.StateData.append(self.STATE)
            self.N = i
        self.animate_State_Data()

    def animate_State_Data(self):
        f = plt.figure()
        states = []
        for state in self.StateData:
            img = plt.imshow(state,'gray',animated=True)
            states.append([img])
        ani = animation.ArtistAnimation(f,states,interval=300,
                                        blit=True,repeat_delay=3000)
        plt.show()

    def transform(self, style, flag):
        flatstate = self.STATE.flatten()
        for i in range(len(flatstate)):
            e = flatstate[i]
            if style == 'diag':
                # Now for future states
                if self.N % 2 == 0:
                    if e == 1:
                        if i % 2 == 0:
                            flatstate[i] = 1
                        else:
                            if i % 3 == 1:
                                flatstate[i] = 1
                if self.N % 2 == 1:
                    if e == 1:
                        if i % 2 == 0:
                            flatstate[i] = 0
                        else:
                            if i % 3 == 1:
                                flatstate[i] = 0

            if style == 'fractal':
                avg = np.cumsum(flatstate[0:i])
                flatstate[i] = avg

            # One type of automata evolution style that inverts current state
            if self.N>2 and flag == 'flip':
                if e == 1:
                    flatstate[i] = 0
                else:
                    flatstate[i] = 1




        return flatstate.reshape((self.W, self.H))

    def flip_state(self):
        flatmat = self.STATE.flatten()
        for i in range(len(flatmat)):
            e = flatmat[i]
            if e == 0:
                flatmat[i] = 1
            else:
                flatmat[i] = 0
        self.STATE = flatmat.reshape((self.W,self.H))



def main():
    CheckerMachine(np.zeros((400,400),dtype=int))
    # Ok, that was fun. Now for something more flexible
    automata = StateMachine(25,25)
    automata.test_transfrom(20,'diag','flip')

if __name__ == '__main__':
    main()
