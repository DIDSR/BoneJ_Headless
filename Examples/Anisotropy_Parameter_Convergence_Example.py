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
csv_dir = "/BoneJ_Headless/Anisotropy_Convergence_Test.csv" #location of csv file storing anisotropy convergence measurements
import Anisotropy_Convergence

if __name__ == "__main__":
  Anisotropy_convergence_result=Anisotropy_Convergence(array,voxel_size,fiji_path,NDirs=NDirs_list, nLines=nLines_list, samplingincrement=1.73, radii=False, eigens=False,csv_dir=csv_dir)
