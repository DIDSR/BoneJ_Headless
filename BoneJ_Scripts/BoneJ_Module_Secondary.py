#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 15:01:19 2022

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
import tifffile as tiff

from contextlib import contextmanager
import sys, os


# BoneJ Function wrapper
# def BoneJ(array,voxel_size,Fiji_path):
    
# Define function for each individual plugin 
#Require installation of Fiji with BoneJ plugins
NAME = 
array,array1header = nrrd.read(volume+NAME)
voxel_size = [51.29980, 51.29980, 51.29980] #microns 
fiji_path = "~/Fiji.app/ImageJ-linux64"



# feed in numpy array
# "startBoxSize",48,"smallestBoxSize",6,"scaleFactor",1.2,"autoParam",True

def Fractal_Dimension(array,voxel_size,fiji_path,startBoxSize,smallestBoxSize,scaleFactor,autoParam):
    
    startBoxSize = str(startBoxSize)
    smallestBoxSize=str(smallestBoxSize)
    scaleFactor=str(scaleFactor)
    autoParam=str(autoParam)
    
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath("Fractal_Dimension_API_Test.py")
    

    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    #
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                     " \'image="+"\""+data1_nrrd+"\"", ", startBoxSize="+"\""+startBoxSize+"\"",\
                     ", outputdir="+"\""+outputdir+"\"",
                     ", NAME="+"\""+NAME+"\"",
                     ", smallestBoxSize="+"\""+smallestBoxSize+"\"",
                     ", scaleFactor="+"\""+scaleFactor+"\"",
                     ", autoParam="+"\""+autoParam+"\"",
                     ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    
 
    with open(outputdir+f"ROI-{NAME}-table.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        print(metric_dict)
             
    return metric_dict
    
def Surface_Area(array,voxel_size,fiji_path):
    
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath("Surface_Area_API_Test.py")

    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)

    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                     " \'image="+"\""+data1_nrrd+"\"",
                     ", outputdir="+"\""+outputdir+"\"",
                     ", NAME="+"\""+NAME+"\"",
                     ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    

    with open(outputdir+f"ROI-{NAME}-table.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        print(metric_dict)
          
    return metric_dict

def Skeletonise(array,voxel_size,fiji_path):
    
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    skeleton_tif = os.path.join(tempdir.name, "skeleton.tif")
    macro_file = os.path.abspath("Skeletonise_API_Test.py")
    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"", 
                         ", NAME="+"\""+NAME+"\"",
                         ", skeleton_tif="+"\""+skeleton_tif+"\"",
                         ", outputdir="+"\""+outputdir+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    plt.figure()
    skeleton_tif = outputdir+f"{NAME}-skeleton.tif"
    skeleton_tif=tiff.imread(skeleton_tif)
    z_center = skeleton_tif.shape[2] // 2
    plt.imshow(skeleton_tif[:, :, z_center])
        
    return skeleton_tif
        

def Analyze_Skeleton(array,voxel_size,fiji_path,pruneCycleMethod=None,pruneEnds=True,excludeRoi=False,calculateShortestPaths=True,verbose=True,displaySkeletons=False):
    
    pruneCycleMethod =str(pruneCycleMethod)
    pruneEnds = str(pruneEnds)
    excludeRoi = str(excludeRoi)
    calculateShortestPaths = str(calculateShortestPaths)
    verbose = str(verbose)
    displaySkeletons = str(displaySkeletons)
    
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name,"img.nrrd")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name,"outputdir")
    skeleton_tif = os.path.join(tempdir.name,"skeleton.tif")
    macro_file = os.path.abspath("Analyze_Skeleton_API_Test.py")
    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"",  ", NAME="+"\""+NAME+"\"",
                         ", pruneCycleMethod="+"\""+pruneCycleMethod+"\"",
                         ", pruneEnds="+"\""+pruneEnds+"\"",
                         ", excludeRoi="+"\""+excludeRoi+"\"",
                         ", calculateShortestPaths="+"\""+calculateShortestPaths+"\"",
                         ", verbose="+"\""+verbose+"\"",
                         ", skeleton_tif="+"\""+skeleton_tif+"\"",
                         ", outputdir="+"\""+outputdir+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd,shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    with open(outputdir+f"ROI-{NAME}-table.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        print(metric_dict)
       
        optional_dict={}
        if displaySkeletons:
           skeleton_tif = outputdir +"ROI-"+NAME+"-skeleton.tif"
           skeleton_tif=tiff.imread(skeleton_tif)
           z_center = skeleton_tif.shape[2] // 2
           plt.imshow(skeleton_tif[:, :, z_center]);plt.show()
        
  
        
    return metric_dict, skeleton_tif

def Intertrabecular_Angles(array,voxel_size,fiji_path,minimumValence=3,maximumValence=50,marginCutOff=10,minimumTrabecularLength=0,useClusters=False,iteratePruning=False,printCentroids=False,printCulledEdgePercentages=False,showSkeleton=False):
    
    minimumValence = str(minimumValence)
    maximumValence = str(maximumValence)
    marginCutOff = str(marginCutOff)
    minimumTrabecularLength =str(minimumTrabecularLength)
    iteratePruning = str(iteratePruning)
    printCentroids = str(printCentroids)
    printCulledEdgePercentages = str(printCulledEdgePercentages)
    useClusters = str(useClusters)
    
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name,"img.nrrd")
    skeleton_tif = os.path.join(tempdir.name,"skeleton.tif")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath("Inter_Trabecular_Angles_API_Test.py")
    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)

    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"", ", skeleton_tif="+"\""+skeleton_tif+"\"",
                         ", minimumValence="+"\""+minimumValence+"\"",", marginCutOff="+"\""+marginCutOff+"\"",
                         ", minimumTrabecularLength="+"\""+minimumTrabecularLength+"\"",
                         ", maximumValence="+"\""+maximumValence+"\"",
                         ", useClusters="+"\""+useClusters+"\"",
                         ", iteratePruning="+"\""+iteratePruning+"\"",", printCentroids="+"\""+printCentroids+"\"",
                         ", printCulledEdgePercentages="+"\""+printCulledEdgePercentages+"\"",
                         ", outputdir="+"\""+outputdir+"\"",
                         ", skeleton_tif="+"\""+skeleton_tif+"\"",
                         ", NAME="+"\""+NAME+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])
    
    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    with open(outputdir+"ROI-"+NAME+"-table.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        print(metric_dict)


Fractal_Dimension_Results = Fractal_Dimension(array,voxel_size,fiji_path,startBoxSize=48,smallestBoxSize=6,scaleFactor=1.2,autoParam=True)
Surface_Area_Result= Surface_Area(array,voxel_size,fiji_path)
Analzye_Skeleton_Result = Analyze_Skeleton(array,voxel_size,fiji_path,pruneCycleMethod=None,pruneEnds=True,excludeRoi=False,calculateShortestPaths=True,verbose=True,displaySkeletons=True)
Intertrabecular_Angles_Result = Intertrabecular_Angles(array,voxel_size,fiji_path,minimumValence=3,maximumValence=50,marginCutOff=10,minimumTrabecularLength=0,iteratePruning=False,printCentroids=False,useClusters=False,printCulledEdgePercentages=False)
Skeletonise_Result=Skeletonise(array,voxel_size,fiji_path)

   
    
    
    
    


    
   
