import numpy as np
import matplotlib.pyplot as plt 
from scipy.spatial import distance
import pandas as pd


key_points=np.load('body1.npz')

###time0 frame####################################################
time0=key_points['time0']
time0_x=time0[:,:,0]
time0_y=time0[:,:,1]
time0_xy=time0[:,:,0:2]
time0_xy=np.reshape(time0_xy,(25,2))
n=np.shape(time0_xy)

###time1 frame#################################################
time1=key_points['time1']
time1_xy=time0[:,:,0:2]
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
time2=key_points['time2'] #Actual pose in the next frame

plt.scatter(estimate[:,0],estimate[:,1])
plt.scatter(time2[:,:,0],time2[:,:,1])


for i, t in enumerate(num):
    x=estimate[i,0]
    y=estimate[i,1]
    plt.annotate(t,(x,y))
for i, t in enumerate(num):
    x=time2[:,i,0]
    y=time2[:,i,1]
    plt.annotate(t,(x,y))

plt.show()
    

    
    

# plt.scatter()  


