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

ROIDir = "/BoneJ_Headless/ROIs/"
showMaps ="True"
maskArtefacts = "True"

ROINRRD = glob(ROIDir)


for txt in ROINRRD:
    
    tempdir = ".../Measurements/"
    data1_nrrd = os.path.join(tempdir,"img.nrrd")
    thickness_tif = os.path.join(tempdir,"thickness.tif")
    table_csv = os.path.join(tempdir,"table.csv")
    outputdir = os.path.join(tempdir)

# TODO: from {file with your BoneJ wrapper} import compute_bonej_thickness
    data1,data1header1 = nrrd.read(volume)
### save data1 to temporaryDirectory
    header = {'units': ['um', 'um', 'um'],'spacings': [51.29980,51.29980,51.29980]}
    nrrd.write(data1_nrrd,data1,header)


# TODO: run your BoneJ thickness wrapper
# table is the boneJ table, thickness_tif is a numpy array containing thickness image
    macro_file = "/BoneJ_Headless/Trabecular_Thickness_API.py"

    fiji_path = "~/Fiji.app/ImageJ-linux64" #home directory
#Run BoneJ in headless mode in commandline with arguments  

    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                     " \'image="+"\""+data1_nrrd+"\"", ", thickness_tif="+"\""+thickness_tif+"\"",
                     ", NAME="+"\""+NAME+"\"",
                     ", showMaps="+"\""+showMaps+"\"",
                     ", maskArtefacts="+"\""+maskArtefacts+"\"",
                     ", outputdir="+"\""+outputdir+"\"",
                     ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
