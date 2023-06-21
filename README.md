
BoneJ Headless Scripts for Python 
===========

***BoneJ Headless Python Wrapper Scripts for Bone Morphological Analysis***

Microstructure metrics are calculated to characterize bone morphology and skeletal geometry. BoneJ is a Fiji plugin for calculating microstrucutre metrics with unique plugins not available from commercial scanners. The plugins can be automated with simple Fiji macros, but this still requires some GUI dependence that prevents complete automation of all functionalities. This repository allows for automation of BoneJ without GUI dependence and can allow for quick processing of large datasets, access to Python libraries, and scripts to optimize input parameters for specific metrics. The plugins were used to compute micorstructure metrics for several microCT images of lumbar vertebrae. All scripts are written in Python and can only be executed on Linux OS. For testing purposes an image of a trabecular bone from a shrew was included. 

* **Citation:** Domander, Richard, Alessandro A. Felder, and Michael Doube. "BoneJ2-refactoring established research software." Wellcome Open Research 6 (2021).
Domander, Richard, Alessandro A. Felder, and Michael Doube. "BoneJ2-refactoring established research software." Wellcome Open Research 6 (2021).


* **Documentation**: Full documentation can be found here: https://bonej-headless.readthedocs.io/en/latest/index.html

**Note**: All code is under CC0 (Creative Commons 1.0 Universal License) 

*BoneJ Headless team: Harsha Marupudi, M.Eng., Qian Cao, Ph.D. 
US Food and Drug Administration, Center for Devices and Radiological Health, Office of Science and Engineering Labs, Division of Imaging, Diagnostics, and Software Reliability.*

Disclaimer
----------

This software and documentation was developed at the Food and Drug Administration (FDA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17, Section 105 of the United States Code, this work is not subject to copyright protection and is in the public domain. Permission is hereby granted, free of charge, to any person obtaining a copy of the Software, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, or sell copies of the Software or derivatives, and to permit persons to whom the Software is furnished to do so. FDA assumes no responsibility whatsoever for use by other parties of the Software, its source code, documentation or compiled executables, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. Further, use of this code in no way implies endorsement by the FDA or confers any advantage in regulatory decisions. Although this software can be redistributed and/or modified freely, we ask that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified. 

BoneJ Headless Plugins
-------------------
The code included in this repository will allow you to compute these common microstructure metrics:

1. Thickness
2. Spacing
3. Anisotropy
4. Ellipsoid Factor
5. Bone Volume Fraction 
6. Connectivity

Secondary metrics not as commonly used in literature are also included here: 
1. Intertrabecular Angles 
2. Skeletonize 
3. Analyze Skeleton 
4. Fractal Dimension
5. Surface Area

Functions can be used for batch processing or processing only one input image. BoneJ Headless takes binary numpy arrays as inputs. 
  
Installation
------------

Before proceeding, make sure you have all the requirements listed above.

Fiji can be installed from the [official website](https://imagej.net/software/fiji/downloads). 
BoneJ must be added as a plugin within the Fiji installation. Instructions can be found from the [official website](https://imagej.net/plugins/bonej#installation).

Clone the repository 

`git clone https://github.com/BoneJ_Headless`

Install the required python libraries. 

`pip install -r requirements.txt`

Usage
-----

First try BoneJ_Module.py to load and run metrics on a single image. You can import any of the available metrics and adjust input paremeters.:

`BoneJ_Module_Example.py`

> You might need to use `python3` instead of `python`.

Each example requires an input and output directory to set by the user, along with the voxel size of the image, and the Fiji directory path. 

> All ``example ROIs`` are acompanied by an ``.nrrd``. The ``.nrrd`` file can be opened in the Fiji softwrae as well. 
Documentation
-------------

Full documentation can be found here:https://bonej-headless.readthedocs.io/en/latest/index.html#

*This code is currently in development, use with caution.*


