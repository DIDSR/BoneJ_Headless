#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nrrd
import numpy as np 
import csv 
import os
import subprocess 
import tempfile 
import matplotlib.pyplot as plt 
import tifffile as tiff
        
def Thickness(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True):
    
    if not isinstance(array, np.ndarray) or array.dtype != np.uint8:
        print("Error: The input array is not an 8-bit array.")
        return
    
    unique_values = np.unique(array)
    binary = len(unique_values) == 2 and np.array_equal(unique_values, [0, 255])

    if not binary:
        print("Error: The input array is not binary.")
        return 
    
    showMaps = str(showMaps)
    maskArtefacts = str(maskArtefacts)
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    thickness_tif = os.path.join(tempdir.name, "thickness.tif")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "Macros/Trabecular_Thickness_API_Test.py"))

    

    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    # run BoneJ thickness wrapper 
    # table is results of thickness plugin as csv file 
    # thickness_tif is numpy array of thickness images 
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                     " \'image="+"\""+data1_nrrd+"\"", ", thickness_tif="+"\""+thickness_tif+"\"",\
                     ", outputdir="+"\""+outputdir+"\"",
                     ", showMaps="+"\""+showMaps+"\"",
                     ", maskArtefacts="+"\""+maskArtefacts+"\"",
                     ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    
 
    with open(outputdir+f"table.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        metric_dict = {row[0]: row[1:] for row in reader if row and row[0]}  
       
    clean_metric_dict = {
        key: value[0].strip('"')
        for key, value in metric_dict.items()
    }

    for idx, (key, value) in enumerate (clean_metric_dict.items()):
        if idx ==0:
            continue
        print(key + ":", value)

    
    
    if showMaps=="True":
        thickness_tif = outputdir +"thickness.tif"
        thickness_tif=tiff.imread(thickness_tif)
        z_center = thickness_tif.shape[2] // 2
        plt.figure();plt.imshow(thickness_tif[:, :, z_center])
        plt.title("thickness map")
        plt.axis("off")
        plt.show()
             
       
    return clean_metric_dict,thickness_tif
    
def Separation(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True):
    
    if not isinstance(array, np.ndarray) or array.dtype != np.uint8:
        print("Error: The input array is not an 8-bit array.")
        return
    
    unique_values = np.unique(array)
    binary = len(unique_values) == 2 and np.array_equal(unique_values, [0, 255])

    if not binary:
        print("Error: The input array is not binary.")
        return 
     
    mapChoice = "Trabecular separation"
    showMaps = str(showMaps)
    maskArtefacts = str(maskArtefacts)
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    separation_tif = os.path.join(tempdir.name, "separation.tif")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath(os.path.join(os.path.dirname(__file__),"Macros/Trabecular_Separation_API_Test.py"))

    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)

    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                     " \'image="+"\""+data1_nrrd+"\"", ", separation_tif="+"\""+separation_tif+"\"",\
                     ", outputdir="+"\""+outputdir+"\"",
                     ", showMaps="+"\""+showMaps+"\"",
                     ", maskArtefacts="+"\""+maskArtefacts+"\"",
                     ", mapChoice="+"\""+mapChoice+"\"",
                     ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    

    with open(outputdir+f"table.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        
        clean_metric_dict = {
            key: value[0].strip('"')
            for key, value in metric_dict.items()
        }

        for idx, (key, value) in enumerate (clean_metric_dict.items()):
            if idx ==0:
                continue
            print(key + ":", value)
                
        
        if showMaps=="True":
            separation_tif = outputdir +"separation.tif"
            separation_tif=tiff.imread(separation_tif)
            z_center = separation_tif.shape[2] // 2
            plt.figure();plt.imshow(separation_tif[:, :, z_center])
            plt.title("separation map")
            plt.axis("off")
            plt.show()
        
        
    return clean_metric_dict, separation_tif

            
       
def Anisotropy(array,voxel_size,fiji_path,NDirs = 2000, nLines = 10000, samplingincrement = 1.73, radii = False, eigens = False):
    if not isinstance(array, np.ndarray) or array.dtype != np.uint8:
        print("Error: The input array is not an 8-bit array.")
        return
    
    unique_values = np.unique(array)
    binary = len(unique_values) == 2 and np.array_equal(unique_values, [0, 255])

    if not binary:
        print("Error: The input array is not binary.")
        return 
    
    NDirs = str(NDirs)
    nLines = str(nLines)
    samplingincrement = str(samplingincrement)
    radii = str(radii)
    eigens = str(eigens)
   
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file =os.path.abspath(os.path.join(os.path.dirname(__file__),"Macros/Anisotropy_API_Test.py"))
    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    

    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"",
                         ", NDirs="+"\""+NDirs+"\"",
                         ", nLines="+"\""+nLines+"\"",
                         ", samplingincrement="+"\""+samplingincrement+"\"",
                         ", radii="+"\""+radii+"\"",
                         ", eigens="+"\""+eigens+"\"",
                         ", outputdir="+"\""+outputdir+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    with open(outputdir+f"table.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}

        clean_metric_dict = {
            key: value[0].strip('"')
            for key, value in metric_dict.items()
        }

        for idx, (key, value) in enumerate (clean_metric_dict.items()):
            if idx ==0:
                continue
            print(key + ":", value)        

      

    return clean_metric_dict

        

def Connectivity(array,voxel_size,fiji_path):
    if not isinstance(array, np.ndarray) or array.dtype != np.uint8:
        print("Error: The input array is not an 8-bit array.")
        return
    
    unique_values = np.unique(array)
    binary = len(unique_values) == 2 and np.array_equal(unique_values, [0, 255])

    if not binary:
        print("Error: The input array is not binary.")
        return 
    
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath(os.path.join(os.path.dirname(__file__),"Macros/Connectivity_API_Test.py"))
    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    
   
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"", 
                         ", outputdir="+"\""+outputdir+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    with open(outputdir+f"table.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        clean_metric_dict = {
            key: value[0].strip('"')
            for key, value in metric_dict.items()
        }

        for idx, (key, value) in enumerate (clean_metric_dict.items()):
            if idx ==0:
                continue
            print(key + ":", value)                  
    return clean_metric_dict
    
def Area_VolumeFraction(array,voxel_size,fiji_path):
    if not isinstance(array, np.ndarray) or array.dtype != np.uint8:
        print("Error: The input array is not an 8-bit array.")
        return
    
    unique_values = np.unique(array)
    binary = len(unique_values) == 2 and np.array_equal(unique_values, [0, 255])

    if not binary:
        print("Error: The input array is not binary.")
        return 
     
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath(os.path.join(os.path.dirname(__file__),"Macros/Area_VolumeFraction_API_Test.py"))
    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"",  
                         ", outputdir="+"\""+outputdir+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])

    b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    with open(outputdir+f"table.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        clean_metric_dict = {
            key: value[0].strip('"')
            for key, value in metric_dict.items()
        }

        for idx, (key, value) in enumerate (clean_metric_dict.items()):
            if idx ==0:
                continue
            print(key + ":", value)
        
    return clean_metric_dict

