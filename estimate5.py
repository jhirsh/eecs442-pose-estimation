import numpy as np
from numpy.polynomial import Polynomial as P
import matplotlib.pyplot as plt 
from scipy.spatial import distance
import pandas as pd


norms = []
for j in [1]:
    key_points=np.load('body' + str(j) + '.npz')
    files = key_points.files
    for i in range(len(files) - 6):
        ###time0 frame####################################################
        file0 = 'time'+str(i)
        file1 = 'time'+str(i+1)
        file2 = 'time'+str(i+2)
        file3 = 'time'+str(i+3)
        file4 = 'time'+str(i+4)
        file5 = 'time'+str(i+5)

        # load times from npz file
        time0=key_points[file0]
        time1=key_points[file1]
        time2=key_points[file2]
        time3=key_points[file3]
        time4=key_points[file4]
        time5=key_points[file5]

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

        time3_x=time3[:,:,0]
        time3_y=time3[:,:,1]
        time3_xy=time3[:,:,0:2]
        time3_xy=np.reshape(time3_xy,(25,2))

        time4_x=time4[:,:,0]
        time4_y=time4[:,:,1]
        time4_xy=time4[:,:,0:2]
        time4_xy=np.reshape(time4_xy,(25,2))

        time5_x=time5[:,:,0]
        time5_y=time5[:,:,1]
        time5_xy=time5[:,:,0:2]
        time5_xy=np.reshape(time5_xy,(25,2))

        estimate = np.ndarray(shape=(25,2))
        ### Differential & estiamtion##################################################
        norm = 0
        counted_norm = 0
        for k in range(0,24):
            p0 = time0_xy[k]
            p1 = time1_xy[k]
            p2 = time2_xy[k]
            p3 = time3_xy[k]
            p4 = time4_xy[k]
            x = []
            y = []
            order = -1
            if p0[0] != 0:
                x.append(p0[0])
                y.append(p0[1])
                order += 1
            if p1[0] != 0:
                x.append(p1[0])
                y.append(p1[1])
                order += 1
            if p2[0] != 0:
                x.append(p2[0])
                y.append(p2[1])
                order += 1
            if p3[0] != 0:
                x.append(p3[0])
                y.append(p3[1])
                order += 1
            if p4[0] != 0:
                x.append(p4[0])
                y.append(p4[1])
                order += 1
            #print(x, y)

            if order > 1 and time5_xy[k][0] != 0:
                z = np.polyfit(x,y,5)
                f = np.poly1d(z)
                
                #### Curve fitting dx
                """ num=np.arange(order+1)
                zx=np.polyfit(num,x,order-2)
                fzx=np.poly1d(zx)
                dx=fzx(order+1) """

                dx = x[order] - x[order-1]        #simple difference dx
                x_n = x[order] + dx
                #print(x_n, f(x_n))
                estimate[k] = [x_n,f(x_n)]
                norm += np.linalg.norm(estimate[k] - time5_xy[k])
                counted_norm += 1
                # print(estimate[k])
            else:
                estimate[k] = [0,0]

              
            """ plt.plot(x,y, 'r+')
            for lin in np.linspace(100,250,50):
                plt.plot(lin,f(lin), 'm*') 
            plt.plot(time3_xy[k][0], time3_xy[k][1], 'b^')
            plt.plot(estimate[k][0], estimate[k][1], 'g-') """
            # plt.show()
        # print(estimate)
        # print(time5_xy)
        """ plt.figure()
        for p,q in zip(time3_xy[:,0],time3_xy[:,1]):
            if abs(p)<0.001 and abs(q)<0.001:
                pass
            else:
                plt.plot(-p, -q, 'b+')
        plt.plot(time3_xy[-1,0],time3_xy[-1,1],'b+', label='Ground Truth Pose')
        for p,q in zip(estimate[:,0],estimate[:,1]):
            if abs(p)<0.001 and abs(q)<0.001:
                pass
            else:
                plt.plot(-p, -q, 'g^')
        plt.plot(estimate[-1,0], estimate[-1,1], 'g^', label='Estimated Pose')
        plt.title('Keypoint plot') """
        norms.append(norm/counted_norm)

    # print('Estimate=', estimate)
    # print('Ground Truth=', time5_xy)
    # time5_x_nz= time5_x[x > 0.0]
    # time5_y_nz = time5_y[x > 0.0]
    # plt.plot(-time5_x, -time5_y, 'b+')
    # plt.plot(-estimate[:,0], -estimate[:,1], 'g^')
    # plt.xlim(right=-50)
    # plt.show()  

print('norms=', norms)
# Plot Histogram
fig, ax = plt.subplots()
n, bins, patches = ax.hist(norms, 10, facecolor='blue', alpha=0.5)
title = 'Histogram of Estimation Accuracy'
description ='FPS:7, Frames:5, Order:5'
annotation = 'N = ' + str(len(norms))
ax.annotate(annotation, (max(norms)-300, 5), fontname='Times New Roman')
ax.set_title(title, fontname='Times New Roman')
ax.set_xlabel('Euclidean Norm between Estimation and Ground Truth (Pixels)',fontname='Times New Roman', fontsize=10)
ax.set_ylabel('Number of Estimations', fontname='Times New Roman', fontsize=10)
# description = 'Figure 1: Histogram for 3 feedback frames'
fig.text(0.5, 0.001, description, ha='center', fontname='Times New Roman', fontsize=11)

plt.show()
