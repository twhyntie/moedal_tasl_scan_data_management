#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The usual suspect(s).
import os

#...for the logging.
import logging as lg

class SchemaElement(object):
    """
    Wrapper class for a metadata schema element.
    """

    def __init__(self, name, **kwargs):

        """ Constructor. """

        ## The schema element name.
        self.__name = name

        ## The field (element) name.
        self.__field_name = name.replace(" ","_").lower().strip(".")
        #
        if "field_name" in kwargs.keys():
            self.__field_name = kwargs["field_name"]

        ## The element definition.
        self.__definition = None
        #
        if "definition" in kwargs.keys():
            self.__definition = kwargs["definition"]

        # The format of the element.
        self.__format = None
        #
        if "element_format" in kwargs.keys():
            self.__format = kwargs["element_format"]

        ## The units associated with the element.
        self.__units = None
        #
        if "units" in kwargs.keys():
           self.__units = kwargs["units"]

        ## Is the element required by the schema?
        self.__required = False
        #
        if "required" in kwargs.keys():
            self.__required = bool(kwargs["required"])

    def get_name(self):
        return self.__name
    def get_field_name(self):
        return self.__field_name
    def has_definition(self):
        return self.__definition != None
    def get_definition(self):
        return self.__definition
    def has_format(self):
        return self.__format != None
    def get_format(self):
        return self.__format
    def set_units(self, units):
        self.__units = units
    def has_units(self):
        return self.__units != None
    def get_units(self):
        return self.__units
    def is_required(self):
        return self.__required


class MetadataSchema(object):
    """
    Wrapper class for a metadata schema.
    """

    def __init__(self, name):

        """ Constructor. """

        ## The schema name.
        self.__name = name

        ## The data format code.
        self.__format = None

        ## The schema overview text.
        self.__overview = None

        ## The schema records description.
        self.__description = None

        ## A dictionary of the schema elements.
        #
        # {order:SchemaElement}
        self.__elements = {}

        lg.info(" * Initialising a MetadataSchema object for '%s'." % (self.__name))
        lg.info(" *")

    def set_format(self, fmt):
        self.__format = fmt

    def set_overview(self, ovw):
        self.__overview = ovw.replace("\n"," ")

    def set_records_description(self, records_description):
        self.__records_description = records_description.replace("\n"," ")

    def add_element(self, el):

        if el["order"] in self.__elements.keys():
            raise KeyError("* ERROR: Duplicate element order value!")

        try:
            self.__elements[el["order"]] = SchemaElement(\
                el["name"],\
                field_name=el["field_name"],\
                definition=el["definition"],\
                element_format=el["format"],\
                #units=el["units"],\
                required=el["required"]\
                )
        except KeyError, e:
            raise KeyError("* ERROR: Schema element has no '%s'" % (str(e)))

        if "units" in el.keys():
            self.__elements[el["order"]].set_units(el["units"])

    def get_csv_header_string(self):

        s = ""

        for i in sorted(self.__elements.keys()):

            s += self.__elements[i].get_field_name()

            if i + 1 < len(self.__elements): s += ","

        return s

    def make_html_schema(self, output_path):
        """ Creates an HTML page describing the element. """

        ## The HTML page string.
        s = """<!DOCTYPE html>
<html>
<body>
<h1>SCHEMA_NAME: Metadata Schema</h1>"""

        # Add the schema overview.
        if self.__overview is not None: s += """
<h2>Overview</h2>
<p>SCHEMA_OVERVIEW</p>"""

        # Add the description of the records.
        if self.__records_description is not None: s += """
<h2>The records</h2>
<p>SCHEME_RECORDS_DESCRIPTION</p>"""

        # Add the schema elements.
        if len(self.__elements) > 0:
            s += """
<h2>Elements</h2>
<p>Each record has the following elements (fields) of metadata associated with it:</p>
<ul>"""
            # Loop over the elements to create a list.
            for i in sorted(self.__elements.keys()):
                el = self.__elements[i]
                s += "  <li><a href='#%s'>%s</a> (<span style='font-family:Monospace'>%s</span>)</li>\n" % (el.get_field_name(), el.get_name().strip("."), el.get_field_name())
            s += """
</ul>
<p>The element details are provided in the tables below."""

            # Write out a table for each element and its properties.
            for i in sorted(self.__elements.keys()):
                el = self.__elements[i]
                s += """
<table>
"""
                s += "  <tr><td><a name='%s'><em>Name</em>:      </td><td>%s</td></tr>\n" % (el.get_field_name(), el.get_name())
                s += "  <tr><td><em>Field name</em>:</td><td style='font-family:Monospace'>%s</td></tr>\n" % (el.get_field_name())
                if el.has_definition():
                    s += "  <tr><td><em>Definition</em>:</td><td>%s</td>\n" % (el.get_definition())
                if el.has_units():
                    s += "  <tr><td><em>Units</em>:</td><td>%s</td>\n" % (el.get_units())
                if el.has_format():
                    s += "  <tr><td><em>Format</em>:</td><td>%s</td>\n" % (el.get_format())
                if el.is_required():
                    s += "  <tr><td><em>Required?</em></td><td>Yes.</td></tr>\n"
                else:
                    s += "  <tr><td><em>Required?</em></td><td>No.</td></tr>\n"

                s += """
</table>
<br />"""

        # Finish off the HTML page.
        s += """
</body>
</html>"""

        s = s.replace("SCHEMA_NAME", self.__name.strip("."))

        s = s.replace("SCHEMA_FORMAT", self.__format)

        s = s.replace("SCHEMA_OVERVIEW", self.__overview)

        s = s.replace("SCHEME_RECORDS_DESCRIPTION", self.__records_description)

        ## Path to the HTML schema.
        html_path = os.path.join(output_path, "schema.html")
        #
        # Write out the HTML schema.
        with open(html_path, "w") as sf:
            sf.write(s)

        return html_path


    def make_tex_schema(self, output_path):
        """ Create a TeX document for the metadata schema. """

        ## The string for the TeX file.
        s = """%
\\documentclass[12pt,a4paper]{article}
\\usepackage[pdftex]{hyperref}%
\\hypersetup{%
colorlinks=true,%
urlcolor=black,%
citecolor=black,%
linkcolor=black}
\\newcommand{\\bullettext}[1]{\\emph{#1}}
\\title{SCHEMA_NAME:\\\\
Metadata Schema}
\\begin{document}
\\maketitle
\\begin{abstract}
This document describes the metadata schema for
SCHEMA_NAME_IN_ABSTRACT.
\\end{abstract}
\\tableofcontents"""

        # Add the overview section.
        if self.__overview is not None: s += """
\\section{Overview}
\\label{sec:overview}
SCHEMA_OVERVIEW"""

        # Add the description of the records for each element.
        if self.__records_description is not None: s += """
\\section{The records}
\\label{sec:records}
SCHEME_RECORDS_DESCRIPTION"""

        # Add subsections for each element.
        if len(self.__elements) > 0:
            s += """
\\section{The elements}
\\label{sec:elements}"""

            s += """
The element details are provided in the following subsections."""

            # Write out a subsection for each element and its properties.
            for i in sorted(self.__elements.keys()):
                el = self.__elements[i]
                s += "\\subsection{%s}\n" % (el.get_name())
                s += "\\label{sec:%s}\n" % (el.get_field_name().replace("_",""))
                if el.has_definition():
                    s += "%s\n" % (el.get_definition())
                s += "\\begin{itemize}\n"
                s += "  \\item \\bullettext{Field name}: "
                s += "\\texttt{%s};\n" % (el.get_field_name().replace("_","\\_"))
                if el.has_units():
                    s += "  \\item \\bullettext{Units}: %s;\n" % (el.get_units().strip("."))
                if el.has_format():
                    s += "  \\item \\bullettext{Format}: %s;\n" % (el.get_format().strip(".").lower())
                s += "  \\item \\bullettext{Required?} "
                if el.is_required():
                    s += "Yes.\n"
                else:
                    s += "No.\n"
                s += "\\end{itemize}\n"
        s += """
\\end{document}
%"""

        s = s.replace("SCHEMA_NAME_IN_ABSTRACT", self.__name[0].lower() + self.__name.strip(".")[1:])

        s = s.replace("SCHEMA_NAME", self.__name.strip("."))

        s = s.replace("SCHEMA_FORMAT", self.__format)

        s = s.replace("SCHEMA_OVERVIEW", self.__overview)

        s = s.replace("SCHEME_RECORDS_DESCRIPTION", self.__records_description)

        #return s

        ## Path to the LaTeX schema.
        latex_path = os.path.join(output_path, "schema.tex")
        #
        # Write out the LaTeX schema.
        with open(latex_path, "w") as sf:
            sf.write(s)

        process_path = os.path.join(output_path, "process.sh")
        #
        with open(process_path, "w") as sf:
            sf.write("!/bin/bash\n")
            sf.write("pdflatex schema.tex\n")
            sf.write("pdflatex schema.tex\n")
            sf.write("pdflatex schema.tex")

        return latex_path, process_path

    def make_markdown_schema(self, output_path):
        """ Create a MarkDown document for the metadata schema. """

        ## The string for the MarkDown file.
        s = \
