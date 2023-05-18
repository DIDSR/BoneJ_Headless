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


array,array1header = nrrd.read(volume)  # should be a numpy array
voxel_size = [51.29980, 51.29980, 51.29980] #microns
fiji_path = "~/Fiji.app/ImageJ-linux64"


# feed in numpy array

nLines_list = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]
NDirs_list = [16,32,64,128,256,512,1024,2048,4096,8192]
csv_dir = "/BoneJ_Headless/Ellipsoid_Factor_Convergence_Test.csv" #location of csv file storing anisotropy convergence measurements

import Ellipsoid_Factor_Convergence

if __name__ == "__main__":
    Ellipsoid_Factor_result = Ellipsoid_Factor_Convergence(array,voxel_size,fiji_path,csv_dir=csv_dir,nVectors = nVectors_list,
    vectorIncrement = VectorIncrement_list,
    skipRatio = skipRatio_list,
    contactSensitivity = contactSensitivity_list,
    maxIterations = maxIterations_list,
    maxDrift = maxDrift_list,
    runs = 1,
    seedOnDistanceRidge = True,
    distanceThreshold = .8,
    seedOnTopologyPreserving = True,
    showFlinnPlots = False,
    showConvergence = False)
