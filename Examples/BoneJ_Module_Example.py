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
import sys 
from argparse import ArgumentParser

from BoneJ_Module import Thickness
from BoneJ_Module import Separation
from BoneJ_Module import Area_VolumeFraction
from BoneJ_Module import Connectivity
from BoneJ_Module import Anisotropy
from BoneJ_Module import Ellipsoid_Factor

voxel_size = [25, 25, 25] #microns 

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", "--ROI", dest="ROI", default=os.path.join(os.path.dirname(os.path.dirname(__file__)), "ROIs/emu.nrrd"))
    parser.add_argument("-f", "--fiji", "--fiji-path", dest="fiji_path", default="~/Fiji.app/ImageJ-linux64")
    args = parser.parse_args()
    
    fiji_path = args.fiji_path
    filepath = args.ROI
    
    
    # Check that those filepaths actually exist
    if os.path.exists(fiji_path):
      print(f"Fiji installation specified: {fiji_path}")
    else:
      print(f"Unrecognized file path: {fiji_path}")
    
    if os.path.exists(filepath):
      print(f"Loading ROI from {filepath}")
    else:
      raise Exception(f"Unrecognized file path: {filepath}")
    
    # read array
    array, array1header = nrrd.read(filepath)
    
    Thickness_result = Thickness(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
    Separation_result = Separation(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
    Area_VolumeFraction_result = Area_VolumeFraction(array,voxel_size,fiji_path)
    Connectivity_result = Connectivity(array,voxel_size,fiji_path)
    Anisotropy_result = Anisotropy(array,voxel_size,fiji_path,NDirs = 2000, nLines = 10000, samplingincrement = 1.73,
    radii = False, eigens = False)
    Ellipsoid_Factor_result = Ellipsoid_Factor(array, voxel_size, fiji_path,nVectors = 100,vectorIncrement =.435,skipRatio =50,contactSensitivity = 1
    ,maxIterations = 100,maxDrift = 1.73,runs = 1,seedOnDistanceRidge = True,distanceThreshold = .6,seedOnTopologyPreserving = True
    ,showFlinnPlots = True,showConvergence = True,showSecondaryImages = True,showMaps = True)
    
        
       
