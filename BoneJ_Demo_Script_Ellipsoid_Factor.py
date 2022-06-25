#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Requires 8 bit binary image as input 
#Image is a 3D np.array of type np.uint8, with binary values of 0 and 1

import numpy as np
from numpy import asarray
import nrrd
import csv 
import tempfile 
import os
import subprocess 
from glob import glob

ROIDir = "/gpfs_projects_old/sriharsha.marupudi/Segmentations_Otsu/"
nVectors = "70"
vectorIncrement = "2"
skipRatio = "1"
contactSensitivity = "1"
maxIterations = "50"
maxDrift = "1"
runs = "1"
seedOnDistanceRidge = "True"
distanceThreshold = ".8"
seedOnTopologyPreserving = "True"
showFlinnPlots = "True"
showConvergence = "True"
showSecondaryImages = "True"


ROINRRD = glob(ROIDir+"Segmentation-grayscale-*.nrrd")

for txt in ROINRRD:
    
    NAME = os.path.basename(txt).replace("Segmentation-grayscale-","").replace(".nrrd","")

    print(f"output ROI{NAME}.")
    
    
    tempdir = "/gpfs_projects_old/sriharsha.marupudi/Ellipsoid_Factor_Measurements"
    data1_nrrd = os.path.join(tempdir,"img.nrrd")
    table_csv = os.path.join(tempdir, "table.csv")
    img_ef_tif = os.path.join(tempdir,"img_ef.tif")
    img_volume_tif = os.path.join(tempdir,"img_volume.tif")
    img_id_tif = os.path.join(tempdir,"img_id.tif")
    img_a_tif = os.path.join(tempdir,"img_a.tif")
    img_b_tif = os.path.join(tempdir,"img_b.tif")
    img_c_tif = os.path.join(tempdir,"img_c.tif")
    img_ab_tif = os.path.join(tempdir,"img_ab.tif")
    img_bc_tif = os.path.join(tempdir,"img_bc.tif")
    img_seed_points_tif = os.path.join(tempdir,"img_seed_points.tif")
    img_flinn_peak_plot_tif = os.path.join(tempdir,"img_flinn_peak_plot.tif")
    img_unweighted_flinn_plot_tif = os.path.join(tempdir,"img_unweighted_flinn_plot.tif")
    
    
    # TODO: from {file with your BoneJ wrapper} import compute_bonej_thickness
    data1,data1header1 = nrrd.read(f"/gpfs_projects_old/sriharsha.marupudi/Segmentations_Otsu/Segmentation-grayscale-{NAME}.nrrd")
    ### save data1 to temporaryDirectory
    header = {'units': ['um', 'um', 'um'],'spacings': [51.29980,51.29980,51.29980]}
    nrrd.write(data1_nrrd,data1,header)

    
    # TODO: run your BoneJ thickness wrapper
    # table is the boneJ table, thickness_image is a numpy array containing thickness image
    macro_file = "/gpfs_projects_old/sriharsha.marupudi/Ellipsoid_Factor_API.py"
    
    fiji_path = "~/Fiji.app/ImageJ-linux64" #home directory
    
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
                         ", NAME="+"\""+NAME+"\"",
                         ", table_csv="+"\""+table_csv+"\""+"\'"])
    b = subprocess.call(fiji_cmd, shell=True)
    # with open(f"/gpfs_projects_old/sriharsha.marupudi/Ellipsoid_Factor_Measurements/ROI-{NAME}-table.csv", "r",) as file:
    #     reader = csv.reader(file)
    #     result = {row[0]:row[1:] for row in reader if row and row[0]}
    # print(result)
    
    
    