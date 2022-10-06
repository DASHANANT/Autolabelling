"""
# -*- coding: utf-8 -*-
-----------------------------------------------------------------------------------
# Author: Anant Dashpute
-----------------------------------------------------------------------------------
# Description: preprocessing functions added here
"""


def removePoints(df, x=None, y=None, z=None):
    """
    Boundary condition
    :param df: point cloud
        list of boundary condition to remove points
        :param x=[minX, maxX]
        :param y=[minY, maxY]
        :param z=[minZ,maxZ]
    :return: cleaned pc
    """
    d = {'X': df[0], 'Y': df[1], 'Z': df[2]}
    df = pd.DataFrame.from_dict(d)
    if x is None:
        x = []
    if x:
        df = df['X'] > x[0]
        df = df['X'] <= x[1]

    if y:
        df = df['Y'] > y[0]
        df = df['Y'] <= y[1]

    if z:
        df = df['Z'] > z[0]
        df = df['Z'] <= z[1]
    return df


def remove_ground(pc):
    """
    :param pc= Point cloud
    """
    return removePoints(pc, x=False, y=False, z=[-1.5, 10])


def random_crop(pc, x=None, y=None, z=None):
    """
        :param x: [minX,maxX]
        :param y: [minY,maxY]
        :param z: [minZ,maxZ]
        :param pc= Point cloud
        """
    return removePoints(pc, x=x, y=y, z=z)
