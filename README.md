# Pose-Detection-python-program-using-OpenPose-software
OpenPose software provides a very convenient tool for extraction of coordinates of human body joints. The program is using the obtained points to detect if a user was Happy/Sad/Surpirse in the video.

The instruction for using the pose estimation code:
1. Record a video with happy, surprise, sad, garbade (disgust) poses
2. Name the video as "VideoSample.mp4"
3. Save the video in the folder "videos", which is located on the desktop
4. Run parse_video.py module
5. Run to_format.py module
6. Save the output .csv file in the desktop
7. Run the PoseEstimation.py module
8. Enjoy the emotion estimations :)

ACKNOWLEDGEMENT
The given project was possible thanks to the authors of OpenPose open-source software. The references are given below:

@article{8765346,
  author = {Z. {Cao} and G. {Hidalgo Martinez} and T. {Simon} and S. {Wei} and Y. A. {Sheikh}},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  title = {OpenPose: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields},
  year = {2019}
}

@inproceedings{simon2017hand,
  author = {Tomas Simon and Hanbyul Joo and Iain Matthews and Yaser Sheikh},
  booktitle = {CVPR},
  title = {Hand Keypoint Detection in Single Images using Multiview Bootstrapping},
  year = {2017}
}


