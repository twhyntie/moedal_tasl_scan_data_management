#<a name='top'>The MoEDAL NTD TASL scan Zooniverse subject images: Metadata Schema</a>


##Overview
This data format describes the images extracted from the Nuclear Track Detector (NTD) scan images provided by TASL for use as subjects in Zooniverse/Panoptes Citizen Science projects. 

##The records
Each record represented by this metadata schema represents an image file extracted from the scans of the Nuclear Track Detector (NTD) plastic sheets. Each image focusses on an accepted 'track' (pit) identified by TASLs discrimination filters. The position coordinates of each point in the plastic are also recorded in the image. After extraction from the raw bitmap, the images are scaled up by a factor of 6 (with no interpolation or smoothing) to make them large enough for the Panoptes user interface. 

##The elements
* [ID](#id) (`id`)
* [Scan ID](#scan_id) (`scan_id`)
* [Batch ID](#batch_id) (`batch_id`)
* [Experiment](#experiment) (`experiment`)
* [Owner](#owner) (`owner`)
* [Data format](#data_format) (`data_format`)
* [Filename](#filename) (`filename`)
* [File format](#file_format) (`file_format`)
* [File size](#file_size) (`file_size`)
* [Image width](#image_width) (`image_width`)
* [Image height](#image_height) (`image_height`)
* [Scan row](#scan_row) (`scan_row`)
* [Scan column](#scan_column) (`scan_column`)
* [Scan magnification](#magnification) (`magnification`)

The element details are provided in the subsections below.

###<a name='id'>ID</a>
The record ID.
* _Field name_: `id`
* _Format_: a string
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='scan_id'>Scan ID</a>
The ID of the scan to which the image belongs.
* _Field name_: `scan_id`
* _Format_: a string
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='batch_id'>Batch ID</a>
The ID of the batch to which the scan belongs.
* _Field name_: `batch_id`
* _Format_: a string
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='experiment'>Experiment</a>
The experiment to which the data belongs.
* _Field name_: `experiment`
* _Format_: a string
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='owner'>Owner</a>
The owner of the data.
* _Field name_: `owner`
* _Format_: a string
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='data_format'>Data format</a>
The data format code (with respect to the data management plan).
* _Field name_: `data_format`
* _Format_: a three-letter string
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='filename'>Filename</a>
The filename of the file represented by the record.
* _Field name_: `filename`
* _Format_: a posix compliant filename (string)
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='file_format'>File format</a>
The file format of the image.
* _Field name_: `file_format`
* _Format_: a string
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='file_size'>File size</a>
The size of the file represented by the record in bytes.
* _Field name_: `file_size`
* _Units_: bytes
* _Format_: an integer
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='image_width'>Image width</a>
The width of the image in pixels.
* _Field name_: `image_width`
* _Units_: pixels
* _Format_: an integer
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='image_height'>Image height</a>
The height of the image in pixels.
* _Field name_: `image_height`
* _Units_: pixels
* _Format_: an integer
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='scan_row'>Scan row</a>
The TASL scan images contain multiple pit candidate images
arranged in a grid. This element records from which row the
subject image came.
* _Field name_: `scan_row`
* _Format_: an integer
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='scan_column'>Scan column</a>
The TASL scan images contain multiple pit candidate images
arranged in a grid. This element records from which column the
subject image came.
* _Field name_: `scan_column`
* _Format_: an integer
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='magnification'>Scan magnification</a>
The magnification at which the scan was taken.
* _Field name_: `magnification`
* _Format_: a floating point number
* _Required?_ Yes.

_Back to the [top](#top)._

