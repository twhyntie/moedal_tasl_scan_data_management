#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

#...for the image base class
from wrapdata.image import ImageFile

class SBJ(ImageFile):
    """
    Wrapper class for the TASL NTD scan Zooniverse subject images.
    """

    def __init__(self, path):
        """ Constructor. """
        super(SBJ, self).__init__(path)

        ## The scan image row.
        self.__row = self.get_scan_row()

        lg.info(" *")
        lg.info(" * Initialising SBJ object from '%s'." % (self.get_path()))
        lg.info(" *--> Batch ID             : '%s'" % (self.get_batch_id()))
        lg.info(" *--> Scan  ID             : '%s'" % (self.get_scan_id()))
        lg.info(" *--> ID                   : '%s'" % (self.get_id()))
        lg.info(" *--> Image filename       : '%s'" % (self.get_filename()))
        lg.info(" *--> Image format         : '%s'" % (self.get_image_format()))
        #lg.info(" *-->")
        lg.info(" *--> Image dimensions     : %d x %d" % (self.get_image_width(), self.get_image_height()))
        #lg.info(" *-->")
        lg.info(" *--> Scan row             : %d" % (self.get_scan_row()))
        lg.info(" *--> Scan column          : %d" % (self.get_scan_column()))

        lg.info(" *")

    def get_id(self):
        return self.get_filename()[:19]
    def get_scan_id(self):
        return self.get_filename()[:13]
    def get_batch_id(self):
        return self.get_filename()[:10]
    def get_format(self):
        return "SBJ"
    def get_scan_row(self):
        return int(self.get_filename()[14:16])
    def get_scan_column(self):
        return int(self.get_filename()[17:19])
