
import os


def retrive(path):
    '''
    Retrive all path at given directory example 
    plantV_file/Plant_leave_diseases_dataset_with_augmentation/
    return directoryname
    '''
    path = path + '.'
    # print(os.listdir(path))
    listdr = os.listdir(path)
    # if '.DS_Store' in listdr:
    #     listdr.remove('.DS_Store')
    return listdr


def retrive_with_glob(path):
    '''
    NO MORE USE
    '''
    raise DeprecationWarning('please use retrive instead')
    # allpath = glob(path, recursive=True)
    # dir_name = []
    # for epath in allpath:
    #     dir_name.append(epath.split(os.sep))
    # print(dir_name)
    # return allpath, dir_name


if __name__ == '__main__':
    print(retrive(
        '/Volumes/ExternalSSDForMac/AITLecture/CSforDSAIAUG22/plantV_file/Plant_leave_diseases_dataset_with_augmentation/'))


'''
['Strawberry___healthy', 'Grape___Black_rot', 'Potato___Early_blight', 'Blueberry___healthy', 'Cherry___Powdery_mildew', 'Tomato___Target_Spot', '.DS_Store', 'Peach___healthy', 'Potato___Late_blight', 'Tomato___Late_blight', 'Tomato___Tomato_mosaic_virus', 'Pepper,_bell___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Tomato___Leaf_Mold', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Apple___Cedar_apple_rust', 'Tomato___Bacterial_spot', 'Grape___healthy', 'Corn___Cercospora_leaf_spot Gray_leaf_spot', 'Tomato___Early_blight', 'Grape___Esca_(Black_Measles)', 'Raspberry___healthy', 'Tomato___healthy', 'Corn___Northern_Leaf_Blight', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Cherry___healthy', 'Apple___Apple_scab', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Corn___Common_rust', 'Background_without_leaves', 'Peach___Bacterial_spot', 'Pepper,_bell___Bacterial_spot', 'Tomato___Septoria_leaf_spot', 'Corn___healthy', 'Squash___Powdery_mildew', 'Apple___Black_rot', 'Apple___healthy', 'Strawberry___Leaf_scorch', 'Potato___healthy', 'Soybean___healthy']

'''
