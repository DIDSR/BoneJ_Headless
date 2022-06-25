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
from glob import glob 

#from file import NAME 
ROIDir = "/gpfs_projects_old/sriharsha.marupudi/Segmentations_Otsu/"


#previewDir = "/gpfs_projects_old/sriharsha.marupudi/Figures/"
#os.makedirs(previewDir,exist_ok=True)

ROINRRD = glob(ROIDir+"Segmentation-grayscale-*.nrrd")


for txt in ROINRRD:
    
    NAME = os.path.basename(txt).replace("Segmentation-grayscale-","").replace(".nrrd","")
    
   
    
    # seg, header = nrrd.read(f"{ROIDir}/Segmentation-{NAME}.nrrd")
    
import BoneJ_Demo_Script_Thickness
import BoneJ_Demo_Script_Spacing
import BoneJ_Demo_Script_Connectivity
import BoneJ_Demo_Script_Anisotropy
import BoneJ_Demo_Script_Area_VolumeFraction
#import BoneJ_Demo_Script_Ellipsoid_Factor
# import BoneJ_Demo_Script_Fractal_Dimension
# import BoneJ_Demo_Script_Surface_Area
#import BoneJ_Demo_Script_Inter_Trabecular_Angles
#import BoneJ_Demo_Script_Skeletonise



#Combine csv files Example 
df1 = pd.read_csv(f"/gpfs_projects_old/sriharsha.marupudi/Thickness_Measurements/ROI-{NAME}-table.csv")      
df2 = pd.read_csv(f"/gpfs_projects_old/sriharsha.marupudi/Spacing_Measurements/ROI-{NAME}-table.csv")
df3 = pd.read_csv(f"/gpfs_projects_old/sriharsha.marupudi/Connectivity_Measurements/ROI-{NAME}-table.csv")      
df4 = pd.read_csv(f"/gpfs_projects_old/sriharsha.marupudi/Anisotropy_Measurements/ROI-{NAME}-table.csv")
df5 = pd.read_csv(f"/gpfs_projects_old/sriharsha.marupudi/Area_VolumeFraction_Measurements/ROI-{NAME}-table.csv")
# # df6= pd.read_csv(f"/gpfs_projects_old/sriharsha.marupudi/Fractal_Dimension_Measurements/ROI-{NAME}-table.csv")  
# # df7 = pd.read_csv(f"/gpfs_projects_old/sriharsha.marupudi/Surface_Area_Measurements/ROI-{NAME}-table.csv")
# #df8 = pd.read_csv("/gpfs_projects_old/sriharsha.marupudi/Inter_Trabecular_Angles_Measurements/ROI-{NAME}-table.csv")   
# #df9 = pd.read_csv("/gpfs_projects_old/sriharsha.marupudi/Skeletonise_Measurements/ROI-{NAME}-table.csv")     
# #df10 = pd.read_csv("/gpfs_projects_old/sriharsha.marupudi/Ellipsoid_Factor_Measurements/ROI-{NAME}-table.csv")             


finaldf = pd.concat([df1, df2, df3, df4, df5])
finaldf.to_csv(f"/gpfs_projects_old/sriharsha.marupudi/BoneJ_Results/ROI-{NAME}-results_table.csv")