"""#<a name='top'>SCHEMA_NAME: Metadata Schema</a>

"""

        # Add the overview section.
        if self.__overview is not None: s += """
##Overview
SCHEMA_OVERVIEW
"""

        # Add the description of the records for each element.
        if self.__records_description is not None: s += """
##The records
SCHEME_RECORDS_DESCRIPTION
"""

        # Add subsections for each element.
        if len(self.__elements) > 0:
            s += """
##The elements
"""

            # Loop over the elements to create a list.
            for i in sorted(self.__elements.keys()):
                el = self.__elements[i]
                s += "* [%s](#%s) (`%s`)\n" % (el.get_name().strip("."), el.get_field_name(), el.get_field_name())
            s += """
The element details are provided in the subsections below.

"""

            # Write out a subsection for each element and its properties.
            for i in sorted(self.__elements.keys()):
                el = self.__elements[i]
                s += "###<a name='%s'>%s</a>\n" % (el.get_field_name(), el.get_name())
                if el.has_definition():
                    s += "%s\n" % (el.get_definition())
                s += "* _Field name_: `%s`\n" % (el.get_field_name())
                if el.has_units():
                    s += "* _Units_: %s\n" % (el.get_units().strip("."))
                if el.has_format():
                    s += "* _Format_: %s\n" % (el.get_format().strip(".").lower())
                s += "* _Required?_ "
                if el.is_required():
                    s += "Yes.\n"
                else:
                    s += "No.\n"
                s += "\n"
                s += "_Back to the [top](#top)._\n"
                s += "\n"

        s = s.replace("SCHEMA_NAME_IN_ABSTRACT", self.__name[0].lower() + self.__name.strip(".")[1:])

        s = s.replace("SCHEMA_NAME", self.__name.strip("."))

        s = s.replace("SCHEMA_FORMAT", self.__format)

        s = s.replace("SCHEMA_OVERVIEW", self.__overview)

        s = s.replace("SCHEME_RECORDS_DESCRIPTION", self.__records_description)

        ## Path to the MarkDown schema.
        md_path = os.path.join(output_path, "schema.md")
        #
        # Write out the MarkDown schema.
        with open(md_path, "w") as sf:
            sf.write(s)

        return md_path
