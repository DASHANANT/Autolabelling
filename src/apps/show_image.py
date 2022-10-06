"""
# -*- coding: utf-8 -*-
-----------------------------------------------------------------------------------
# Author: Anant Dashpute
-----------------------------------------------------------------------------------
# Description: Class to visualize the point cloud data
"""

from src.tools import plot_utils


class show_image(object):
    """
          Class having different plotting functions for camera data
          image
          images with labels--Coming soon
    """

    def __init__(self, root, dp, cam=False):
        if cam:
            plot_utils.view_image(root_path=root, data_path=dp)
