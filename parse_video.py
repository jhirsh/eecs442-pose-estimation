import argparse
import cv2
import json
import os

""" USAGE:
    * frame_rate
    * filename
"""

parser = argparse.ArgumentParser()
parser.add_argument('--frame_rate', default=5, type=int, help='Proc')
parser.add_argument('--filename', default='temp', help='filename')
parser.add_argument('--output', default='output', help='none')
args = parser.parse_known_args()  # video narm_movement')ame

filename_video = args[0].filename + '.mov'
cap = cv2.VideoCapture(filename_video)

if not os.path.isdir(args[0].output):
    os.mkdir(args[0].output)

outputfolder = args[0].output
if outputfolder[-1] != '/':
    outputfolder += '/'

counter = 0
while True:
    ret, frame = cap.read()
    if ret == True and counter % args[0].frame_rate == 0:
        filename = outputfolder + str(counter) + '.jpg'
        cv2.imwrite(filename,frame)
    elif ret == False:
        break
    counter+=1

cap.release()
cv2.destroyAllWindows()
