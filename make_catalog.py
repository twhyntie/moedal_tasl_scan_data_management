#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

 MoEDAL and CERN@school - Make the metadata catalogues.

 See the README.md file and the GitHub wiki for more information.

 http://cernatschool.web.cern.ch

"""

# Import the code needed to manage files.
import os, glob

#...for parsing the arguments.
import argparse

#...for the logging.
import logging as lg

#...for handling the annotation JSON information.
import json

# For importing modules on the fly.
import importlib

if __name__ == "__main__":

    print("*")
    print("*==================================================*")
    print("* MoEDAL and CERN@school: make metadata catalogues *")
    print("*==================================================*")
    print("*")

    # Get the datafile path from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument("dataFormat",      help="The format to make the metadata catalogue for.")
    parser.add_argument("dataPath",        help="Path to the data to catalogue.")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    args = parser.parse_args()

    ## The data format to make the metadata catalogue for.
    data_format = args.dataFormat

    ## The path to the metadata schema.
    metadata_path = "metadata/%s/" % (data_format.upper())
    #
    # Check if the path exists. If it doesn't, quit.
    if not os.path.isdir(metadata_path):
        raise IOError("* ERROR: Invalid data format '%s' - '%s' does not exist!" % (schema_format, metadata_path))

    ## The path to the data.
    data_path = os.path.join(args.dataPath, data_format.upper())
    #
    if not os.path.isdir(data_path):
        raise IOError("* ERROR: Unable to find data at '%s'." % (data_path))

    ## The path to the catalog file.
    catalog_path = os.path.join(data_path, "catalog.csv")

    # Set the logging level.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    # Configure the logging.
    lg.basicConfig(filename=os.path.join('logfiles', 'make_catalog.log'), filemode='w', level=level)

    lg.info(" *")
    lg.info(" *====================================================*")
    lg.info(" * MoEDAL and CERN@school: Making metadata catalogues *")
    lg.info(" *====================================================*")
    lg.info(" *")
    lg.info(" * Data format to be processed : '%s'" % (data_format))
    lg.info(" * Making the catalog file in  : '%s'" % (catalog_path))
    lg.info(" *")

    ## The name of the module containing the metadata schema wrapper class.
    meta_module_name = "wrapmeta.%smeta" % (data_format.lower())

    ## The name of the module containing the data wrapper class.
    data_module_name = "wrapdata.%sdata" % (data_format.lower())

    try:

        ## The metadata wrapper module.
        meta_m = importlib.import_module(meta_module_name)

        ## The data wrapper module.
        data_m = importlib.import_module(data_module_name)

    except ImportError, e:
        raise ImportError("* ERROR: Invalid data format '%s' - %s." % (data_format, str(e).lower()))

    ## The catalogue string.
    cs = meta_m.the_schema.get_csv_header_string() + "\r"

    ## The record paths.
    record_paths = glob.glob(os.path.join(data_path, "data/*.*"))

    for i, record_path in enumerate(sorted(record_paths)):
        lg.info(" * Found record % 3d: '%s'" % (i, record_path))

        if data_format == "RAW":
            record = data_m.RAW(record_path)

            cs += "TASL%s," % (record.get_id())
            cs += "TASL%s," % (record.get_batch_id())
            cs += "moedal,"
            cs += "," # Owner
            cs += "%s," % (record.get_filename())
            cs += "%s," % (record.get_image_format())
            cs += "%s," % (record.get_format())
            cs += "%d," % (record.get_image_width())
            cs += "%d," % (record.get_image_height())
            cs += "%d," % (record.get_file_size())
            cs += "," # Rows
            cs += "," # Columns
            cs += "," # Individual scan images
            cs += "5.0"
        elif data_format == "SBJ":
            record = data_m.SBJ(record_path)
            cs += "%s," % (record.get_id())
            cs += "%s," % (record.get_scan_id())
            cs += "%s," % (record.get_batch_id())
            cs += "moedal,"
            cs += "," # Owner
            cs += "%s," % (record.get_format())
            cs += "%s," % (record.get_filename())
            cs += "%s," % (record.get_image_format())
            cs += "%d," % (record.get_file_size())
            cs += "%d," % (record.get_image_width())
            cs += "%d," % (record.get_image_height())
            cs += "%d," % (record.get_scan_row())
            cs += "%d," % (record.get_scan_column())
            cs += "5.0"
        elif data_format == "ANN":
            record = data_m.ANN(record_path)
            cs += "%s," % (record.get_id())
            cs += "77.83," # Workflow ID
            cs += "%d"  % (record.get_number_of_annotations())

        if i < len(record_paths): cs += "\r"

    # Write out the catalogue file.
    with open(catalog_path, "w") as cf:
        cf.write(cs.encode('utf8'))
