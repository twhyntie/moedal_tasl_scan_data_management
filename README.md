# MoEDAL TASL Scans: Data Management

This is a repository for managing data from the MoEDAL TASL
Nuclear Track Detector (NTD) scans.

##Getting started

To create the metadata schema, type:

```bash
$ python make_scheme.py [FORMAT_CODE]
```

where `[FORMAT_CODE]` is the data format for which you want to
create the metadata schema.

##Supported formats

* `RAW`: the raw TASL scan images.
