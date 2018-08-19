from skimage import io
from skimage import color
from scipy import ndimage as ndi
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def load_sample_image(arg):
    pictures = {'coins':'https://raw.githubusercontent.com/scikit-image/scikit-image/'
                        'v0.10.1/skimage/data/coins.png',
                'astronaut':'https://raw.githubusercontent.com/scikit-image/scikit-image/'
                        'master/skimage/data/astronaut.png'}
    for name in pictures.keys():
        if arg == name:
            pic = io.imread(pictures[name])
            #plt.imshow(pic,'gray')
            #plt.show()
            return pic


def mask_overlay(image,x1,x2,y1,y2,maskvec):
    img_sq = np.copy(image)
    img_sq[x1:x2,y1:y2] = maskvec
    plt.imshow(img_sq)
    plt.show()
    return img_sq


def grid_overlay(image, spacing):
    """
    grid_overlay takes an image and superimposes a blue
    cartesian grid over it.
    :param iamge:
    :param spacing:
    :return:
    """
    gridded = np.copy(image)
    for x in range(0,image.shape[0],int(image.shape[0]/spacing)):
        gridded[x,:] = [0,0,255]
    for y in range(0, image.shape[1], int(image.shape[1] / spacing)):
        gridded[:,y] = [0,0,255]
    plt.title('Grid Spacing = '+str(spacing))
    plt.imshow(gridded)
    plt.show()
    return gridded


def guassian_kernel(size, sigma):
    """

    :param size:
    :param sigma:
    :return:
    """
    positions = np.arange(size) - size//2
    kernel_raw = np.exp(-positions**2/(2*sigma**2))
    kernal_norm = kernel_raw/np.sum(kernel_raw)
    return kernal_norm


def guassian_convolution(diff, sig):
    """

    :param diff:
    :param sig:
    :return:
    """
    smooth_diff = ndi.convolve(guassian_kernel(25,3),diff)
    sdsig = ndi.convolve(sig,smooth_diff)
    plt.plot(smooth_diff)
    plt.title('Smoothened Difference')
    plt.show()
    plt.plot(sdsig)
    plt.title('Filted Signal')
    plt.show()
    return smooth_diff, sdsig


def filter_testing():
    """

    :return:
    """
    # Create virtual signal
    sig = np.zeros(100, np.float)
    # Add any Digital ONs to signal
    sig[30:60] = 1
    fig, ax = plt.subplots()
    ax.plot(sig)
    ax.set_ylim(-0.1,1.1)

    sigdelta = sig[1:] # setting up a differential
    sigdiff = sigdelta - sig[:1]
    sigon = np.clip(sigdiff, 0, np.inf)
    ax.plot(sigon)
    ax.set_ylim(-0.1,1.1)
    plt.title('Timing Difference Creates a signal')
    plt.show()

    diff = np.array([1, 0, -1])
    dsig = ndi.convolve(sig,diff)
    plt.plot(dsig)
    plt.title("Conv. of the Difference Signal ")
    plt.show()

    np.random.seed(0)
    sig = sig+np.random.normal(0, 0.3, size = sig.shape)
    plt.title('Adding noise to create Virtual Signal')
    plt.plot(sig)
    plt.show()
    plt.title('Signal')
    plt.plot(ndi.convolve(sig,diff))
    plt.show()

    # Now run this through the Gaussian-Convolution Filter
    guassian_convolution(diff,sig)
    return diff, sig


def edge_filter(img):
    mat = img.astype(float) / 255
    diff2d = np.array([[0, 1, 0],[1, 0, -1],[0 -1, 0]])
    mat_edges = ndi.convolve(mat,diff2d)
    io.imshow(mat_edges)
    return mat, mat_edges


def reduce_xaxis_labels(ax, factor):
    plt.setp(ax.xaxis.get_ticklabels(),visible=False)
    for label in ax.xaxis.get_ticklabels()[::factor]:
        label.set_visible(True)


def edge_filter_sobel(img):

    hdiff = np.array([[1], [0], [-1]])

    hsobel = np.array([[1,  2, 1],
                       [0,  0, 0],
                       [-1,-2,-1]])
    vsobel = hsobel.T

    img_h = ndi.convolve(img, hsobel)
    img_v = ndi.convolve(img, vsobel)

    fig, axes = plt.subplots(nrows=1,ncols=2)
    axes[0].imshow(img_h,cmap='gray')
    axes[1].imshow(img_v,cmap='gray')
    for ax in axes:
        reduce_xaxis_labels(ax,2)
    plt.show()
    img_sobel = np.sqrt(img_h**2 + img_v**2)
    # Hmmm... Some Error I Need to fix with this TODO
    # plt.imshow(img_sobel, cmap='gray')
    # plt.show()
    return img_sobel


def main():
    # Just some Test Images to play with
    test_pic_coins = load_sample_image('coins')
    test_pic_astro = load_sample_image('astronaut')

    ''' Add a Mask to a specified area of an image, with specified color'''
    # mask_overlay(test_pic_astro,50,100,50,100,[0, 255, 0])

    ''' Add a grid with a given spacing over the image'''
    #grid_overlay(test_pic_astro,100)

    ''' An Example of how to use python to filter noisy images '''
    # Now testing some filtering function
    #filter_testing()

    ''' 2D Image Filters: Edge Detection '''
    # The Edge detection isnt working right now
    # edge_filter(test_pic_coins)
    edge_filter_sobel(test_pic_coins)


if __name__ == '__main__':
    main()
