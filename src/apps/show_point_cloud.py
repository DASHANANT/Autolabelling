"""
# -*- coding: utf-8 -*-
-----------------------------------------------------------------------------------
# Author: Anant Dashpute
-----------------------------------------------------------------------------------
# Description: Class to visualize the point cloud data
"""

from src.tools import plot_utils
from src.tools import load_utils
from src.tools import preprocess_util


class show_point_cloud(object):
    """
       Class having different plotting functions for lidar data
       BV- Bird view
       EV- Environment/ 360 view
    """

    def __init__(self, pc_path, azimuth=180, elevation=10, rmg=False, bev=False, ev=False):
        self.pc = load_utils.get_pc(data_path=pc_path)
        if rmg:
            self.pc = preprocess_util.remove_ground(self.pc)
        if bev:
            plot_utils.view_lidar(self.pc, elevation=90)
        elif ev:
            plot_utils.view_lidar(self.pc, azimuth=azimuth, elevation=elevation)


