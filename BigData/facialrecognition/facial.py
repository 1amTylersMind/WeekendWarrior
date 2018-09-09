import sys, os, time, numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi


def ImagePipeLine():
    os.system('clear')
    start = time.time()
    print "# Opening Female Face Images"

    os.system('cd female;  dir=$PWD;ls | while read line; '
              'do ls $dir"/"$line | while read img; do echo $PWD/$img >> faces.txt;done; done ; ')

    femaleImgs = []
    for femface in open('female/faces.txt', 'r').readlines():
        femaleImgs.append(femface)
    print "Found " + str(len(femaleImgs)) + " images found"

    print "# Opening Male Face Images"
    os.system('cd male; dir=$PWD; ls | while read line;'
              'do ls $dir"/"$line | while read img; do echo $PWD/$img >> faces.txt; done; done ; ')

    maleImgs = []
    for maleface in open('male/faces.txt', 'r').readlines():
        maleImgs.append(maleface)
    print "Found " + str(len(maleImgs)) + " images found"

    print "# Opening Male Staff Face Images"

    os.system('cd malestaff; dir=$PWD; ls | while read line;'
              'do ls $dir"/"$line | while read img; do echo $PWD/$img >> faces.txt; done; done ; ')
    malestaffImgs = []
    for staff in open('malestaff/faces.txt', 'r').readlines():
        malestaffImgs.append(staff)
    print "Found "+str(len(malestaffImgs))+" images found "

    os.system('rm female/faces.txt male/faces.txt malestaff/faces.txt')
    TotalNImages = len(malestaffImgs) + len(maleImgs) + len(femaleImgs)
    print "------------------------------------------------------------"
    print "Total Images Found: " + str(TotalNImages)
    print "Time Elapsed: " + str(time.time() - start)+" seconds "
    return femaleImgs, maleImgs, malestaffImgs, TotalNImages


def main():
    fmimlist, mimlist, msimlist, nimgs = ImagePipeLine()


if __name__ == '__main__':
    main()
