"""This module contains routines for easily working with project paths.

Methods:
    top_level_path() - returns the top level path of the project folder
    data_dir_path() - returns path of directory where data is stored
    images_dir_path() - returns path of directory where images are stored
"""

#----------------------------- Import Statements -------------------------------
import os

#---------------------- Resource Handling Functions ----------------------------
def top_level_path() :
    """Get the top level path for the project.

    Notes:
        -This is the level where nosetests would be run 
        -This directory will contain all other folders and packages 
    Returns:
        the absolute path as a string
    """
    path_with_dir = os.path.dirname(os.path.realpath(__file__))
    top_path, discarded_dir = os.path.split(path_with_dir)
    return top_path

def get_path_to(resource) :
    """Get absolute path to a resource located directly under the project folder.
    Attributes:
        resource - the name of a folder or file located directly under the
            project folder
    Returns:
        the absolute path to the desired folder as a string
    """
    return os.path.join(top_level_path(), resource)

__all__ = ['top_level_path', 'get_path_to']