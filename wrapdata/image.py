#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspect(s).
import os

#...for the logging.
import logging as lg

#...for the image manipulation.
import matplotlib.image as mpimg

class ImageFile(object):
    """
    Wrapper base class for an file.
    """

    def __init__(self, path):
        """ Constructor. """

        ## The path.
        self.__path = path

        ## The filename.
        self.__filename = os.path.basename(self.__path)

        ## The image format.
        self.__image_format = os.path.splitext(self.__filename)[1][1:].upper()

        # Load in the image.

        ## The image as a NumPy array.
        self.__img = mpimg.imread(self.__path)

    def get_path(self):
        return self.__path
    def get_filename(self):
        return self.__filename
    def get_image_format(self):
        return self.__image_format

    def get_image(self):
        return self.__img
    def get_file_size(self):
        return os.path.getsize(self.__path)

    def get_image_width(self):
        return self.__img.shape[1]
    def get_image_height(self):
        return self.__img.shape[0]
