import numpy as np
import matplotlib.pyplot as plt


x=np.random.randint(100,size=5)
print('x=',x)
y=np.random.randint(100,size=5)
print('y=',y)
""" x = [10, 30, 50, 80, 100]
y = [30, 45, 40, 20,  40] """

for x1, y1 in zip(x, y):
    plt.plot(x1, y1, 'go')

z=np.polyfit(x,y,4)
print('z=',z)
f=np.poly1d(z)

for x1 in np.linspace(-150,150,150):
    plt.plot(x1,f(x1),'r+')

plt.axis([-200,200,-200,200])
plt.show()


