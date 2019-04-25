import numpy as np
import matplotlib.pyplot as plt 
from scipy.spatial import distance
import pandas as pd


norms = []
count = 0
for j in [1,2,3]:
    key_points=np.load('body' + str(j) + '.npz')
    files = key_points.files
    count = 0
    for i in range(len(files) - 2):
        ###time0 frame####################################################
        file0 = 'time'+str(i)
        file1 = 'time'+str(i+1)                         
        file2 = 'time'+str(i+2)
        time0=key_points[file0]
        time0_x=time0[:,:,0]
        time0_y=time0[:,:,1]
        time0_xy=time0[:,:,0:2]
        time0_xy=np.reshape(time0_xy,(25,2))
        n=np.shape(time0_xy)

        ###time1 frame#################################################
        time1=key_points[file1]
        time1_xy=time1[:,:,0:2]
        time1_xy=np.reshape(time1_xy,(25,2))
        m=np.shape(time1_xy)
        time1_x=time1[:,:,0]
        time1_y=time1[:,:,1]

        ###Differential & estiamtion##################################################
        for k in range(0,25):
            dk_x=time1_x-time0_x
            dk_y=time1_y-time0_y

        dk=np.hstack((dk_x.T,dk_y.T))
        estimate=time1_xy+dk

        num=np.arange(25) #Used just for annotation
        time2=key_points[file2] #Actual pose in the next frame

        time2_xy=time2[:,:,0:2]
        count += 1
        # norms.append(np.linalg.norm(estimate - time2_xy))                 #Used for the plot w/o normalization                                                                                                          #Shifted here to handle the comment in the next line
        norms.append(np.linalg.norm(estimate - time2_xy)/count)             #Used for plot with Normalization


print(len(norms))
# norms2=norms/len(norms)
plt.hist(norms, 10, facecolor='blue', alpha=0.5)
plt.show()
