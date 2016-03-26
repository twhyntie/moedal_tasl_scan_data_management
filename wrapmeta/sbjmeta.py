#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MoEDAL and CERN@school: Metadata schema object for the SBJ data format.
"""

# For the metadata schema objects.
from wrapmeta.schema import MetadataSchema

## Metadata schema for the [...].
the_schema = MetadataSchema("The MoEDAL NTD TASL scan Zooniverse subject images")

# Set the data format code.
the_schema.set_format("SBJ")

## An overview of the schema.
overview = \
"""This data format describes the images extracted from
the Nuclear Track Detector (NTD) scan images provided
by TASL for use as subjects in Zooniverse/Panoptes
Citizen Science projects.
"""
#
the_schema.set_overview(overview)

## A description of what each record represents.
records_description = \
"""Each record represented by this metadata schema
represents an image file extracted from the scans of
the Nuclear Track Detector (NTD) plastic sheets.
Each image focusses on an accepted 'track' (pit)
identified by TASLs discrimination filters.
The position coordinates of each point in the plastic
are also recorded in the image.
After extraction from the raw bitmap,
the images are scaled up by a factor of 6
(with no interpolation or smoothing)
to make them large enough for the Panoptes
user interface.
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
        "name"       : "Scan ID",
        "field_name" : "scan_id",
        "format"     : "A string.",
        "definition" : """The ID of the scan to which the image belongs.""",
        "required"   : True,
        "order"      : 1
    }
    )

the_schema.add_element(
    {
        "name"       : "Batch ID",
        "field_name" : "batch_id",
        "format"     : "A string.",
        "definition" : """The ID of the batch to which the scan belongs.""",
        "required"   : True,
        "order"      : 2
    }
    )

the_schema.add_element(
    {
        "name"       : "Experiment",
        "field_name" : "experiment",
        "format"     : "A string.",
        "definition" : """The experiment to which the data belongs.""",
        "required"   : True,
        "order"      : 3
    }
    )

the_schema.add_element(
    {
        "name"       : "Owner",
        "field_name" : "owner",
        "format"     : "A string.",
        "definition" : """The owner of the data.""",
        "required"   : True,
        "order"      : 4
    }
    )

the_schema.add_element(
    {
        "name"       : "Data format",
        "field_name" : "data_format",
        "format"     : "A three-letter string.",
        "definition" : """The data format code (with respect to the data management plan).""",
        "required"   : True,
        "order"      : 5
    }
    )

the_schema.add_element(
    {
        "name"       : "Filename",
        "field_name" : "filename",
        "format"     : "A POSIX compliant filename (string).",
        "definition" : """The filename of the file represented by the record.""",
        "required"   : True,
        "order"      : 6
    }
    )

the_schema.add_element(
    {
        "name"       : "File format",
        "field_name" : "file_format",
        "format"     : "A string.",
        "definition" : """The file format of the image.""",
        "required"   : True,
        "order"      : 7
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
        "order"      : 8
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
        "order"      : 9
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
        "order"      : 10
    }
    )

the_schema.add_element(
    {
        "name"       : "Scan row",
        "field_name" : "scan_row",
        "format"     : "An integer.",
        "definition" : \
"""The TASL scan images contain multiple pit candidate images
arranged in a grid. This element records from which row the
subject image came.""",
        "required"   : True,
        "order"      : 11
    }
    )

the_schema.add_element(
    {
        "name"       : "Scan column",
        "field_name" : "scan_column",
        "format"     : "An integer.",
        "definition" : \
"""The TASL scan images contain multiple pit candidate images
arranged in a grid. This element records from which column the
subject image came.""",
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
