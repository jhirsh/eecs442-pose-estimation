import os
import numpy as np

def main():
    twod = np.load('pose_keypoints_2d.npy')
    threed = np.load('pose_keypoints_3d.npy')
    print(twod)
    print('break')
    print(threed)

if __name__ == '__main__':
    main()

