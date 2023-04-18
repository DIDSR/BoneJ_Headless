.. _bonej-installation-label:

Installation
===============

Requirements
------------

dependencies:

*python=3.7

*numpy

*scipy

*numba

*mkl

*matplotlib

*scikit-image

*scikit-learn

*spyder

*ipython

*glob2

*pip:

*pynrrd # image/data file formats

*pydicom

*h5py

*nibabel

*python-csv

*temp

*sys

*os

*subprocess

Installation
------------

Before proceeding, make sure you have all the requirements listed above.

Fiji can be installed here: https://imagej.net/software/fiji/downloads. 
BoneJ must be added as a plugin within the Fiji installation. 

1. Launch Fiji
2. From the menu select Help › Update…
3. Select manage update sites
4. Select BoneJ
5. Close manage update sites
6. Select Apply changes


Clone the repository 

`git clone https://github.com/BoneJ_Headless`

Execute the installation script:

`source install.sh`

Install the required python libraries. 

Usage
-----

First try BoneJ_Module.py located in Examples to launch individual metrics on a single image:

`BoneJ_Module.py`

> This example allows a user to load an ROI, after defining voxel size of the image, and the location of Fiji installation. Any of the plugins can be chosen and different parameter setttings can be selected for each individual microstructure metric.

> You might need to use `python3` instead of `python`.

Each example requires an input and output directory to set by the user, along with the voxel size of the image, and the Fiji directory path. 

> All ROIs are acompanied by an ``.nrrd``. The ``.nrrd`` file can be opened in Fiji/ImageJ as well. Any file type can be used as long as they are 3D binary 8 bit files. Files are read as numpy arrays by the plugins. 

*This code is currently in development, use with caution.*
