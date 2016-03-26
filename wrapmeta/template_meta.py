#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MoEDAL and CERN@school: Metadata schema template.
"""

# For the metadata schema objects.
from wrapmeta.schema import MetadataSchema

## Metadata schema for the [...].
the_schema = MetadataSchema("[Data format name (verbose)]")

# Set the data format code.
the_schema.set_format("AAA")

## An overview of the schema.
overview = \
"""[OVERVIEW HERE].
"""
#
the_schema.set_overview(overview)

## A description of what each record represents.
records_description = \
"""[DESCRIPTION HERE].
"""
#
the_schema.set_records_description(records_description)

# Add the schema elements.
the_schema.add_element(
    {
        "name"       : "",
        "field_name" : "",
        "format"     : "",
        "definition" : """""",
        "required"   : , # Boolean.
        "order"      : # Int
    }
    )
