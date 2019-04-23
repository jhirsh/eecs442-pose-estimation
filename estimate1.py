import numpy as np
import matplotlib.pyplot as plt 
from scipy.spatial import distance
import pandas as pd

""" key_points=np.load('pose_keypoints_2d.npy')
# print(key_points)
 x1=key_points[0,:,0]
y1=key_points[0,:,1]
z1=key_points[0,:,2]
plt.scatter(-x1,-y1) 
 for i,type in enumerate(z1):
    x=x1[i]
    y=y1[i]
    plt.text(-x,-y,'%.2f' % z1[i])
x2=key_points[1,:,0]
y2=key_points[1,:,1]
z2=key_points[1,:,2]
plt.scatter(-x2,-y2)
for i,type in enumerate(z2):
    x=x2[i]
    y=y2[i]
    plt.text(-x,-y,'%.2f' % z2[i])
x3=key_points[2,:,0]
y3=key_points[2,:,1]
z3=key_points[2,:,2]
plt.scatter(-x3,-y3)
for i,type in enumerate(z3):
    x=x3[i]
    y=y3[i]
    plt.text(-x,-y,'%.2f' % z3[i])

x4=key_points[3,:,0]
y4=key_points[3,:,1]
z4=key_points[3,:,2]
plt.scatter(-x4,-y4)
for i,type in enumerate(z4):
    x=x4[i]
    y=y4[i]
    plt.text(-x,-y,'%.2f' % z4[i])
plt.show()  """

key_points=np.load('walk_poses.npz')

###time0 frame####################################################
time0=key_points['time0']
time0_x=time0[:,:,0]
time0_y=time0[:,:,1]
time0_xy=time0[:,:,0:2]
time0_xy=np.reshape(time0_xy,(25,2))
# print(time0_xy)
n=np.shape(time0_xy)
# print(n)

###time1 frame#################################################
time1=key_points['time1']
time1_xy=time0[:,:,0:2]
time1_xy=np.reshape(time1_xy,(25,2))
# print('time1',time1_xy)
m=np.shape(time1_xy)
# print(m)
time1_x=time1[:,:,0]
time1_y=time1[:,:,1]

###Differential & estiamtion##################################################
# dk=np.array(25,2)
for k in range(0,25):
    # print(k)
    dk_x=time1_x-time0_x
    dk_y=time1_y-time0_y
""" print(dk_x)
print(dk_y)
a=np.shape(dk_x)
b=np.shape(dk_y)
print(a,b) """
dk=np.hstack((dk_x.T,dk_y.T))
# print('dk',dk)
estimate=time1_xy+dk
# print(estimate)

num=np.arange(25)
time2=key_points['time2']
# print(time2)

# df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21) })

plt.scatter(estimate[:,0],estimate[:,1])
plt.scatter(time2[:,:,0],time2[:,:,1])
plt.plot(estimate[:,0],estimate[:,1], label='Our Estimate', marker='o', markerfacecolor='m', markersize=7, color='olive', linewidth=2, zorder=1)
plt.plot(time2[:,:,0],time2[:,:,1],linestyle='-', color='olive', linewidth=2, zorder=2)
# markerfacecolor='g', 
""" print(estimate[:,0])
print(time2[:,:,0]) """

for i, t in enumerate(num):
    # print(i)
    x=estimate[i,0]
    y=estimate[i,1]
    plt.annotate(t,(x,y))
for i, t in enumerate(num):
    # print(i)
    x=time2[:,i,0]
    y=time2[:,i,1]
    plt.annotate(t,(x,y))
plt.legend()
plt.show()
    

    
    

# plt.scatter()  


