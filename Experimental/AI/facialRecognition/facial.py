import sys, os, time, numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi


class Face:
    path = ''
    dimsx = 0
    dimsy = 0

    def __init__(self, path,dirname,flags):
        self.path = path
        self.getFace(dirname,flags)

    def getFace(self,dirname,FLAG):
        if dirname != 'staff':
            os.system('find -name ' + self.path.replace('\n', '').split(dirname)[1].replace('/', '') + ' >> target.txt')
            fname = open('target.txt', 'r').readlines().pop().replace('\n', '')

            imat = plt.imread(fname)
            dims = imat.shape
            self.dimsx = dims[0]
            self.dimsy = dims[1]
            """
            Assigning Weights from Images:
            
            """
            if FLAG:
                plt.imshow(imat)
                plt.show()

        else:
            os.system('find -name ' + self.path.replace('\n', '').replace('/', '') + ' >> target.txt')
            fname = open('target.txt', 'r').readlines().pop().replace('\n', '')

            imat = plt.imread(fname)
            dims = imat.shape
            self.dimsx = dims[0]
            self.dimsy = dims[1]



    @staticmethod
    def assignWeights(imat):
        matrixout = np.array((imat.shape), dtype=int)
        return matrixout

def ImagePipeLine():
    """

    :return:
    """
    os.system('clear')
    start = time.time()
    print "# Opening Female Face Images"

    os.system('cd female;  dir=$PWD;ls | while read line; '
              'do ls $dir"/"$line | while read img; do echo $PWD/$img >> faces.txt;done; done ; ')

    femaleImgs = []
    for femface in open('female/faces.txt', 'r').readlines():
        femaleImgs.append(femface)
    print "[*] " + str(len(femaleImgs)) + " images found"

    print "# Opening Male Face Images"
    os.system('cd male; dir=$PWD; ls | while read line;'
              'do ls $dir"/"$line | while read img; do echo $PWD/$img >> faces.txt; done; done ; ')

    maleImgs = []
    for maleface in open('male/faces.txt', 'r').readlines():
        maleImgs.append(maleface)
    print "[*] " + str(len(maleImgs)) + " images found"

    print "# Opening Male Staff Face Images"

    os.system('cd malestaff; dir=$PWD; ls | while read line;'
              'do ls $dir"/"$line | while read img; do echo $PWD/$img >> faces.txt; done; done ; ')
    malestaffImgs = []
    for staff in open('malestaff/faces.txt', 'r').readlines():
        malestaffImgs.append(staff)
    print "[*] "+str(len(malestaffImgs))+" images found "

    # To test how the weights are assigned try out the faceWeightAssignment on last image indexed


    os.system('rm female/faces.txt male/faces.txt malestaff/faces.txt')
    TotalNImages = len(malestaffImgs) + len(maleImgs) + len(femaleImgs)
    print "------------------------------------------------------------"
    print "Total Images Found: " + str(TotalNImages)
    print "Time Elapsed: " + str(time.time() - start)+" seconds "
    return femaleImgs, maleImgs, malestaffImgs, TotalNImages


def extractFacesFromListData(fmimlist,mimlist,msimlist):
    """
    
    :param fmimlist: 
    :param mimlist: 
    :param msimlist: 
    :param nimgs: 
    :return: 
    """
    FACES = {}
    II = 0
    start = time.time()
    n_female_faces = 0
    for f4ce in fmimlist:
        try:
            FACES[II] = Face(f4ce, "female",False)
            II += 1
            n_female_faces += 1
            # if II == 415:
            #     Face(f4ce,'female',True)
        except:
            pass

    n_male_faces = 0
    print str(n_female_faces) + " Images of Female Student faces indexed."
    for face in msimlist:
        try:
            FACES[II] = Face(face, "male",False)
            II += 1
            n_male_faces += 1
        except:
            pass

    print str(n_male_faces) + " Images of Male Student faces indexed."
    nmale_staff = 0

    for fac3 in mimlist:
        FACES[II] = Face(fac3, "staff",False)
        II += 1
        nmale_staff += 1

    print str(nmale_staff) + " Images of Male Staff faces indexed."
    print "Finished Indexing  " + str(II) + " faces in " \
          + str(time.time() - start) + " seconds "
    print "------------------------------------------------------------"
    os.system('rm target.txt')
    return FACES

def getWorkingDirectory():
    os.system('pwd >> dir.txt')
    workingdir = open('dir.txt','r').readlines().pop().replace('\n','')
    os.system('rm dir.txt')
    return workingdir

def main():

    workingdir = getWorkingDirectory()

    fmimlist, mimlist, msimlist, nimgs = ImagePipeLine()
    FaceLib = extractFacesFromListData(fmimlist,mimlist,msimlist)

    print "Working Directory:" + workingdir
    folders = ['female', 'male', 'malestaff']
    # Process an individual image like this

    print "\t** Starting Image Processing on " +str(nimgs) + " Images **"
    print "------------------------------------------------------------"
    start = time.time()
    nFacesProcessed = 0
    nFacesDropped = 0
    for i in FaceLib.keys():
        try:
            picpath = FaceLib[i].path.split(workingdir)[1]
            if picpath.split('/')[1].split('/')[0] in folders:
                path = workingdir + '/' + picpath.split('/')[1].split('/')[0]
                img = FaceLib[1].path.split(path)[1].replace('\n', '').replace('/', '')
                os.system('find -name ' + img + ' >> imgpath.txt')
                ipath = open('imgpath.txt', 'r').readlines().pop().replace('\n', '')
                os.system('rm imgpath.txt; python frex.py ' + ipath)
                nFacesProcessed += 1
        except IndexError:
            nFacesDropped += 1
    print str(nFacesProcessed) + " Faces Run Through Image Processing in "\
          + str(time.time()-start) + " seconds"
    print '['+str(nFacesDropped)+' faces could not be found...]'


if __name__ == '__main__':
    main()
