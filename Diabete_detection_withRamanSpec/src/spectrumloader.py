import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.model_selection import train_test_split
from BaselineRemoval import BaselineRemoval
from sklearn.preprocessing import MinMaxScaler, StandardScaler


PLT = '/root/projects/ProjectAug22/CP/Diabete_detection_withRamanSpec/dataset/'
'''This function take path to dataset directory as input and return pandas of std or validation compound spectrum and list of pandas dataF
to get the data use std,data_all = read_file('SOME_PATH')
'''
def read_file(PLT):
    standard = pd.read_csv(PLT+'AGEs.csv')
    samp_thumb = pd.read_csv(PLT+'thumbNail.csv')
    samp_earl = pd.read_csv(PLT+'earLobe.csv')
    samp_inarm = pd.read_csv(PLT+'innerArm.csv')
    samp_vein = pd.read_csv(PLT+'vein.csv')
    return standard,[samp_thumb,samp_earl,samp_inarm,samp_vein]

def cut_tonumpy(alldataf):
    Xs = []
    ys = []

    for each_df in alldataf:
        # print(each_df.head())
        n = each_df[1:].to_numpy()
        m = n[:,2:].astype(float)
        X = m[:,800:1800]
        Xs.append(X)
        y = each_df.has_DM2.to_numpy()[1:]
        ys.append(y)
        all_Xsample = m
    return Xs,ys,all_Xsample
    
def split_train_test(Xs,ys):
    seed_rand = 112
    X_train0, X_test0, y_train0, y_test0 = train_test_split( Xs[0], ys[0], test_size=0.2, random_state=seed_rand)
    X_train1, X_test1, y_train1, y_test1 = train_test_split( Xs[1], ys[1], test_size=0.2, random_state=seed_rand)
    X_train2, X_test2, y_train2, y_test2 = train_test_split( Xs[2], ys[2], test_size=0.2, random_state=seed_rand)
    X_train3, X_test3, y_train3, y_test3 = train_test_split( Xs[3], ys[3], test_size=0.2, random_state=seed_rand)
    return [X_train0,X_train1,X_train2,X_train3],[X_test0,X_test1,X_test2,X_test3],[y_train0,y_train1,y_train2,y_train3],[y_test0,y_test1,y_test2,y_test3]


def fluoresence_removal(datalist_toremove):
    X_train_VR = []
    for X_each_type in datalist_toremove:
        X_train_each = []
        for each_train in X_each_type:
            baseObj = BaselineRemoval(each_train)
            X_train_each.append(baseObj.ZhangFit())
        X_train_each = np.array(X_train_each)
        X_train_VR.append(X_train_each)
    return X_train_VR


# PREPROCESS = True
# FITBYSPECTRUM = True
# MINMX = True
# 'X_trainall' # data without fluoresence removing
# 'X_train_VR' # data with fluoresence removing



def seting_normalized_fuoresence_smoothing(fitbyspectrum,minmax,X_train_All):
    if minmax:
        sc0 = MinMaxScaler()
        sc1 = MinMaxScaler()
        sc2 = MinMaxScaler()
        sc3 = MinMaxScaler()
    else:
        sc0 = StandardScaler()
        sc1 = StandardScaler()
        sc2 = StandardScaler()
        sc3 = StandardScaler()
# if PREPROCESS:
    X_train0,X_train1,X_train2,X_train3 = X_train_All
# else :
#     X_train0,X_train1,X_train2,X_train3 = X_trainall

    if fitbyspectrum:
        X_train0_std = sc0.fit_transform(X_train0.T).T
        X_train1_std = sc1.fit_transform(X_train1.T).T
        X_train2_std = sc2.fit_transform(X_train2.T).T
        X_train3_std = sc3.fit_transform(X_train3.T).T
    else:
        X_train0_std = sc0.fit_transform(X_train0)
        X_train1_std = sc1.fit_transform(X_train1)
        X_train2_std = sc2.fit_transform(X_train2)
        X_train3_std = sc3.fit_transform(X_train3)
    
    return X_train0_std,X_train1_std,X_train2_std,X_train3_std,[sc0,sc1,sc2,sc3]



    