import cv2
import numpy as np
import math
import os

image_directory = './data/test'
score_directory = './result'

for file in os.listdir(image_directory):
    image = cv2.imread(os.path.join(image_directory, file))
    with open(os.path.join(score_directory, "{}.rbox.score".format(file)), "r") as f:
        lines = f.readlines()

        for l in lines:
            as_list = l.split(" ")
            Cx = (float(as_list[0]))
            Cy = (float(as_list[1]))
            W = (float(as_list[2]))
            H = (float(as_list[3]))
            Angle_rad = (float(as_list[6].replace("\n", "")))

            _Angle_rad = Angle_rad * math.pi / 180
            b = math.cos(_Angle_rad) * 0.5
            a = math.sin(_Angle_rad) * 0.5
            pt0 = (int(Cx - a * H - b * W),
                   int(Cy + b * H - a * W))
            pt1 = (int(Cx + a * H - b * W),
                   int(Cy - b * H - a * W))
            pt2 = (int(2 * Cx - pt0[0]), int(2 * Cy - pt0[1]))
            pt3 = (int(2 * Cx - pt1[0]), int(2 * Cy - pt1[1]))
            cv2.line(image, pt0, pt1, (0, 255, 0), 2)
            cv2.line(image, pt1, pt2, (0, 255, 0), 2)
            cv2.line(image, pt2, pt3, (0, 255, 0), 2)
            cv2.line(image, pt3, pt0, (0, 255, 0), 2)
    cv2.imwrite(os.path.join(score_directory, file), image)
