#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Requires 8 bit binary image as input 
#Image is a 3D np.array of type np.uint8, with binary values of 0 and 1

import numpy as np
from numpy import asarray
import nrrd
import csv 
import tempfile 
import os
import subprocess 
from glob import glob


#from file import NAME 
ROIDir = "/gpfs_projects_old/sriharsha.marupudi/Segmentations_Otsu_L1/"
showMaps ="True"
maskArtefacts = "True"
mapChoice = "Trabecular spacing"

ROINRRD = glob(ROIDir+"Segmentation-grayscale-*.nrrd")

for txt in ROINRRD:
    
    NAME = os.path.basename(txt).replace("Segmentation-grayscale-","").replace(".nrrd","")

    print(f"output ROI{NAME}.")
    
   
    
    # seg, header = nrrd.read(f"{ROIDir}/ROI-{NAME}.nrrd")

    tempdir = "/gpfs_projects_old/sriharsha.marupudi/Spacing_Measurements_L1"
    data1_nrrd = os.path.join(tempdir,"img.nrrd")
    spacing_tif = os.path.join(tempdir,"spacing.tif")
    table_csv = os.path.join(tempdir,"table.csv")

# TODO: from {file with your BoneJ wrapper} import compute_bonej_thickness
    data1,data1header1 = nrrd.read(f"/gpfs_projects_old/sriharsha.marupudi/Segmentations_Otsu_L1/Segmentation-grayscale-{NAME}.nrrd")
    header = {'units': ['um', 'um', 'um'],'spacings': [51.29980,51.29980,51.29980]}
    nrrd.write(data1_nrrd,data1,header)


# TODO: run your BoneJ thickness wrapper
# table is the boneJ table, thickness_tif is a numpy array containing thickness image
    macro_file = "/gpfs_projects_old/sriharsha.marupudi/Trabecular_Spacing_API.py"

    fiji_path = "~/Fiji.app/ImageJ-linux64" #home directory
#Run BoneJ in headless mode in commandline with arguments  

    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                     " \'image="+"\""+data1_nrrd+"\"", ", spacing_tif="+"\""+spacing_tif+"\"",
                     ", NAME="+"\""+NAME+"\"",
                     ", showMaps="+"\""+showMaps+"\"",
                     ", maskArtefacts="+"\""+maskArtefacts+"\"",
                     ", mapChoice="+"\""+mapChoice+"\"",
                     ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True)
    print(table_csv)
# Write to a NRRD file: this should be the same image as running the thickness plugin manually in boneJ
#img, header = nrrd.read("/gpfs_projects_old/sriharsha.marupudi/Measurements/thickness.tif")
#print(img,header)
    # with open(f"/gpfs_projects_old/sriharsha.marupudi/Spacing_Measurements/ROI-{NAME}-table.csv", "r",) as file:
    #     reader = csv.reader(file)
    #     result = {row[0]:row[1:] for row in reader if row and row[0]}
    #     print(result)
#'name1="Alice", name2="Bob"'
# read table_csv into dictionary {table}

#return table, img