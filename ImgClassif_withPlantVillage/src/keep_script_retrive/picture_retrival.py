from directory_retriever import retrive
import cv2
import numpy as np
import os
import sys
import pickle


def read_pic_from_path(path):
    directory_name = retrive(path)
    # mypath = [path+i for i in directory_name]
    list_of_img = []
    list_of_label = []
    # print(mypath)
    for i in directory_name:
        epath = path+i
        onlyfiles = [f for f in os.listdir(
            epath) if os.path.isfile(os.path.join(epath, f))]
        for ehfile in onlyfiles:
            pic_path = f'{epath}{os.sep}{ehfile}'
            img = cv2.imread(pic_path)
            if img is not None:
                list_of_img.append(img)
                list_of_label.append(i)
    if len(list_of_img) == len(list_of_label):
        listfile = open('leavesVillagePickle.atikeep', 'wb')
        pickle.dump((list_of_img, list_of_label), listfile)
        listfile.close()
        return (list_of_img, list_of_label)
    else:
        raise Exception('non equal')
     # GitHub user||student : AtiChetsurakul
    return


if __name__ == '__main__':
    read_pic_from_path(
        '/Volumes/ExternalSSDForMac/AITLecture/CSforDSAIAUG22/plantV_file/Plant_leave_diseases_dataset_with_augmentation/')
