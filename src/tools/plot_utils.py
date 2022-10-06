"""
# -*- coding: utf-8 -*-
-----------------------------------------------------------------------------------
# Author: Anant Dashpute
-----------------------------------------------------------------------------------
# Description: Common plot functions are added here
"""

import matplotlib.pyplot as plt
import pandas as pd
import cv2
from src.tools import util


def view_lidar(pc, azimuth=180, elevation=10):
    """
    pc : Point cloud array
    azimuth: Rotation angle
    elevation: View angle
    """

    plt.figure(figsize=[10, 10])
    ax = plt.axes(projection='3d')
    d = {'X': pc[0], 'Y': pc[1], 'Z': pc[2], 'intensity': pc[3]}
    df = pd.DataFrame.from_dict(d)
    ax.scatter(df['X'], df['Y'], df['Z'], c=df['intensity'], s=0.1)
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_zlim(-15, 15)
    ax.azim = azimuth
    ax.elev = elevation
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


def view_image(root_path, data_path):
    """
    image_path : Direct path to image
    """
    image_path = util.get_image_path(root_dir=root_path, data_path=data_path)
    img = cv2.imread(image_path)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
