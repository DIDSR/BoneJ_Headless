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
from glob import glob
import csv 
# sys.path.append('/gpfs_projects/sriharsha.marupudi/BoneJ_Headless-main/BoneJ_Scripts/')
from BoneJ_Module import Thickness
from BoneJ_Module import Spacing
from BoneJ_Module import Area_VolumeFraction
from BoneJ_Module import Connectivity
from BoneJ_Module import Anisotropy
from BoneJ_Module import Ellipsoid_Factor

filepath = "/gpfs_projects/sriharsha.marupudi/BoneJ_Headless-main/ROIs/"
voxel_size = [25,25,25] #microns 
fiji_path = "~/Fiji.app/ImageJ-linux64"
outdir = "/gpfs_projects/sriharsha.marupudi/BoneJ_Headless-main/ROIs/"

if __name__ == "__main__":
    Dir = glob(filepath+"*.nrrd")
    for file in Dir:
        
        NAME = os.path.basename(file).replace(".nrrd","")
        array,array1header = nrrd.read(filepath+NAME+".nrrd") 
        Thickness_result = Thickness(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
        Spacing_result = Spacing(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
        Area_VolumeFraction_result = Area_VolumeFraction(array,voxel_size,fiji_path)
        Connectivity_result = Connectivity(array,voxel_size,fiji_path)
        Anisotropy_result = Anisotropy(array,voxel_size,fiji_path,NDirs = 2000, nLines = 10000, samplingincrement = 1.73,
        radii = False, eigens = False)
        Ellipsoid_Factor_result = Ellipsoid_Factor(array, voxel_size, fiji_path,nVectors = 100,vectorIncrement =.435,skipRatio =1,contactSensitivity = 1
        ,maxIterations = 100,maxDrift = .4,runs = 1,seedOnDistanceRidge = True,distanceThreshold = .6,seedOnTopologyPreserving = True
        ,showFlinnPlots = True,showConvergence = True,showSecondaryImages = True,showMaps = True) 
        # writer.writerow([NAME, Thickness_result, Spacing_result, Area_VolumeFraction_result, Connectivity_result, Anisotropy_result])
        print(f"ROI-{NAME} Complete")
    
    # write results to csv
    csv_results = [f"{NAME}",
                  Thickness_result[0]['Tb.Th Mean (µm)'],Spacing_result[0]['Tb.Sp Mean (µm)'],Anisotropy_result['DA'],
                  Area_VolumeFraction_result['BV/TV'],
                  Connectivity_result['Conn.D (µm⁻³)'],Ellipsoid_Factor_result[0]['Median EF']]
    
    csv_path = outdir + "output_metrics.csv"
    with open(csv_path, 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(["ROI Name", "Thickness", "Spacing", "Anisotropy", "BV/TV", "Connectivity"])
        csvwriter.writerow(csv_results)
        
