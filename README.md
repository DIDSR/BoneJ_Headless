
BoneJ Headless Scripts for Python 
===========
![](https://bonej.org/images/thickness.png)\
***Bone J Headless Python Wrapper Scripts for Bone Morphological Analysis***

Microstructural metrics are calculated to characterize bone morphology and skeletal geometry. BoneJ is a Fiji plugin for calculation of microstructural metrics and bone analysis with unique plugins not available from vendors. The plugins can be automated with simple Fiji macros, but this still requires GUI support. This repository allows for automation of BoneJ without GUI dependence and can allow for quick processing of large datasets, access to Python libraries, and a simple method of parameter sweeping to optimize BoneJ plugins. The Division of Imaging, Diagnostics, and Software Reliability (DIDSR) at the U.S. Food and Drug Administration developed BoneJ Headless a Python wrapper that automates BoneJ without any GUI dependence. This plugin was used on several microCT images and compared to microstructural metrics from other sources. All scripts are written in Python and can only be executed on Linux OS. 

* **Citation:** Domander, Richard, Alessandro A. Felder, and Michael Doube. "BoneJ2-refactoring established research software." Wellcome Open Research 6 (2021).
Domander, Richard, Alessandro A. Felder, and Michael Doube. "BoneJ2-refactoring established research software." Wellcome Open Research 6 (2021).


* **Documentation**: Full documentation can be found here: https://github.com/harshamarupudi56/BoneJ_Headless/blob/main/BoneJ%20Documentation.docx

**Note**: All code is under CC0 (Creative Commons 1.0 Universal License) 

*BoneJ Headless team: Harsha Marupudi, M.Eng., Qian Cao, Ph.D. US Food and Drug Administration, Center for Devices and Radiological Health, Office of Science and Engineering Labs, Division of Imaging, Diagnostics, and Software Reliability.*

Disclaimer
----------

This software and documentation (the "Software") were developed at the Food and Drug Administration (FDA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17, Section 105 of the United States Code, this work is not subject to copyright protection and is in the public domain. Permission is hereby granted, free of charge, to any person obtaining a copy of the Software, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, or sell copies of the Software or derivatives, and to permit persons to whom the Software is furnished to do so. FDA assumes no responsibility whatsoever for use by other parties of the Software, its source code, documentation or compiled executables, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. Further, use of this code in no way implies endorsement by the FDA or confers any advantage in regulatory decisions. Although this software can be redistributed and/or modified freely, we ask that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified. 

BoneJ Headless Plugisn
-------------------
The code included in this repository will allow you to execute these common microstructural metrics:

1. Trabecular Thickness
2. Trabecular Spacing
3. Anisotropy
4. Ellipsoid Factor
5. Area Volume Fraction 
6. Connectivity

Scripts can be launched individually through use of modules and functions or as a batch scripts. Acceptable file types include NRRD, NIfTI, and DICOM. All files must be 3D 8 bit images. 

Requirements
------------
dependencies:
  - python=3.7
  - numpy
  - scipy
  - numba
  - mkl
  - matplotlib
  - scikit-image
  - scikit-learn
  - spyder
  - ipython
  - glob2
  - pip:
    - pynrrd # image/data file formats
    - pydicom
    - h5py
    - nibabel
    - python-csv
    - temp
    - sys
    - os
    - subprocess
  
Installation
------------

Before proceeding, make sure you have all the requirements listed above.

Fiji can be installed from the [official website](https://imagej.net/software/fiji/downloads). 
BoneJ must be added as a plugin within the Fiji installation. Instructions can be found from the [official website](https://imagej.net/plugins/bonej#installation).

Clone the repository 

`git clone https://github.com/BoneJ_Headless`

Execute the installation script:

`source install.sh`

Install the required python libraries. 

Usage
-----

First try BoneJ_Module.py to launch individual metrics on a single image:

`BoneJ_Module.py`

> You might need to use `python3` instead of `python`.

Each example requires an input and output directory to set by the user, along with the voxel size of the image, and the Fiji directory path. 

> All ``image segmentation`` files are acompanied by an ``.nrrd``. The ``.nrrd`` file can be opened in software Fiji as well. 
Documentation
-------------

Full documentation can be found here:https://github.com/harshamarupudi56/BoneJ_Headless/blob/main/BoneJ%20Documentation.docx

*This code is currently in development, use with caution.*
