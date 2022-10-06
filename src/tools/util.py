"""
# -*- coding: utf-8 -*-
-----------------------------------------------------------------------------------
# Author: Anant Dashpute
-----------------------------------------------------------------------------------
# Description: All common functions are added here
"""

import os


def get_dire_len(dire):
    """
        it finds count of all the documents present in that path
        :param dire: specific directory path
        :return: count of files
    """
    return len([entry for entry in os.listdir(dire)])


def get_path(root_dir=None, data_dir=None, idx=0):
    """
            :parameters
            root_dir: Contains folders of training and testing data
            data_dir: contains point cloud files
            data_path: Fixed path for specific point cloud
            idx: Index number from base_dir
    """
    data_path = None
    if root_dir:
        data_dir = root_dir + '\\training\\pc'
        num_samples = get_dire_len(data_dir)
        assert idx < num_samples
        data_path = data_dir + "\\" + os.listdir(data_dir)[idx]

    elif data_dir:
        num_samples = get_dire_len(data_dir)
        assert idx < num_samples
        data_path = data_dir + "\\" + os.listdir(data_dir)[idx]

    return data_path


def get_file_index(root_dir=None, dp=None):
    if "training" in dp.split("\\"):
        data_dir = root_dir + '\\training\\pc'
    else:
        data_dir = root_dir + '\\testing\\pc'
    index = os.listdir(data_dir).index(dp.split("\\")[::-1][0])
    return index


def get_image_path(root_dir=None, data_path=None):
    """
            :parameters
            root_dir: Contains folders of training and testing data

    """
    idx = get_file_index(root_dir=root_dir, dp=data_path)
    if "training" in data_path.split("\\"):
        data_dir = root_dir + '\\training\\image'
        image_path: str = data_dir + "\\" + os.listdir(data_dir)[idx]

    else:
        data_dir = root_dir + '\\testing\\image'
        image_path: str = data_dir + "\\" + os.listdir(data_dir)[idx]

    return image_path
