# From Python
# It requires OpenCV installed for Python
import sys
import cv2
import os
from sys import platform
import argparse
import time
import numpy as np

# Import Openpose (Windows/Ubuntu/OSX)
dir_path = os.path.dirname(os.path.realpath(__file__))
try:
    # Windows Import
    if platform == "win32":
        # Change these variables to point to the correct folder (Release/x64 etc.)
        sys.path.append(dir_path + '/../../python/openpose/Release');
        os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/../../x64/Release;' +  dir_path + '/../../bin;'
        import pyopenpose as op
    else:
        # Change these variables to point to the correct folder (Release/x64 etc.)
        sys.path.append('../../python');
        # If you run `make install` (default path is `/usr/local/python` for Ubuntu), you can also access the OpenPose/python module from there. This will install OpenPose and the python library at your desired installation path. Ensure that this is in your python path in order to use it.
        # sys.path.append('/usr/local/python')
        from openpose import pyopenpose as op
except ImportError as e:
    print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
    raise e

# Flags
parser = argparse.ArgumentParser()
parser.add_argument("--image_dir", default="../../../examples/media/", help="Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).")
parser.add_argument("--no_display", default=False, help="Enable to disable the visual display.")
parser.add_argument("--output", default="output/", help="output")
args = parser.parse_known_args()

if not os.path.isdir(args[0].output):
    os.makedirs(args[0].output)

outputfolder = args[0].output
if outputfolder[-1] != '/':
    outputfolder += '/'

# Custom Params (refer to include/openpose/flags.hpp for more parameters)
params = dict()
params["model_folder"] = "../../../models/"

# Add others in path?
for i in range(0, len(args[1])):
    curr_item = args[1][i]
    if i != len(args[1])-1: next_item = args[1][i+1]
    else: next_item = "1"
    if "--" in curr_item and "--" in next_item:
        key = curr_item.replace('-','')
        if key not in params:  params[key] = "1"
    elif "--" in curr_item and "--" not in next_item:
        key = curr_item.replace('-','')
        if key not in params: params[key] = next_item

# Construct it from system arguments
# op.init_argv(args[1])
# oppython = op.OpenposePython()

# Starting OpenPose
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()

# Read frames on directory
imagePaths = sorted(os.listdir(args[0].image_dir), key = lambda x: int(x.split("/")[-1].split(".")[0]))
imagePaths = [args[0].image_dir + path for path in imagePaths]
print(imagePaths)
start = time.time()
# Process and display images
counter=0
poses = {}
for imagePath in imagePaths:
    print("Processing " + imagePath + "\n")
    datum = op.Datum()
    imageToProcess = cv2.imread(imagePath)
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop([datum])

    print(str(datum.poseKeypoints))
    filename = 'time' + str(counter)
    poses[filename] = datum.poseKeypoints
    cv2.imwrite(outputfolder + filename + '.jpg', datum.cvOutputData)
    counter += 1

np.savez(outputfolder + outputfolder[:-1] +'.npz', **poses)
end = time.time()
print("OpenPose demo successfully finished. Total time: " + str(end - start) + " seconds")
