"""
# -*- coding: utf-8 -*-
-----------------------------------------------------------------------------------
# Author: Anant Dashpute
-----------------------------------------------------------------------------------
# Description: All the parser arguments are added here
"""


import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='3D Bounding Box')

    parser.add_argument('--rd', type=str, default="../",
                        help='Root Directory')

    parser.add_argument('--dd', type=str, default=None,
                        help='Data Directory')

    parser.add_argument('--dp', type=str, default=None,
                        help='Exact Data path')

    # for lidar -------------------------------------------------------
    parser.add_argument('--i', type=int, default=0,
                        help='Index number of datafile in a data directory')

    parser.add_argument('--bv', action='store_true',
                        help='to show bird view')

    parser.add_argument('--ev', action='store_true',
                        help='to show environment view with different elevation angle')

    parser.add_argument('--eva', type=int, default=10,
                        help='elevation angle ')

    parser.add_argument('--azim', type=int, default=180,
                        help='azimuth angle ')

    parser.add_argument("--vwp", action="store_true", help="to view point cloud")

    # for camera -------------------------------------------------------------
    parser.add_argument("--vwc", action="store_true", help="to view images")

    configs = vars(parser.parse_args())

    return configs
