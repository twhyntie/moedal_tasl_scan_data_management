#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper class to test.
from sbjdata import SBJ

class TestSBJ(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sbj(self):

        ## The SBJ image file.
        sbj = SBJ("testdata/SBJ/data/TASL000000_00_00_00.png")

        # The tests.

        # Test the file properties.
        self.assertEqual(sbj.get_filename(), "TASL000000_00_00_00.png")
        self.assertEqual(sbj.get_file_size(), 12164)
        self.assertEqual(sbj.get_image_format(), "PNG")
        self.assertEqual(sbj.get_image_width(), 390)
        self.assertEqual(sbj.get_image_height(), 390)

        # Test the data format code.
        self.assertEqual(sbj.get_format(), "SBJ")

        # Test the subject, scan and batch ID.
        self.assertEqual(sbj.get_id(),       "TASL000000_00_00_00")
        self.assertEqual(sbj.get_scan_id(),  "TASL000000_00")
        self.assertEqual(sbj.get_batch_id(), "TASL000000")

        # Test the scan properties.
        self.assertEqual(sbj.get_scan_row(), 0)
        self.assertEqual(sbj.get_scan_column(), 0)


if __name__ == "__main__":

    lg.basicConfig(filename='logfiles/test_sbjdata.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *=============================================")
    lg.info(" * Logger output from wrappers/test_sbjdata.py ")
    lg.info(" *=============================================")
    lg.info(" *")

    unittest.main()
