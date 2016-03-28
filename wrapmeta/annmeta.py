#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MoEDAL and CERN@school: Metadata schema object for the ANN data format.
"""

# For the metadata schema objects.
from wrapmeta.schema import MetadataSchema

## Metadata schema for the [...].
the_schema = MetadataSchema("The MoEDAL NTD TASL scan Zooniverse subject annotation data")

# Set the data format code.
the_schema.set_format("ANN")

## An overview of the schema.
overview = \
"""This data format describes the annotation data extracted from
the Zooniverse Panoptes project classification CSV dumps from
Monopole Quest! on a per-subject basis.
"""
#
the_schema.set_overview(overview)

## A description of what each record represents.
records_description = \
"""Each record described by this metadata schema represents
a CSV file containing the annotations extracted for a given
subject image as uploaded to the Zooniverse/Panoptes
Monopole Quest! project. Each classification has an
annotation ID formed of the user ID number (logged on users)
or IP address (non-logged on users) and the timestamp of the
classification (which makes the annotation ID unique),
and the annotation JSON itself.
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
        "name"       : "Workflow ID",
        "field_name" : "workflow_id",
        "format"     : "Two integers seperated by a decimal point (major and minor version)",
        "definition" : """The ID (major and minor version number)
of the workflow used to create the classification.""",
        "required"   : True,
        "order"      : 1
    }

    )
the_schema.add_element(
    {
        "name"       : "Number of annotations",
        "field_name" : "n_annotations",
        "format"     : "An integer",
        "definition" : """The number of annotations extracted for the subject.""",
        "required"   : True,
        "order"      : 2
    }
    )
