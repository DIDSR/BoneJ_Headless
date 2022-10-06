#!/usr/bin/env python3
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


# BoneJ Function wrapper
# def BoneJ(array,voxel_size,Fiji_path):
    
# Define function for each individual plugin 
#Require installation of Fiji with BoneJ plugins

NAME = "1_04216"
array,array1header = nrrd.read(f"/gpfs_projects/sriharsha.marupudi/Segmentations_Otsu_L1/Segmentation-grayscale-{NAME}.nrrd")  # should be a numpy array
voxel_size = [51.29980, 51.29980, 51.29980] #microns 
fiji_path = "~/Fiji.app/ImageJ-linux64"




    

# feed in numpy array

def Thickness(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True):
    
    showMaps = str(showMaps)
    maskArtefacts = str(maskArtefacts)
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    thickness_tif = os.path.join(tempdir.name, "thickness.tif")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath("Trabecular_Thickness_API_Test.py")
    

    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    # macro_file = "/gpfs_projects/sriharsha.marupudi/Trabecular_Thickness_API_Test.py"
    # run BoneJ thickness wraapper 
    # table is results of thickness plugin as csv file 
    # thickness_tif is numpy array of thickness images 
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                     " \'image="+"\""+data1_nrrd+"\"", ", thickness_tif="+"\""+thickness_tif+"\"",\
                     ", outputdir="+"\""+outputdir+"\"",
                     ", NAME="+"\""+NAME+"\"",
                     ", showMaps="+"\""+showMaps+"\"",
                     ", maskArtefacts="+"\""+maskArtefacts+"\"",
                     ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    
 
    with open(outputdir+f"ROI-{NAME}-table.csv", "r",) as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        print(metric_dict)
    
        optional_dict={}
        if showMaps==True:
            with open(outputdir+f"ROI-{NAME}-thickness.tif", 'rb') as f:
                thickness_tif = f.read()
            optional_dict["thickness_tif"] = thickness_tif
            
           
        
    return metric_dict, optional_dict
    
def Spacing(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True):
    mapChoice = "Trabecular spacing"
    showMaps = str(showMaps)
    maskArtefacts = str(maskArtefacts)
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    spacing_tif = os.path.join(tempdir.name, "spacing.tif")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath("Trabecular_Spacing_API_Test.py")

    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    # macro_file = "/gpfs_projects/sriharsha.marupudi/Trabecular_Thickness_API_Test.py"
    # run BoneJ thickness wraapper 
    # table is results of thickness plugin as csv file 
    # thickness_tif is numpy array of thickness images 
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                     " \'image="+"\""+data1_nrrd+"\"", ", spacing_tif="+"\""+spacing_tif+"\"",\
                     ", outputdir="+"\""+outputdir+"\"",
                     ", NAME="+"\""+NAME+"\"",
                     ", showMaps="+"\""+showMaps+"\"",
                     ", maskArtefacts="+"\""+maskArtefacts+"\"",
                     ", mapChoice="+"\""+mapChoice+"\"",
                     ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    

    with open(outputdir+f"ROI-{NAME}-table.csv", "r",) as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        print(metric_dict)
    
        optional_dict={}
        if showMaps==True:
            with open(outputdir+f"ROI-{NAME}-spacing.tif", 'rb') as f:
                spacing_tif = f.read()
            optional_dict["spacing_tif"] = spacing_tif
        
    return metric_dict, optional_dict


nLines_list = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]
NDirs_list = [16,32,64,128,256,512,1024,2048,4096,8192]


# for i in nLines_list:
#     print(i)
    
# for c in NDirs_list:
#     print(c)


         
def Anisotropy(array,voxel_size,fiji_path,NDirs = NDirs_list, nLines =nLines_list, samplingincrement = 1.73, radii = False, eigens = False):
    
    # nLines_list = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]
    # NDirs_list = [16,32,64,128,256,512,1024,2048,4096,8192]
    
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
            
            
            
            # return metric_dict

