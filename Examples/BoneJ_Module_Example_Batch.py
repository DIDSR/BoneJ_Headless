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
from argparse import ArgumentParser

from BoneJ_Module import Thickness
from BoneJ_Module import Spacing
from BoneJ_Module import Area_VolumeFraction
from BoneJ_Module import Connectivity
from BoneJ_Module import Anisotropy
from BoneJ_Module import Ellipsoid_Factor

voxel_size = [25,25,25] #microns 
outdir = "/BoneJ_Headless-main/ROIs/"
csv_path = outdir + "output_metrics.csv"

with open(csv_path, 'w', newline='') as csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerow(["ROI Name", "Tb.Th Mean (µm)", "Tb.Sp Mean (µm)", "DA", "BV/TV", "Conn.D (µm⁻³)", "Median EF"])
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
        print(f"ROI-{NAME} Complete")
    
        # write results to csv
        csv_results = [f"{NAME}",
                      Thickness_result[0]['Tb.Th Mean (µm)'],Spacing_result[0]['Tb.Sp Mean (µm)'],Anisotropy_result['DA'],
                      Area_VolumeFraction_result['BV/TV'],
                      Connectivity_result['Conn.D (µm⁻³)'],Ellipsoid_Factor_result[0]['Median EF']]
        
        with open(csv_path, 'a', newline='') as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(csv_results)
