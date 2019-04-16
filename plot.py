import numpy as np
import matplotlib.pyplot as plt

key_points=np.load('pose_keypoints_2d.npy')
# print(key_points)
x1=key_points[0,:,0]
y1=key_points[0,:,1]
# z=key_points[0,:,2]
plt.scatter(x1,y1)
x2=key_points[1,:,0]
y2=key_points[1,:,1]
plt.scatter(x2,y2)
x3=key_points[2,:,0]
y3=key_points[2,:,1]
plt.scatter(x3,y3)
plt.show()
