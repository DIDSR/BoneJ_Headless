#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from numpy import asarray
import nrrd
import csv 
import tempfile 
import os
import subprocess
import os 
from glob import glob 

out_dir1 = "/Thickness_Measurements/"
os.makedirs(out_dir1, exist_ok=True)

out_dir2 = "/Separation_Measurements/"
os.makedirs(out_dir2, exist_ok=True)

out_dir3 = "/Anisotropy_Measurements/"
os.makedirs(out_dir3, exist_ok=True)

out_dir4 = "/Area_VolumeFraction_Measurements/"
os.makedirs(out_dir4, exist_ok=True)

out_dir5 = "/Connectivity_Measurements/"
os.makedirs(out_dir5, exist_ok=True)

 out_dir6 = "/Ellipsoid_Factor/"
 os.makedirs(out_dir6, exist_ok=True)


ROIDir = "/BoneJ_Headless/ROIs"



ROINRRD = glob(ROIDir+"*.nrrd")


for txt in ROINRRD:
    NAME = os.path.basename(txt).replace(".nrrd","")

import BoneJ_Demo_Script_Area_VolumeFraction
import BoneJ_Demo_Script_Thickness
import BoneJ_Demo_Script_Separation
import BoneJ_Demo_Script_Anisotropy
import BoneJ_Demo_Script_Connectivity



