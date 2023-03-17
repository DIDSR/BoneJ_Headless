#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
import nrrd 
from pydicom import dcmread
from glob import glob 
import nibabel as nib
import os 
out_dir = "/gpfs_projects/sriharsha.marupudi/Emu_Scans/"
os.makedirs(out_dir, exist_ok=True)



dcmDirs =["/gpfs_projects/sriharsha.marupudi/Emu_Scans/03915/"]

         
for dind, folder in enumerate(dcmDirs): # Iterate over dicom images

    dcmDir = folder
    dcmFiles = glob(dcmDir+"*.DCM")
    dcmFiles.sort()
    
    outName = os.path.basename(os.path.normpath(folder))

    for ind, file in enumerate(dcmFiles): # Iterate over dicom slices of one image
        
        print(f"reading file: {dind}, bone 1, slice: {ind}")
        
        dataset = dcmread(file)
    
        if ind == 0:
            Nx, Ny = dataset.pixel_array.shape
            Nz = len(dcmFiles)
            image = np.zeros((Nx,Ny,Nz), dtype=np.int16)
            
        image[:,:,ind] = dataset.pixel_array
        
        # img = nib.Nifti1Image(image, np.eye(4))
        # nib.save(img, os.path.join(out_dir, outName))
        
   
 
    # nrrd.write("/gpfs_projects/sriharsha.marupudi/Trabecular_Bone_ROI_Scans/03918.nrrd",image)
    nrrd.write(os.path.join(out_dir,outName+".nrrd"),image)
   


    