def Ellipsoid_Factor(array,voxel_size,fiji_path,nVectors = 100,vectorIncrement =.435,skipRatio =1,contactSensitivity = 1
,maxIterations = 100,maxDrift = 1.73,runs = 1,seedOnDistanceRidge = True,distanceThreshold = .6,seedOnTopologyPreserving = True
,showFlinnPlots = True,showConvergence = True,showSecondaryImages = False,showMaps = True):
    if not isinstance(array, np.ndarray) or array.dtype != np.uint8:
        print("Error: The input array is not an 8-bit array.")
        return
    
    unique_values = np.unique(array)
    binary = len(unique_values) == 2 and np.array_equal(unique_values, [0, 255])

    if not binary:
        print("Error: The input array is not binary.")
        return 
    
     
    nVectors =str(nVectors)
    vectorIncrement = str(vectorIncrement)
    skipRatio = str(skipRatio)
    contactSensitivity = str(contactSensitivity)
    maxIterations = str(maxIterations)
    maxDrift = str(maxDrift)
    runs = str(runs)
    seedOnDistanceRidge = str(seedOnDistanceRidge)
    distanceThreshold = str(distanceThreshold)
    seedOnTopologyPreserving = str(seedOnTopologyPreserving)
    showFlinnPlots = str(showFlinnPlots)
    showConvergence = str(showConvergence)
    showSecondaryImages = str(showSecondaryImages)
    showMaps = str(showMaps)
    
    tempdir = tempfile.TemporaryDirectory()
    data1_nrrd = os.path.join(tempdir.name,"img.nrrd")
    table_csv = os.path.join(tempdir.name, "table.csv")
    img_ef_tif = os.path.join(tempdir.name,"img_ef.tif")
    img_volume_tif = os.path.join(tempdir.name,"img_volume.tif")
    img_id_tif = os.path.join(tempdir.name,"img_id.tif")
    img_b_tif = os.path.join(tempdir.name,"img_b.tif")
    img_c_tif = os.path.join(tempdir.name,"img_c.tif")
    img_ab_tif = os.path.join(tempdir.name,"img_ab.tif")
    img_bc_tif = os.path.join(tempdir.name,"img_bc.tif")
    img_seed_points_tif = os.path.join(tempdir.name,"img_seed_points.tif")
    img_flinn_peak_plot_tif = os.path.join(tempdir.name,"img_flinn_peak_plot.tif")
    img_unweighted_flinn_plot_tif = os.path.join(tempdir.name,"img_unweighted_flinn_plot.tif")
    data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
    table_csv = os.path.join(tempdir.name,"table.csv")
    outputdir = os.path.join(tempdir.name, "outputdir")
    macro_file = os.path.abspath(os.path.join(os.path.dirname(__file__),"Macros/Ellipsoid_Factor_API_Test.py"))
    
    # save to temporary directory
    header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

    nrrd.write(data1_nrrd,array,header)
    
    
    
    fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                         " \'image="+"\""+data1_nrrd+"\"", ", img_ef_tif="+"\""+img_ef_tif+"\"",
                         ", img_volume_tif="+"\""+img_volume_tif+"\"",", img_id_tif="+"\""+img_id_tif+"\"",
                         ", img_b_tif="+"\""+img_b_tif+"\"",", img_c_tif="+"\""+img_c_tif+"\"",
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
                         ", table_csv="+"\""+table_csv+"\""+"\'"])
    
    b= subprocess.call(fiji_cmd,shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    with open(outputdir+f"table.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
        clean_metric_dict = {
            key: value[0].strip('"')
            for key, value in metric_dict.items()
        }

        for idx, (key, value) in enumerate (clean_metric_dict.items()):
            if idx ==0:
                continue
            print(key + ":", value)
            
            output_names = [
    "img_ef",
    "img_volume",
    "img_ab",
    "img_bc",
    "img_b",
    "img_c",
    "img_flinn_peak_plot"]
        
    for name in output_names:
        
        optional_dict={}
        if showMaps=="True":
            img_path = outputdir + name + ".tif"
            img_tif = tiff.imread(img_path)
            z_center = img_tif.shape[2] // 2
            plt.figure()
            plt.imshow(img_tif[:, :, z_center])
            plt.title(name) 
            plt.axis("off")
            plt.show()  
    return clean_metric_dict, img_tif


if __name__ == "__main__":

    filepath = "/BoneJ_Headless/ROIs/emu.nrrd"
    #8 bit 3D numpy array 
    array,array1header = nrrd.read(filepath)
    voxel_size = [25,25,25] #microns 
    fiji_path = "~/Fiji.app/ImageJ-linux64"
       
    Thickness_result = Thickness(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
    Separation_result = Separation(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
    Area_VolumeFraction_result = Area_VolumeFraction(array,voxel_size,fiji_path)
    Connectivity_result = Connectivity(array,voxel_size,fiji_path)
    Anisotropy_result = Anisotropy(array,voxel_size,fiji_path,NDirs = 2000, nLines = 10000, samplingincrement = 1.73,
    radii = False, eigens = False)
    Ellipsoid_factor_result = Ellipsoid_Factor(array, voxel_size, fiji_path,nVectors = 100,vectorIncrement =.435,skipRatio =50,contactSensitivity = 1
    ,maxIterations = 100,maxDrift = 1.73,runs = 1,seedOnDistanceRidge = True,distanceThreshold = .6,seedOnTopologyPreserving = True
    ,showFlinnPlots = True,showConvergence = True,showSecondaryImages = True,showMaps = True) 

    
   
