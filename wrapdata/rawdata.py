#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

#...for the image base class
from wrapdata.image import ImageFile

class RAW(ImageFile):
    """
    Wrapper class for the raw TASL scan images.
    """

    def __init__(self, path):
        """ Constructor. """
        super(RAW, self).__init__(path)

        lg.info(" *")
        lg.info(" * Initialising RAW object from '%s'." % (self.get_path()))
        lg.info(" *--> ID                   : '%s'" % (self.get_id()))
        lg.info(" *--> Batch ID             : '%s'" % (self.get_batch_id()))
        lg.info(" *--> Image filename       : '%s'" % (self.get_filename()))
        lg.info(" *--> Image dimensions     : %d x %d" % (self.get_image_width(), self.get_image_height()))
        lg.info(" *--> Image format         : '%s'" % (self.get_image_format()))

        lg.info(" *")

    def get_id(self):
        return self.get_filename()[3:12]
    def get_batch_id(self):
        return self.get_filename()[3:9]
    def get_format(self):
        return "RAW"
