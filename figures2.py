import numpy as np
import matplotlib.pyplot as plt

### Plotting Extrapolation
x = [1,2,3,4]
y = [4,1,0,1]
z = np.polyfit(x,y,2)
f = np.poly1d(z)
space = np.linspace(0,5,50)
line = plt.plot(space,f(space), 'g--', linewidth=1)
plt.plot(x,y, 'ro')

x_est = 5
GT = [6,3]

# plot the line connectioning estimation and GT
#plt.plot([x_est,GT[0]], [f(x_est),GT[1]], 'm-')
# plot the estimated and GT points
plt.plot(5,f(x_est), 'bo')
plt.plot(6,3,'go', alpha=0)
plt.show()


'''
### Plotting geound truth pose vs estimate
plt.figure()
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
plt.title('Keypoint plot')
'''
