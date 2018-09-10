import sys, os, time, numpy as np
import scipy.spatial as space
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import scipy.ndimage as ndi


class FaceDetection:

    path = ''

    def __init__(self, pathToImage):
        self.path = pathToImage
        self.debug = True
        self.characterize()

    def visualizeFaceSeqments(self,matrices):
        f = plt.figure()
        imgs = []
        for matrix in matrices.values():
            imgs.append([plt.imshow(matrix,'gray_r')])
        a = animation.ArtistAnimation(f,imgs,interval=200,
                                      blit=True,repeat_delay=1000)
        plt.show()

    def characterize(self):
        imat = ndi.imread(self.path)
        dims = imat.shape
        avgpxl = imat.mean()
        min = imat.min()
        max = imat.max()

        quarters = {}
        x1 = int(dims[0]/4)
        y1 = int(dims[1]/4)
        # Top Row slices in four
        quarters[0] = imat[0:x1,0:y1]
        quarters[1] = imat[x1:2*x1,0:y1]
        quarters[2] = imat[2*x1:3*x1,0:y1]
        quarters[3] = imat[3*x1:dims[0],0:y1]
        # middle eight boxes
        quarters[4] = imat[0:x1,y1:2*y1]
        quarters[5] = imat[x1:2*x1,y1:2*y1]
        quarters[6] = imat[2*x1:3*x1,y1:2*y1]
        quarters[7] = imat[3*x1:dims[0],y1:2*y1]

        quarters[8] = imat[0:x1,2*y1:3*y1:]
        quarters[9] = imat[x1:2*x1,2*y1:3*y1]
        quarters[10]= imat[2*x1:3*x1,2*y1:3*y1]
        quarters[11]= imat[3*x1:dims[0],2*y1:3*y1]
        # Bottom 4 slices
        quarters[12]= imat[0:x1,3*y1:dims[1]]
        quarters[13]= imat[x1:2*x1,3*y1:dims[1]]
        quarters[14]= imat[2*x1:3*x1,3*y1:dims[1]]
        quarters[15]= imat[3*x1:dims[0],3*y1:dims[1]]

        self.visualizeFaceSeqments(quarters)


        # Give a printout while under development
        if self.debug:
            print "Dims:\t"+str(dims)
            print "Avg. Pixel Val:\t"+str(avgpxl)
            print "Min:\t" + str(min)
            print "Max:\t" + str(max)


def faceDetection(example_img,debug):
    """

    :param example_img:
    :param debug:
    :return:
    """
    imat = ndi.imread(example_img)
    avg = (imat[:, :, 0] / 3 + imat[:, :, 1] / 3 + imat[:, :, 2] / 3) / 3

    # Set up some filters
    edges = np.array([[1, 1, 1],
                      [0, 0, 0],
                      [-1, -2, -1]])

    spread = np.array([[1, 1,1],
                       [1,-3,1],
                       [1, 1,1]])

    blur = np.array([[-1, 1, -1],
                     [1, -2, 1],
                     [-1, 1, -1]])

    cross = np.array([[0,1,0],
                      [1,1,1],
                      [0,0,0]])

    feature0 = np.array([[1,1,0],[1,0,0],[1,0,0]])

    convR = ndi.convolve(imat[:, :, 0], edges)
    convG = ndi.convolve(imat[:, :, 1], edges)
    convB = ndi.convolve(imat[:, :, 2], edges)
    conv = ndi.convolve(avg, cross)
    e = ndi.convolve(avg, blur)
    convC = avg*ndi.fourier_gaussian(e,1)

    if debug:
        print "DIMS: " + str(imat.shape)
        print "MAX: " + str(imat.max())
        print "MIN: " + str(imat.min())
        print "MEAN: " + str(imat.mean())

        '''
        plt.title('Example Face')
        plt.imshow(imat)
        plt.show()
        
        print np.array(avg).shape
        plt.title('EigenFace 1')
        plt.imshow(conv, 'gray')
        plt.show()

        print "EigenFace 2"
        plt.title('Face Detection ? ')
        plt.imshow(conv - e / (avg + 4), 'gray_r')
        plt.show()

        plt.title('EigenFace 3')
        plt.imshow(convC,'gray_r')
        plt.show()
        
        '''
        f, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
        ax1.imshow(conv, 'gray_r')
        ax1.set_title('EigenFace 1')
        ax2.imshow(conv - e / (avg + 4), 'gray_r')
        ax2.set_title('EigenFace 2')
        ax3.imshow(convC,'gray')
        ax3.set_title('EigenFace 3')
        plt.show(f)

    return conv-e / (avg+4)


def main():
    if len(sys.argv) > 1:
        example_img = sys.argv[1]
        data = faceDetection(example_img,False)
    else:
        example_img = "/media/root/DB0/Experimental/AI/facialRecognition/female/elduns/elduns.1.jpg"
        # faceDetection(example_img,True)

        FaceDetection(example_img)


if __name__ == '__main__':
    main()
