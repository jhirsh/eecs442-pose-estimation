import numpy as np
from numpy.polynomial import Polynomial as P
import matplotlib.pyplot as plt 
from scipy.spatial import distance
import pandas as pd


norms = []
for j in [1,2,3]:
    key_points=np.load('body' + str(j) + '.npz')
    files = key_points.files
    for i in range(len(files) - 4):
        ###time0 frame####################################################
        file0 = 'time'+str(i)
        file1 = 'time'+str(i+1)
        file2 = 'time'+str(i+2)
        file3 = 'time'+str(i+3)

        # load times from npz file
        time0=key_points[file0]
        time1=key_points[file1]
        time2=key_points[file2]
        time3=key_points[file3]

        # extract x and y coordinates
        time0_x=time0[:,:,0]
        time0_y=time0[:,:,1]
        time0_xy=time0[:,:,0:2]
        time0_xy=np.reshape(time0_xy,(25,2))

        time1_x=time1[:,:,0]
        time1_y=time1[:,:,1]
        time1_xy=time1[:,:,0:2]
        time1_xy=np.reshape(time1_xy,(25,2))

        time2_x=time2[:,:,0]
        time2_y=time2[:,:,1]
        time2_xy=time2[:,:,0:2]
        time2_xy=np.reshape(time2_xy,(25,2))

        time3_xy=time3[:,:,0:2]
        time3_xy=np.reshape(time3_xy,(25,2))

        estimate = np.ndarray(shape=(25,2))
        ### Differential & estiamtion##################################################
        for k in range(0,24):
            p0 = time0_xy[k]
            p1 = time1_xy[k]
            p2 = time2_xy[k]
            x = [p0[0], p1[0], p2[0]]
            y = [p0[1], p1[1], p2[1]]
            #print(x, y)
            if x[0] == 0 or x[1] == 0 or x[2] == 0:
                estimate[k] = [0,0]
            else:
                z = np.polyfit(x,y,3)
                f = np.poly1d(z)
                dx = x[2] - x[1]
                x_n = x[2] + dx
                #print(x_n, f(x_n))
                estimate[k] = [x_n, f(x_n)] 
                print(estimate[k])
            plt.plot(x,y,'r+')
            for lin in np.linspace(x_n-10,x_n+10,50):
                plt.plot(lin,f(lin),'g+') 
            plt.plot(time3_xy[k][0], time3_xy[k][1], 'ro')
            plt.plot(estimate[k][0], estimate[k][1], 'b+')
            plt.show()
            '''
            '''

        norms.append(np.linalg.norm(estimate - time3_xy))

print(norms)
# Plot Histogram
fig, ax = plt.subplots()
n, bins, patches = ax.hist(norms, 10, facecolor='blue', alpha=0.5)
title = 'Histogram of Estimation Accuracy'
annotation = 'N = ' + str(len(norms))
ax.annotate(annotation, (max(norms)-300, 5))
ax.set_title(title)
ax.set_xlabel('Euclidean Norm between Estimation and Ground Truth (Pixels)')
ax.set_ylabel('Number of Estimations')

plt.show()
