import matplotlib.pyplot as plt
from PIL import Image

im1 = Image.open('body3_7fps/time3.jpg')
im2 = Image.open('body3_7fps/time4.jpg')

fig, ax = plt.subplots(ncols=2)
ax[0].imshow(im1)
ax[0].set_title('time0', fontname='Times New Roman')
ax[1].imshow(im2)
ax[1].set_title('time1', fontname='Times New Roman')
# fig.suptitle('OpenPose Results')
description = 'Figure 1: OpenPose results of two consecutive time frames'
fig.text(0.5, 0.1, description, ha='center', fontname='Times New Roman', fontsize=16)
# Set the font name for axis tick labels to be Comic Sans
plt.show()
