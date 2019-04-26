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

            if order > 1 and time5_xy[k][0] != 0:
                z = np.polyfit(x,y,2)
                f = np.poly1d(z)
                
                #### Curve fitting dx
                """ num=np.arange(order+1)
                zx=np.polyfit(num,x,order-2)
                fzx=np.poly1d(zx)
                dx=fzx(order+1) """

                ### simple difference dx
                dx = x[order] - x[order-1]        
               
                x_n = x[order] + dx
                estimate[k] = [x_n,f(x_n)]
                norm += np.linalg.norm(estimate[k] - time5_xy[k])
                counted_norm += 1
            else:
                estimate[k] = [0,0]
        norms.append(norm/counted_norm)

        ### Plotting Extrapolation
        """ plt.plot(x,y, 'r+')
            for lin in np.linspace(100,250,50):
                plt.plot(lin,f(lin), 'm*') """

        ### Plotting geound truth pose vs estimate   
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

    
#### Chop off values >1000 assuming they're outliers(based on experiments) before plotting histogram
norm_p=[]
for i in range(len(norms)):
    if norms[i]>1000:
        pass
    else:
        norm_p.append(norms[i])

mean=np.mean(norm_p)
mean='%.2f' % mean

# Plot Histogram
fig, ax = plt.subplots()
n, bins, patches = ax.hist(norm_p, 50, facecolor='blue', alpha=0.5)
m=max(n)
title = 'Histogram of Estimation Accuracy'
annotation1 = 'N =' + str(len(norm_p))
ax.annotate(annotation1, (max(norm_p)-150, m-0.3), fontname='Times New Roman')
annotation2 = 'Mean error = ' + str(mean)
ax.annotate(annotation2, (max(norm_p)-150, m-0.5), fontname='Times New Roman')
ax.set_title(title, fontname='Times New Roman')
ax.set_xlabel('Euclidean Norm between Estimation and Ground Truth (Pixels)',fontname='Times New Roman', fontsize=10)
ax.set_ylabel('Number of Estimations', fontname='Times New Roman', fontsize=10)
description ='FPS:7, Frames:5, Order:2'
fig.text(0.5, 0.001, description, ha='center', fontname='Times New Roman', fontsize=11)
plt.show()

""" ##### Plot of error variation with order increase
error=[89.64, 95.31, 163.22, 185.94, 308.82]
na=np.arange(1,6)
plt.plot(na, error, marker='o', markerfacecolor='blue', markersize=7, color='skyblue', linewidth=2)
for i, t in enumerate(error):
    # print(i)
    x=na[i]
    y=t
    plt.annotate(t,(x,y))
plt.xlabel('Order of polynomial fit')
plt.ylabel('Mean Error')
plt.title('Mean Error variation with variation in order')
plt.show() """

""" ##### Plot of error variation with feedback frames variation
error=[136.86, 89, 95.31 ]
na=[3,4,5]
plt.plot(na, error, marker='o', markerfacecolor='blue', markersize=7, color='skyblue', linewidth=2)
for i, t in enumerate(error):
    # print(i)
    x=na[i]
    y=t
    plt.annotate(t,(x,y))
plt.xlabel('Number of Feedback Frames')
plt.ylabel('Mean Error')
plt.title('Mean Error variation with variation in number of feedback frames')
plt.show() """
