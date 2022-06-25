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
import matplotlib.pyplot as plt

from glob import glob
ROIDir = "/gpfs_projects/sriharsha.marupudi/extract_rois_output/"

ROINRRD = glob(ROIDir+"ROI-*.nrrd")

for txt in ROINRRD:
    
    NAME = os.path.basename(txt).replace("ROI-","").replace(".nrrd","")

    print(f"output ROI{NAME}.")
    tempdir = "/gpfs_projects/sriharsha.marupudi/Skeletonise_Measurements"
    data1_nrrd = os.path.join(tempdir,"img.nrrd")
    skeleton_tif = os.path.join(tempdir,"skeleton_tif")
    
    # TODO: from {file with your BoneJ wrapper} import compute_bonej_thickness
    data1,data1header1 = nrrd.read(f"/gpfs_projects/sriharsha.marupudi/extract_rois_output/ROI-{NAME}.nrrd")
    ### save data1 to temporaryDirectory
    header = {'units': ['um', 'um', 'um'],'spacings': [51.29980,51.29980,51.29980]}
    nrrd.write(data1_nrrd,data1,header)

    
    # TODO: run your BoneJ thickness wrapper
    # table is the boneJ table, thickness_image is a numpy array containing thickness image
    macro_file = "/gpfs_projects/sriharsha.marupudi/Skeletonise.py"
    
    fiji_path = "~/Fiji.app/ImageJ-linux64" #home directory
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"",
                         ", NAME="+"\""+NAME+"\"",
                         ", skeleton_tif="+"\""+skeleton_tif+"\""+"\'"])
    b = subprocess.call(fiji_cmd, shell=True)
    
    #I = plt.imread(f"/gpfs_projects/sriharsha.marupudi/Skeletonise_Measurements/ROI-{NAME}-skeleton.tif")
    #plt.imshow(I)
    
