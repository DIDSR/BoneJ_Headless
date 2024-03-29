6#!/usr/bin/env python3
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
import tempfile 

filepath = "/BoneJ_Headless-main/ROIs/emu.nrrd"

array, array_header = nrrd.read(filepath)  # should be a numpy array
voxel_size = [51.29980, 51.29980, 51.29980]  # microns
fiji_path = "~/Fiji.app/ImageJ-linux64"

nLines_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
NDirs_list = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
csv_dir = "/gpfs_projects/sriharsha.marupudi/BoneJ_Headless/Anisotropy_Convergence_Test.csv"  # location of csv file storing anisotropy convergence measurements 
os.makedirs(csv_dir, exist_ok=True)

def Anisotropy_Convergence(array, voxel_size, fiji_path, NDirs=NDirs_list, nLines=nLines_list, samplingincrement=1.73, radii=False, eigens=False):
    for i in NDirs_list:
        for c in nLines_list:
            NDirs = str(i)
            nLines = str(c)
            samplingincrement = str(samplingincrement)
            radii = str(radii)
            eigens = str(eigens)

            tempdir = tempfile.TemporaryDirectory()
            data1_nrrd = os.path.join(tempdir.name, "img.nrrd")
            table_csv = os.path.join(tempdir.name, "table.csv")
            outputdir = os.path.join(tempdir.name, "outputdir")
            macro_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "Macros/Anisotropy_API_Test.py"))

            # save to temporary directory
            header = {'units': ['um', 'um', 'um'], 'spacings': voxel_size}

            nrrd.write(data1_nrrd, array, header)

            fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " " + macro_file,
                                " \'image=" + "\"" + data1_nrrd + "\"",
                                ", NDirs=" + "\"" + NDirs + "\"",
                                ", nLines=" + "\"" + nLines + "\"",
                                ", samplingincrement=" + "\"" + samplingincrement + "\"",
                                ", radii=" + "\"" + radii + "\"",
                                ", eigens=" + "\"" + eigens + "\"",
                                ", outputdir=" + "\"" + outputdir + "\"",
                                ", table_csv=" + "\"" + table_csv + "\"" + "\'"])

            b = subprocess.call(fiji_cmd, shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            with open(outputdir + f"table.csv", "r", encoding='utf-8') as file:
                reader = csv.reader(file)
                metric_dict = {row[0]: row[1:] for row in reader if row and row[0]}
                print(metric_dict)
if __name__ == "__main__":

    Anisotropy_Convergence(array, voxel_size, fiji_path, NDirs=NDirs_list, nLines=nLines_list,
           samplingincrement=1.73, radii=False, eigens=False)
