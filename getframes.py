# IMPORTANT: REQUIREMENTS
# Before running the code, you need two folders:
#   input  - put your videos here
#   frames - your frames will be written here, in a folder named based on your video

import cv2
import os
import numpy as np

INPUT_FILES = os.listdir('input')

FRAME_SKIP = 120

for f in INPUT_FILES:
    cap = cv2.VideoCapture('input/'+f)
    current_frame = 0
    current_image = 0
    FRAME_RATE = cap.get(cv2.CAP_PROP_FPS)
    FRAME_COUNT = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    file_name = os.path.splitext(f)[0]
    print(file_name)
    if (not os.path.exists('frames/'+file_name)):
        os.mkdir('frames/'+file_name)

    while (current_frame < FRAME_COUNT):
        print(file_name+" "+str(current_frame)+"/"+str(FRAME_COUNT))
        ret, frame = cap.read()
        cap.set(1, current_frame)
        cv2.imwrite("frames/" + file_name + "/" + file_name +
                    "_"+str(current_image)+".png", frame)
        current_frame += FRAME_SKIP
        current_image += 1
