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

# sys.path.append('/gpfs_projects/sriharsha.marupudi/BoneJ_Headless-main/BoneJ_Scripts/')
from BoneJ_Module_Secondary import Fractal_Dimension
from BoneJ_Module_Secondary import Surface_Area
from BoneJ_Module_Secondary import Analyze_Skeleton
from BoneJ_Module_Secondary import Intertrabecular_Angles
from BoneJ_Module_Secondary import Skeletonise

filepath = "/BoneJ_Headless/ROIs/emu.nrrd"
array,array1header = nrrd.read(filepath) 
voxel_size = [25, 25, 25] #microns 
fiji_path = "~/Fiji.app/ImageJ-linux64"
if __name__ == "__main__":

    Fractal_Dimension_Results = Fractal_Dimension(array,voxel_size,fiji_path,startBoxSize=48,smallestBoxSize=6,scaleFactor=1.2,autoParam=True)
    Surface_Area_Result= Surface_Area(array,voxel_size,fiji_path)
    Analzye_Skeleton_Result = Analyze_Skeleton(array,voxel_size,fiji_path,pruneCycleMethod=None,pruneEnds=True,excludeRoi=False,calculateShortestPaths=True,verbose=True,displaySkeletons=True)
    Intertrabecular_Angles_Result = Intertrabecular_Angles(array,voxel_size,fiji_path,minimumValence=3,maximumValence=50,marginCutOff=10,minimumTrabecularLength=0,iteratePruning=False,printCentroids=False,useClusters=False,printCulledEdgePercentages=False)
    Skeletonise_Result=Skeletonise(array,voxel_size,fiji_path)
    
       

       
