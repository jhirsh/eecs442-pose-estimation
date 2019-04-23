import numpy as np
import matplotlib.pyplot as plt 

key_points=np.load('walk_poses.npz')

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

num=np.arange(25)
time2=key_points['time2']
time2_h=np.reshape(time2[:,:,0:2], (25,2))

plt.scatter(estimate[:,0],estimate[:,1])
plt.scatter(time2_h[:,0],time2_h[:,1])
plt.plot(estimate[:,0],estimate[:,1], label='Our Estimate', marker='o', markerfacecolor='blue', markersize=7, color='skyblue', linewidth=2, zorder=1)
plt.plot(time2_h[:,0],time2_h[:,1], label='Next Pose', marker='*', markerfacecolor='pink', markersize=7, color='k', linewidth=2, zorder=1)

for i, t in enumerate(num):
    # print(i)
    x=estimate[i,0]
    y=estimate[i,1]
    plt.annotate(t,(x,y))

for i, t in enumerate(num):
    # print(i)
    x=time2_h[i,0]
    y=time2_h[i,1]
    plt.annotate(t,(x,y))

plt.legend()
plt.show()
