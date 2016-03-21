#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MoEDAL and CERN@school: The MoEDAL TASL Raw Scan Images metadata schema.
"""

# For the metadata schema objects.
from wrapmeta.schema import MetadataSchema

## Metadata schema for the TASL raw scan images.
the_schema = MetadataSchema("The MoEDAL TASL Raw Scan Images")

# Set the data format.
the_schema.set_format("RAW")

## An overview of the schema.
overview = \
"""This data format describes the raw scan images
of the Nuclear Track Detector (NTD) sheets
provided by TASL."""
#
the_schema.set_overview(overview)

## A description of what each record represents.
records_description = \
"""Each record represented by this metadata schema
represents an image file provided by TASL.
Each image is a montage of all accepted 'tracks' (pits)
and their position coordinates from a particular
scan after TASL's discrimination filters have been applied.
"""
#
the_schema.set_records_description(records_description)

# Add the schema elements.
the_schema.add_element(
    {
        "name"       : "ID",
        "field_name" : "id",
        "format"     : "A string.",
        "definition" : "The record ID.",
        "required"   : True,
        "order"      : 0
    }
    )

the_schema.add_element(
    {
        "name"       : "Batch ID",
        "field_name" : "batch_id",
        "format"     : "A string.",
        "definition" : """The ID of the batch to which the scan belongs.""",
        "required"   : True,
        "order"      : 1
    }
    )

the_schema.add_element(
    {
        "name"       : "Experiment",
        "field_name" : "experiment",
        "format"     : "A string.",
        "definition" : """The experiment to which the data belongs.""",
        "required"   : True,
        "order"      : 2
    }
    )

the_schema.add_element(
    {
        "name"       : "Owner",
        "field_name" : "owner",
        "format"     : "A string.",
        "definition" : """The owner of the data.""",
        "required"   : True,
        "order"      : 3
    }
    )

the_schema.add_element(
    {
        "name"       : "Filename",
        "field_name" : "filename",
        "format"     : "A POSIX compliant filename (string).",
        "definition" : """The filename of the file represented by the record.""",
        "required"   : True,
        "order"      : 4
    }
    )

the_schema.add_element(
    {
        "name"       : "File format",
        "field_name" : "file_format",
        "format"     : "A string.",
        "definition" : """The file format of the image.""",
        "required"   : True,
        "order"      : 5
    }
    )

the_schema.add_element(
    {
        "name"       : "Data format",
        "field_name" : "data_format",
        "format"     : "A three-letter string.",
        "definition" : """The data format code (with respect to the data management plan).""",
        "required"   : True,
        "order"      : 6
    }
    )

the_schema.add_element(
    {
        "name"       : "Image width",
        "field_name" : "image_width",
        "format"     : "An integer.",
        "units"      : "pixels",
        "definition" : """The width of the image in pixels.""",
        "required"   : True,
        "order"      : 7
    }
    )

the_schema.add_element(
    {
        "name"       : "Image height",
        "field_name" : "image_height",
        "format"     : "An integer.",
        "units"      : "pixels",
        "definition" : """The height of the image in pixels.""",
        "required"   : True,
        "order"      : 8
    }
    )

the_schema.add_element(
    {
        "name"       : "File size",
        "field_name" : "file_size",
        "format"     : "An integer.",
        "units"      : "bytes",
        "definition" : """The size of the file represented by the record in bytes.""",
        "required"   : True,
        "order"      : 9
    }
    )

the_schema.add_element(
    {
        "name"       : "Number of individual scan rows",
        "field_name" : "n_scan_rows",
        "format"     : "An integer.",
        "definition" : \
"""The TASL scan images contain multiple pit candidate images
arranged in a table. This element records the number of rows
in the file.""",
        "required"   : True,
        "order"      : 10
    }
    )

the_schema.add_element(
    {
        "name"       : "Number of individual scan columns",
        "field_name" : "n_scan_columns",
        "format"     : "An integer.",
        "definition" : \
"""The TASL scan images contain multiple pit candidate images
arranged in a table. This element records the number of rows
in the file.""",
        "required"   : True,
        "order"      : 11
    }
    )

the_schema.add_element(
    {
        "name"       : "Number of individual scan images",
        "field_name" : "n_scans",
        "format"     : "An integer.",
        "definition" : \
"""The TASL scan images contain multiple pit candidate images
arranged in a table. This element records the number of scans
in the file. Note that this will not necessarily be the
rows multiplied by the columns as not every space in the
table is full.""",
        "required"   : True,
        "order"      : 12
    }
    )

the_schema.add_element(
    {
        "name"       : "Scan magnification",
        "field_name" : "magnification",
        "format"     : "A floating point number.",
        "definition" : """The magnification at which the scan was taken.""",
        "required"   : True,
        "order"      : 13
    }
    )
