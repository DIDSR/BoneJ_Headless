#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from numpy import asarray
import nrrd
import csv 
import tempfile 
import os
import subprocess 
from glob import glob
ROIDir = "/gpfs_projects_old/sriharsha.marupudi/Segmentations_Otsu_L1/"

ROINRRD = glob(ROIDir+"Segmentation-grayscale-*.nrrd")


for txt in ROINRRD:
    
    NAME = os.path.basename(txt).replace("Segmentation-grayscale-","").replace(".nrrd","")

    print(f"output ROI{NAME}.")
    
   
    
    # seg, header = nrrd.read(f"{ROIDir}/ROI-{NAME}.nrrd")
    tempdir = "/gpfs_projects_old/sriharsha.marupudi/Area_VolumeFraction_Measurements_L1"
    data1_nrrd = os.path.join(tempdir,"img.nrrd")
    table_csv = os.path.join(tempdir, "table.csv")
    
    # TODO: from {file with your BoneJ wrapper} import compute_bonej_thickness
    data1,data1header1 = nrrd.read(f"/gpfs_projects_old/sriharsha.marupudi/Segmentations_Otsu_L1/Segmentation-grayscale-{NAME}.nrrd")
    ### save data1 to temporaryDirectory
    header = {'units': ['um', 'um', 'um'],'spacings': [51.29980,51.29980,51.29980]}
    nrrd.write(data1_nrrd,data1,header)

    
    # TODO: run your BoneJ thickness wrapper
    # table is the boneJ table, thickness_image is a numpy array containing thickness image
    macro_file = "/gpfs_projects_old/sriharsha.marupudi/Area_VolumeFraction_API_.py"
    
    fiji_path = "~/Fiji.app/ImageJ-linux64" # where is this
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"",  ", NAME="+"\""+NAME+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])
    b = subprocess.call(fiji_cmd, shell=True)
    # with open(f"/gpfs_projects_old/sriharsha.marupudi/Area_VolumeFraction_Measurements/ROI-{NAME}table.csv", encoding = "utf8", errors = 'ignore') as file:
    #     reader = csv.reader(file)
    #     result = {row[0]:row[1:] for row in reader if row and row[0]}
    # print(result)
    #'name1="Alice", name2="Bob"'
    # read table_csv into dictionary {table}
    
    #return table, img
    
