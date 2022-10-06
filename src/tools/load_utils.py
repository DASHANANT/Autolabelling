"""
# -*- coding: utf-8 -*-
-----------------------------------------------------------------------------------
# Author: Anant Dashpute
-----------------------------------------------------------------------------------
# Description: functions to load the data, which can be further used
"""

# importing libraries
from __future__ import print_function
import numpy as np


def read_pc(filepath, n_vec, format_type='bin'):
    """
    accepted_formats vto read point cloud= ['txt','npy','npz','bin']
    :param
    filepath: data
    n_vec: no. attributes to be extracted from pc
    format_type : default 'bin'

    """
    if format_type == 'bin':
        pc_bin = np.fromfile(filepath, '<f4')
        pc_bin = np.reshape(pc_bin, (-1, n_vec)).T
        return pc_bin

    elif format_type == 'npy' or format_type == 'npz':
        pc_np = np.load(filepath)
        pc_np = np.reshape(pc_np, (-1, n_vec))
        return pc_np

    elif format_type == 'txt':
        pc_txt = np.loadtxt(filepath, delimiter=',')
        pc_txt = pc_txt[:, :n_vec]
        return pc_txt

    else:
        print("Other formats are not supported yet")
        return 0


def get_pc(data_path=None, n_vec=4):
    """
    it returns n-D Array of point cloud (pc) data
    :param

    n_vec: (var)
            default= 4 ...attributes (X,Y,Z,Intensity)

    :return: array
    """

    if data_path:
        format_type = data_path.split('.')[::-1][0]
        return read_pc(data_path, n_vec, format_type)
    else:
        print('None path has None files')


# def get_labels(root_dir=None, idx=0):
#     """
#     labels---  Class name and 3-D bounding box coordinates
#             ex. -
#              car 0 1 12 32 24 33 532 432 43 666 332 11.0 121.21
#
#              first value is class name
#              then coordinates
#     :return: returns labels
#     """

#     return o
