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

# out_dir6 = "/gpfs_projects/sriharsha.marupudi/Ellipsoid_Factor_Measurements_Print_40"
# os.makedirs(out_dir6, exist_ok=True)
# ROIDir = "/gpfs_projects/sriharsha.marupudi/Segmentations_Otsu_Print/"

# ROINRRD = glob(ROIDir+"Segmentation-grayscale-Print-*.nrrd")


# for txt in ROINRRD:
    
#     NAME = os.path.basename(txt).replace("Segmentation-grayscale-Print-","").replace(".nrrd","")

#     print(f"output ROI{NAME}.")
#from file import NAME 


ROIDir = "/gpfs_projects/sriharsha.marupudi/Segmentations_Otsu_Print_40/"

#previewDir = "/gpfs_projects/sriharsha.marupudi/Figures/"
#os.makedirs(previewDir,exist_ok=True)

ROINRRD = glob(ROIDir+"*.nrrd")


for txt in ROINRRD:
    NAME = os.path.basename(txt).replace("Segmentation-grayscale-Print-","").replace(".nrrd","")
    print (f"output ROI-{NAME}")

        
   
    
    # seg, header = nrrd.read(f"{ROIDir}/Segmentation-{NAME}.nrrd")
    

import BoneJ_Demo_Script_Area_VolumeFraction
import BoneJ_Demo_Script_Thickness
import BoneJ_Demo_Script_Spacing
import BoneJ_Demo_Script_Anisotropy
import BoneJ_Demo_Script_Connectivity
# import BoneJ_Demo_Script_Ellipsoid_Factor
# import BoneJ_Demo_Script_Fractal_Dimension
# import BoneJ_Demo_Script_Surface_Area
#import BoneJ_Demo_Script_Inter_Trabecular_Angles
#import BoneJ_Demo_Script_Skeletonise



    #Combine csv files Example 
    # df1 = pd.read_csv(f"/gpfs_projects/sriharsha.marupudi/Thickness_Measurements_Print/ROI-{NAME}-table.csv")      
    # df2 = pd.read_csv(f"/gpfs_projects/sriharsha.marupudi/Spacing_Measurements_Print/ROI-{NAME}-table.csv")
    # df3 = pd.read_csv(f"/gpfs_projects/sriharsha.marupudi/Connectivity_Measurements_Print/ROI-{NAME}-table.csv")      
    # df4 = pd.read_csv(f"/gpfs_projects/sriharsha.marupudi/Anisotropy_Measurements_Print/ROI-{NAME}-table.csv")
    # df5 = pd.read_csv(f"/gpfs_projects/sriharsha.marupudi/Area_VolumeFraction_Measurements_Print/ROI-{NAME}-table.csv")
    # # df6= pd.read_csv(f"/gpfs_projects/sriharsha.marupudi/Fractal_Dimension_Measurements_Print/ROI-{NAME}-table.csv")  
    # # df7 = pd.read_csv(f"/gpfs_projects/sriharsha.marupudi/Surface_Area_Measurements_Print/ROI-{NAME}-table.csv")
    # # df8 = pd.read_csv("/gpfs_projects/sriharsha.marupudi/Inter_Trabecular_Angles_Measurements_Print/ROI-{NAME}-table.csv")   
    # # df9 = pd.read_csv("/gpfs_projects/sriharsha.marupudi/Skeletonise_Measurements_Print/ROI-{NAME}-table.csv")     
    # # df10 = pd.read_csv("/gpfs_projects/sriharsha.marupudi/Ellipsoid_Factor_Measurements_Print/ROI-{NAME}-table.csv")             
    
    
    # finaldf = pd.concat([df1, df2, df3, df4, df5])
    # finaldf.to_csv(f"/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print/ROI-{NAME}-results_table.csv")


