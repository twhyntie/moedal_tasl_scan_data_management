#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

 CERN@school and MoEDAL - Converting TASL NTD scans: RAW -> SBJ.

 See the README.md file and the GitHub wiki for more information.

 http://moedal.web.cern.ch

"""

# Import the code needed to manage files.
import os, glob

#...for parsing the arguments.
import argparse

#...for the logging.
import logging as lg

#...for the plotting.
import matplotlib.pyplot as plt

#...for the image conversions.
import Image

#...for the image manipulation.
import matplotlib.image as mpimg

#...for the MATH.
import numpy as np

#...for the image scaling.
import scipy.ndimage.interpolation as inter

if __name__ == "__main__":

    print("*")
    print("*====================================*")
    print("* CERN@school and MoEDAL: RAW -> SBJ *")
    print("*====================================*")

    # Get the datafile path from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument("dataPath",        help="Path to the data to catalogue.")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    args = parser.parse_args()

    ## The path to the data.
    data_path = os.path.join(args.dataPath, "RAW/data")
    #
    if not os.path.isdir(data_path):
        raise IOError("* ERROR: Unable to find data at '%s'." % (data_path))

    ## The output path.
    output_path = os.path.join(args.dataPath, "SBJ/data")
    #
    # Check if the output directory exists. If it doesn't, make it.
    if not os.path.isdir(output_path):
        raise IOError("* ERROR: '%s' output directory does not exist!" % (output_path))

    # Set the logging level.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    # Configure the logging.
    lg.basicConfig(filename=os.path.join('logfiles', 'convert_raw_to_sbj.log'), filemode='w', level=level)

    print("*")
    print("* Data path         : '%s'" % (data_path))
    print("* Writing to        : '%s'" % (output_path))
    print("*")

    ## The scale factor.
    scale = 6.0

    ## A list of te data entities found in RAW/data.
    entity_list = glob.glob(os.path.join(data_path, "*.bmp"))

    # Loop through the scan BMP files found.
    for f in sorted(entity_list):

        ## The base name.
        bn = os.path.basename(f)

        ## The image ID.
        image_id = "TASL" + bn[3:12]

        print image_id

        ## The new PNG file base name.
        new_bn = "%s.png" % (bn.split(".")[0])

        ## The path to the new file.
        new_path = os.path.join(output_path, new_bn)

        print("* Converting '%s' -> '%s'." % (bn, new_path))

        ## The image as a NumPy array.
        img = mpimg.imread(f)
        #img = mpimg.imread(datapath)

        lg.info(" * Image '%s' dimensions: %s" % (bn, str(img.shape)))

        # Note that for the first images, the row and column limits
        # had to be hard-coded as the images were not split/joined
        # in a uniform manner. It still works though! :-)

        ## The row limits.
        row_limits = [65, 129, 194, 258, 323, 387, 452, 516]

        ## The column limits.
        col_limits = [1, 66, 130, 195, 259, 324, 389, 453, 518, 582, 647, 711]

        lg.info(" * Row    limits: %s" % str(row_limits))
        lg.info(" * Column limits: %s" % str(col_limits))

        # Split the montage into rows.
        row_imgs = np.split(img, row_limits)

        # Loop over the rows.
        for i, row_im in enumerate(row_imgs):

            # Split the row into the images.
            imgs = np.split(row_im, col_limits, axis=1)

            ## A vertical black line - artefact of the montage process?
            vert_line = imgs[0]

            # Remove the black line at the start of the row...
            imgs = imgs[1:]

            #...and add it to the last image.
            imgs[11] = np.concatenate((imgs[11], vert_line), axis=1)

            # Loop over the images.
            for j, img in enumerate(imgs):

                ## The scaled image - no interpolation or pre-filtering.
                zoom_img = inter.zoom(img, (scale, scale, 1.0), order=0, prefilter=False)

                # Save the images.
                mpimg.imsave(os.path.join(output_path, "%s_%02d_%02d.png" % (image_id, i, j)), zoom_img)
