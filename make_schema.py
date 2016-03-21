#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

 MoEDAL and CERN@school - Make the metadata schema.

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
    print("*==============================================*")
    print("* MoEDAL and CERN@school: make metadata schema *")
    print("*==============================================*")
    print("*")

    # Get the datafile path from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument("schemaFormat",    help="The format to make the metadata schema for.")
    #parser.add_argument("metadataPath",    help="Path to the input metadata schema JSON.")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    args = parser.parse_args()

    ## The data format to make the metadata schema for.
    schema_format = args.schemaFormat

    ## The path to the metadata schema.
    metadata_path = "metadata/%s/" % (schema_format.upper())
    #
    # Check if the path exists. If it doesn't, quit.
    if not os.path.isdir(metadata_path):
        raise IOError("* ERROR: Invalid data format '%s' - '%s' does not exist!" % (schema_format, metadata_path))

    # Set the logging level.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    # Configure the logging.
    lg.basicConfig(filename=os.path.join('./logfiles/', 'make_schema.log'), filemode='w', level=level)

    lg.info(" *")
    lg.info(" *================================================*")
    lg.info(" * MoEDAL and CERN@school: Making metadata schema *")
    lg.info(" *================================================*")
    lg.info(" *")
    lg.info(" * Data format to be processed : '%s'" % (schema_format))
    lg.info(" * Making schema files in      : '%s'" % (metadata_path))
    lg.info(" *")

    ## The name of the module containing the metadata schema wrapper class.
    module_name = "wrapmeta.%smeta" % (schema_format.lower())

    try:
        m = importlib.import_module(module_name)
    except ImportError, e:
        print("* ERROR: Invalid data format '%s' - %s." % (schema_format, str(e).lower()))

    # Make the HTML schema files.
    html_path = m.the_schema.make_html_schema(metadata_path)
    print("* HTML schema created in '%s'. Type:" % (html_path))
    print("*")
    print("* $ firefox %s &" % (html_path))
    print("*")
    print("* to view it.")
    print("*")

    # Make the LaTeX schema document files.
    latex_path, process_path = m.the_schema.make_tex_schema(metadata_path)
    print("* LaTeX schema created in '%s'. Type:" % (latex_path))
    print("*")
    print("* $ cd %s" % (metadata_path))
    print("* $ . process.sh")
    print("* $ qpdfview schema.pdf &")
    print("*")
    print("* to process and view it.")
    print("*")

    # Make the MarkDown schema file.
    md_path = m.the_schema.make_markdown_schema(metadata_path)
    print("* MarkDown schema created in '%s'." % (md_path))

    lg.info(" *")
    print("*")
