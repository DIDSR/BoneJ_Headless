6#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 17:03:31 2022

@author: sriharsha.marupudi
"""

import numpy as np
import nrrd
import csv 
import os
import subprocess 
from glob import glob
import tempfile 
import sys 
import matplotlib.pyplot as plt 
from contextlib import contextmanager
import sys, os


array,array1header = nrrd.read(volume)  # should be a numpy array
voxel_size = [51.29980, 51.29980, 51.29980] #microns 
fiji_path = "~/Fiji.app/ImageJ-linux64"

 
# feed in numpy array

nLines_list = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]
NDirs_list = [16,32,64,128,256,512,1024,2048,4096,8192]
csv_dir = "/BoneJ_Headless/Anisotropy_Convergence_Test.csv" #location of csv file storing anisotropy convergence measurements 

         
def Anisotropy(array,voxel_size,fiji_path,NDirs = NDirs_list, nLines =nLines_list, samplingincrement = 1.73, radii = False, eigens = False):
    
  
    
    for i in NDirs_list:
        
       
        
       for c in nLines_list:
           


            NDirs = str(i)
            nLines = str(c)
            samplingincrement = str(samplingincrement)
            radii = str(radii)
            eigens = str(eigens)
               
            
            
            tempdir = tempfile.TemporaryDirectory()
            data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
            table_csv = os.path.join(tempdir.name,"table.csv")
            outputdir = os.path.join(tempdir.name, "outputdir")
            macro_file = os.path.abspath("Anisotropy_API_Test.py")
            csv_Dir  = csv_dir
            # save to temporary directory
            header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}
            
            nrrd.write(data1_nrrd,array,header)
            
            # run BoneJ thickness wraapper 
            # table is results of thickness plugin as csv file 
            # thickness_tif is numpy array of thickness images 
            
            fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                             " \'image="+"\""+data1_nrrd+"\"",
                             ", NAME="+"\""+NAME+"\"",", NDirs="+"\""+NDirs+"\"",
                             ", nLines="+"\""+nLines+"\"",
                             ", samplingincrement="+"\""+samplingincrement+"\"",
                             ", radii="+"\""+radii+"\"",
                             ", eigens="+"\""+eigens+"\"",
                             ", outputdir="+"\""+outputdir+"\"",
                             ", table_csv="+"\""+table_csv+"\""+"\'"])
            
            b = subprocess.call(fiji_cmd, shell=True)
            with open(outputdir+f"ROI-{NAME}-table.csv", "r",encoding='utf-8') as file:
                reader = csv.reader(file)
                metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
                print(metric_dict)
                writer = csv.writer(csv_dir,dialect='excel')
                writer.writeheader()
                writer.writerows(metric_dict)
        

    return metric_dict




Anisotropy_result = Anisotropy(array,voxel_size,fiji_path,NDirs = NDirs_list, nLines =nLines_list, samplingincrement = 1.73, radii = False, eigens = False) 
