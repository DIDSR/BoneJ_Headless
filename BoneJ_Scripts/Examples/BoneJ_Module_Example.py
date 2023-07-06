#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import nrrd
import os
import subprocess
import tempfile
import sys
import matplotlib.pyplot as plt
import tifffile as tiff
from contextlib import contextmanager
import sys, os

#sys.path.append('/gpfs_projects/sriharsha.marupudi/BoneJ_Headless-main/BoneJ_Scripts/')
from BoneJ_Module import Thickness
from BoneJ_Module import Spacing
from BoneJ_Module import Area_VolumeFraction
from BoneJ_Module import Connectivity
from BoneJ_Module import Anisotropy
from BoneJ_Module import Ellipsoid_Factor

filepath = "/gpfs_projects/sriharsha.marupudi/BoneJ_Headless-main/ROIs/emu.nrrd"
array,array1header = nrrd.read(filepath) 
voxel_size = [51.29980, 51.29980, 51.29980] #microns 
fiji_path = "~/Fiji.app/ImageJ-linux64"

if __name__ == "__main__":
    Thickness_result = Thickness(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
    Spacing_result = Spacing(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
    Area_VolumeFraction_result = Area_VolumeFraction(array,voxel_size,fiji_path)
    Connectivity_result = Connectivity(array,voxel_size,fiji_path)
    Anisotropy_result = Anisotropy(array,voxel_size,fiji_path,NDirs = 2000, nLines = 10000, samplingincrement = 1.73,
    radii = False, eigens = False)
    Ellipsoid_Factor(array, voxel_size, fiji_path,nVectors = 100,vectorIncrement =.435,skipRatio =1,contactSensitivity = 1
    ,maxIterations = 100,maxDrift = .4,runs = 1,seedOnDistanceRidge = True,distanceThreshold = .6,seedOnTopologyPreserving = True
    ,showFlinnPlots = True,showConvergence = True,showSecondaryImages = True) 
    
    
        
       
