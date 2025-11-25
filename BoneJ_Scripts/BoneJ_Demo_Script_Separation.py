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

ROIDir = "/BoneJ_Headless_ROIs/"
showMaps = "True"
maskArtefacts = "True"
mapChoice = "Trabecular separation"

ROINRRD = glob(ROIDir+"*.nrrd")

for txt in ROINRRD:
    
    NAME = os.path.basename(txt)..replace(".nrrd","")

    print(f"output ROI-{NAME}.")
    
    tempdir = "/gpfs_projects/sriharsha.marupudi/...Measurements/"
    data1_nrrd = os.path.join(tempdir,"img.nrrd")
    separation_tif = os.path.join(tempdir,"separation.tif")
    table_csv = os.path.join(tempdir,"table.csv")
    outputdir = os.path.join(tempdir)

    data1,data1header1 = nrrd.read(ROIDir+f"{NAME}.nrrd")
    ### save data1 to temporaryDirectory
    header = {'units': ['um', 'um', 'um'],'spacings': [51.29980,51.29980,51.29980]}
    nrrd.write(data1_nrrd,data1,header)


    macro_file = "/gpfs_projects/sriharsha.marupudi/Trabecular_Separation_API.py"

    fiji_path = "~/Fiji.app/ImageJ-linux64" #home directory

    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                     " \'image="+"\""+data1_nrrd+"\"", ", separation_tif="+"\""+separation_tif+"\"",
                     ", NAME="+"\""+NAME+"\"",
                     ", showMaps="+"\""+showMaps+"\"",
                     ", maskArtefacts="+"\""+maskArtefacts+"\"",
                     ", mapChoice="+"\""+mapChoice+"\"",
                     ", outputdir="+"\""+outputdir+"\"",
                     ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