def EllipsoidFactor (array,voxel_size,fiji_path,nVectors = "70",
vectorIncrement = "2",
skipRatio = "1",
contactSensitivity = "1",
maxIterations = "50",
maxDrift = "1",
runs = "1",
seedOnDistanceRidge = "True",
distanceThreshold = ".8",
seedOnTopologyPreserving = "True",
showFlinnPlots = "False",
showConvergence = "True",
showSecondaryImages = "False"):
    
    
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir,"img.nrrd")
    table_csv = os.path.join(tempdir, "table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    img_ef_tif = os.path.join(tempdir,"img_ef.tif")
    img_volume_tif = os.path.join(tempdir,"img_volume.tif")
    img_id_tif = os.path.join(tempdir,"img_id.tif")
    img_a_tif = os.path.join(tempdir,"img_a.tif")
    img_c_tif = os.path.join(tempdir,"img_c.tif")
    img_ab_tif = os.path.join(tempdir,"img_ab.tif")
    img_bc_tif = os.path.join(tempdir,"img_bc.tif")
    img_seed_points_tif = os.path.join(tempdir,"img_seed_points.tif")
    img_flinn_peak_plot_tif = os.path.join(tempdir,"img_flinn_peak_plot.tif")
    img_unweighted_flinn_plot_tif = os.path.join(tempdir,"img_unweighted_flinn_plot.tif")
    macro_file = os.path.abspath("Ellipsoid_Factor_API_Test.py")

    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    
    # run BoneJ thickness wraapper 
    # table is results of thickness plugin as csv file 
    # thickness_tif is numpy array of thickness images 
   
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"", ", img_ef_tif="+"\""+img_ef_tif+"\"",
                         ", img_volume_tif="+"\""+img_volume_tif+"\"",", img_id_tif="+"\""+img_id_tif+"\"",
                         ", img_a_tif="+"\""+img_a_tif+"\"",", img_b_tif="+"\""+img_c_tif+"\"",
                         ", img_ab_tif="+"\""+img_ab_tif+"\"",", img_bc_tif="+"\""+img_bc_tif+"\"",
                         ", img_seed_points_tif="+"\""+img_seed_points_tif+"\"",", img_flinn_peak_plot_tif="+"\""+img_flinn_peak_plot_tif+"\"",
                         ", img_unweighted_flinn_plot_tif="+"\""+img_unweighted_flinn_plot_tif+"\"",
                         ", nVectors="+"\""+nVectors+"\"",
                         ", vectorIncrement="+"\""+vectorIncrement+"\"",
                         ", skipRatio="+"\""+skipRatio+"\"",
                         ", contactSensitivity="+"\""+contactSensitivity+"\"",
                         ", maxIterations="+"\""+maxIterations+"\"",
                         ", maxDrift="+"\""+maxDrift+"\"",
                         ", runs="+"\""+runs+"\"",
                         ", seedOnDistanceRidge="+"\""+seedOnDistanceRidge+"\"",
                         ", distanceThreshold="+"\""+distanceThreshold+"\"",
                         ", seedOnTopologyPreserving="+"\""+seedOnTopologyPreserving+"\"",
                         ", showFlinnPlots="+"\""+showFlinnPlots+"\"",
                         ", showConvergence="+"\""+showConvergence+"\"",
                         ", showSecondaryImages="+"\""+showSecondaryImages+"\"",
                         ", outputdir="+"\""+outputdir+"\"",
                         ", NAME="+"\""+NAME+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])
    b = subprocess.call(fiji_cmd, shell=True)

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    with open(outputdir+f"ROI-{NAME}-table.csv", "r",) as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        print(metric_dict)
        

    return metric_dict       

def Connectivity(array,voxel_size,fiji_path):
    
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath("Connectivity_API_Test.py")
    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    
    # run BoneJ thickness wraapper 
    # table is results of thickness plugin as csv file 
    # thickness_tif is numpy array of thickness images 
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"", 
                         ", NAME="+"\""+NAME+"\"",
                         ", outputdir="+"\""+outputdir+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    with open(outputdir+f"ROI-{NAME}-table.csv", "r",) as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        print(metric_dict)
        
    return metric_dict
    
def Area_VolumeFraction(array,voxel_size,fiji_path):
    
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath("Area_VolumeFraction_API_Test.py")
    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    
    # run BoneJ thickness wraapper 
    # table is results of thickness plugin as csv file 
    # thickness_tif is numpy array of thickness images 
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"",  ", NAME="+"\""+NAME+"\"",
                         ", outputdir="+"\""+outputdir+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    with open(outputdir+f"ROI-{NAME}-table.csv", "r",) as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        print(metric_dict)
        
    return metric_dict

# Thickness_result = Thickness(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
# Spacing_result = Spacing(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
# Area_VolumeFraction_result = Area_VolumeFraction(array,voxel_size,fiji_path)
# Connectivity_result = Connectivity(array,voxel_size,fiji_path)
# Anisotropy_result = Anisotropy(array,voxel_size,fiji_path,NDirs = NDirs_list, nLines =nLines_list, samplingincrement = 1.73, radii = False, eigens = False) 
#Ellipsoid_Factor_result = Ellipsoid_Factor(array,voxel_size,fiji_path,nVectors = "70",
# vectorIncrement = "2",
# skipRatio = "1",
# contactSensitivity = "1",
# maxIterations = "50",
# maxDrift = "1",
# runs = "1",
# seedOnDistanceRidge = "True",
# distanceThreshold = ".8",
# seedOnTopologyPreserving = "True",
# showFlinnPlots = "False",
# showConvergence = "True",
# showSecondaryImages = "False")

     
   
    
    
    
    


    
   