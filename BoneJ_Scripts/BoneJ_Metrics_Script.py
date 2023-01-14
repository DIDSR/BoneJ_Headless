#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from numpy import asarray
import nrrd
import csv 
import tempfile 
import os
import subprocess
import pandas as pd 
import os 
from glob import glob 

out_dir1 = "/gpfs_projects/sriharsha.marupudi/Thickness_Measurements_Print_40"
os.makedirs(out_dir1, exist_ok=True)

out_dir2 = "/gpfs_projects/sriharsha.marupudi/Spacing_Measurements_Print_40"
os.makedirs(out_dir2, exist_ok=True)

out_dir3 = "/gpfs_projects/sriharsha.marupudi/Anisotropy_Measurements_MIL_L1_100"
os.makedirs(out_dir3, exist_ok=True)

out_dir4 = "/gpfs_projects/sriharsha.marupudi/Area_VolumeFraction_Measurements_Print_40"
os.makedirs(out_dir4, exist_ok=True)

out_dir5 = "/gpfs_projects/sriharsha.marupudi/Connectivity_Measurements_Print_40"
os.makedirs(out_dir5, exist_ok=True)

 out_dir6 = "/gpfs_projects/sriharsha.marupudi/Ellipsoid_Factor_Measurements_Print_40"
 os.makedirs(out_dir6, exist_ok=True)


ROIDir = "/gpfs_projects/sriharsha.marupudi/Segmentations_Otsu_Print_40/"



ROINRRD = glob(ROIDir+"*.nrrd")


for txt in ROINRRD:
    NAME = os.path.basename(txt).replace("Segmentation-grayscale-Print-","").replace(".nrrd","")
    print (f"output ROI-{NAME}")

            

import BoneJ_Demo_Script_Area_VolumeFraction
import BoneJ_Demo_Script_Thickness
import BoneJ_Demo_Script_Spacing
import BoneJ_Demo_Script_Anisotropy
import BoneJ_Demo_Script_Connectivity



