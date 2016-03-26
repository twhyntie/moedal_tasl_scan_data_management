#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

 CERN@school and MoEDAL - Extracting the annotation information.

 See the README.md file and the GitHub wiki for more information.

 http://moedal.web.cern.ch

"""

# Import the code needed to manage files.
import os, glob

#...for parsing the arguments.
import argparse

#...for the logging.
import logging as lg

#...for the data, sweet DATA.
import csv, json

#...for the time (being).
import time, calendar

if __name__ == "__main__":

    print("*")
    print("*=====================================*")
    print("* CERN@school and MoEDAL: Extract ANN *")
    print("*=====================================*")

    # Get the datafile path from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument("dataPath",        help="Path to the classification dump CSV file.")
    parser.add_argument("outputPath",      help="The path for the output files.")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    args = parser.parse_args()

    ## The path to the data.
    data_path = args.dataPath
    #
    if not os.path.exists(data_path):
        raise IOError("* ERROR: Unable to find classification data at '%s'." % (data_path))

    ## The output path.
    output_path = os.path.join(args.outputPath, "ANN/data")
    #
    # Check if the output directory exists.
    if not os.path.isdir(output_path):
        raise IOError("* ERROR: '%s' output directory does not exist!" % (output_path))

    ## The subject path.
    subject_path = os.path.join(args.outputPath, "SBJ/data")
    #
    # Check if the subject directory exists.
    if not os.path.isdir(subject_path):
        raise IOError("* ERROR: '%s' subject directory does not exist!" % (subject_path))
    # Set the logging level.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    # Configure the logging.
    lg.basicConfig(filename=os.path.join('logfiles', 'extract_ann.log'), filemode='w', level=level)

    print("*")
    print("* CSV path          : '%s'" % (data_path))
    print("* Writing to        : '%s'" % (output_path))
    print("*")

    lg.info(" *")
    lg.info(" *=============================================*")
    lg.info(" * MoEDAL and CERN@school: Extract annotations *")
    lg.info(" *=============================================*")
    lg.info(" *")
    lg.info(" * CSV path   : '%s'" % (data_path))
    lg.info(" * Writing to : '%s'" % (output_path))
    lg.info(" *")

    ## Dictionary of subject annotations.
    #
    # {subject_id:dictionary of annotations}.
    sub_ann_dict = {}

    # Loop over the subjects in the SBJ directory.
    for i, path in enumerate(sorted(glob.glob(os.path.join(subject_path, "*.png")))):

        ## The subject ID.
        sub_id = os.path.basename(path)[:-4]

        # Add an (empty) annotation dictionary for each subject.
        # The annotation dictionary format: {user_id:annotation JSON}
        sub_ann_dict[sub_id] = {}

        lg.info(" * Found subject with ID: '%s'" % (sub_id))

    lg.info(" *")

    # Read in the classification dump CSV file.
    with open(data_path, "r") as df:

        ## The CSV file reader.
        reader = csv.reader(df)

        # Loop over the rows of the CSV file via the reader.
        for i, row in enumerate(reader):
            if i == 0:
                # Extract the header information.
                headers = row
            else:
                # Extract the data.

                # Check if the workflow is the correct version.
                #
                ## The workflow version.
                workflow_v = row[5]

                #
                #lg.info(" * Workflow version: %s" % (workflow_version))
                #
                if workflow_v != "77.83":
                    continue

                # The User's ID.
                user_id = ""

                ## The time stamp the classification was created at (string).
                time_stamp_string = row[6]

                ## The UNIX time stamp the classification was created at (seconds).
                time_stamp_sec = calendar.timegm(time.strptime(time_stamp_string, "%Y-%m-%d %H:%M:%S %Z"))

                ## The subject ID [image number]_[row]_[col].
                sub_id = json.loads(row[11]).values()[0]["id"]
                #
                # Note - this is temporary as the Monopole Quest! subject IDs
                # were in an old format.
                sub_id = sub_id.replace("00000","TASL000000_00")
                #lg.info(" *--> Subject ID: %s" % (sub_id))

                # Skip subjects that are not in our list.
                #if subject_id != sub_id: continue
                if sub_id not in sub_ann_dict.keys(): continue

                # Was the user logged in?
                if row[1] != "":
                    # For logged in users, use the User ID and the UNIX timestamp.
                    user_id = row[1] + ":%d" % (time_stamp_sec)
                else:
                    # For non-logged in users, use the User IP hash and UNIX timestamp.
                    user_id = row[2] + ":%d" % (time_stamp_sec)

                ## The annotation ID (should be unique!).
                anno_id = user_id

                #lg.info(" *--> Annotation ID: %s" % (anno_id))

                ## The annotation.
                anno = row[10]

                # Add the annotation to the dictionary.
                if anno_id in sub_ann_dict[sub_id].keys():
                    lg.error(" * ERROR!")
                    lg.error(" * User ID: %s" % (user_id))
                    lg.error(" * Subject: %s" % (subject_id))
                    raise IOError("* ERROR: The same user has classified the same subject twice!")
                else:
                    sub_ann_dict[sub_id][anno_id] = anno

                #break

    ## The total number of annotations of the right workflow.
    total_annotations = 0

    for sub_id in sorted(sub_ann_dict.keys()):

        ## String for the annotation CSV file.
        acs = "annotation_id,annotation\n"

        # Loop over the annotations.
        for i, anno_id in enumerate(sorted(sub_ann_dict[sub_id].keys())):
            acs += "%s,%s" % (anno_id, sub_ann_dict[sub_id][anno_id])
            if i < len(sub_ann_dict[sub_id]): acs += "\n"

        ## ANN filename.
        ann_path = os.path.join(output_path, "%s.csv" % (sub_id))

        with open(ann_path, "w") as cf:
            cf.write(acs)

        ## The number of annotations for the subject.
        num_annos = len(sub_ann_dict[sub_id])
        #
        total_annotations += num_annos

        lg.info(" * Number of annotations for %s : %d" % (sub_id, num_annos))

    lg.info(" *")
    lg.info(" * Total annotations: % 6d" % (total_annotations))
    lg.info(" *")
