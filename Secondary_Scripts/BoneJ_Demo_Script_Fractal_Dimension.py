#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from numpy import asarray
import nrrd
import csv 
import tempfile 
import os
import subprocess 

#from file import NAME 
from glob import glob
ROIDir = "/BoneJ_Headless/ROIs/"
startBoxSize = "48"
smallestBoxSize = "6"
scaleFactor = "1.2"
autoParam = "True"

ROINRRD = glob(ROIDir+"*.nrrd")


for txt in ROINRRD:
    
    NAME = os.path.basename(txt).replace(".nrrd","")
    
    tempdir = "/...Measurements/"
    data1_nrrd = os.path.join(tempdir,"img.nrrd")
    table_csv = os.path.join(tempdir, "table.csv")
    
    # TODO: from {file with your BoneJ wrapper} import compute_bonej_thickness
    data1,data1header1 = nrrd.read(ROIDir+f"-{NAME}.nrrd")
    ### save data1 to temporaryDirectory
    header = {'units': ['um', 'um', 'um'],'spacings': [51.29980,51.29980,51.29980]}
    nrrd.write(data1_nrrd,data1,header)

    # TODO: run your BoneJ thickness wrapper
    # table is the boneJ table, thickness_image is a numpy array containing thickness image
    macro_file = "/BoneJ_Headless/Fractal_Dimension_API.py"
    
    fiji_path = "~/Fiji.app/ImageJ-linux64" #home directory
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"", 
                         ", NAME="+"\""+NAME+"\"",
                         ", startBoxSize="+"\""+startBoxSize+"\"",
                         ", smallestBoxSize="+"\""+smallestBoxSize+"\"",
                         ", scaleFactor="+"\""+scaleFactor+"\"",
                         ", autoParam="+"\""+autoParam+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])
    b = subprocess.call(fiji_cmd, shell=True)
 
    
    
    
