#<a name='top'>The MoEDAL NTD TASL scan Zooniverse subject annotation data: Metadata Schema</a>


##Overview
This data format describes the annotation data extracted from the Zooniverse Panoptes project classification CSV dumps from Monopole Quest! on a per-subject basis. 

##The records
Each record described by this metadata schema represents a CSV file containing the annotations extracted for a given subject image as uploaded to the Zooniverse/Panoptes Monopole Quest! project. Each classification has an annotation ID formed of the user ID number (logged on users) or IP address (non-logged on users) and the timestamp of the classification (which makes the annotation ID unique), and the annotation JSON itself. 

##The elements
* [ID](#id) (`id`)
* [Workflow ID](#workflow_id) (`workflow_id`)
* [Number of annotations](#n_annotations) (`n_annotations`)

The element details are provided in the subsections below.

###<a name='id'>ID</a>
The record ID.
* _Field name_: `id`
* _Format_: a string
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='workflow_id'>Workflow ID</a>
The ID (major and minor version number)
of the workflow used to create the classification.
* _Field name_: `workflow_id`
* _Format_: two integers seperated by a decimal point (major and minor version)
* _Required?_ Yes.

_Back to the [top](#top)._

###<a name='n_annotations'>Number of annotations</a>
The number of annotations extracted for the subject.
* _Field name_: `n_annotations`
* _Format_: an integer
* _Required?_ Yes.

_Back to the [top](#top)._

