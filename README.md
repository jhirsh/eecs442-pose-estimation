# Estimating Figure Trajectory using OpenPose
## Shruti Ambekar and Jonas Hirshland
## EECS 442 Final Project (Winter 2019)

## Setup

### Carnegie Mellon OpenPose
We built our project using processed frames from [CMU's
OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose).

The instruction steps for all operating systems should be in there. You can
clone this repository in the following path in OpenPose after you have
configured using CMake.
`OpenPose_directory/build/examples/tutorial_api_python/`. The only file that
needs to be moved from this repository to that repository is the
`multiple_frames.py` file. It will not run correctly if it remains in this
project repository.

### Our Files

* `parse_video.py` takes a command line arguments `--filename`, `--frame_rate`,
  and `--output` which takes in a `.MOV` file and outputs JPGs after skipping
  as many frames as put in the frame rate argument. 

* `multiple_frames.py` is a slightly tweaked `01_keypoints_from_images.py` from
OpenPose that correctly stores the keypoints in `.npz` files so we can reuse
them instead of having to rerun OpenPose.

* `estimate[x].py` are the different estimations we used, using linear, and
  other methods. 

* `figure[x].py` are some pyplot figures created to help illustrate our
  methodology in the report.

* `raw_videos/` are the videos we tested our estimations on.

* `processed_videos/` are the processed videos after running `parse_video` and
  `multiple_frames` scripts on our input data.
