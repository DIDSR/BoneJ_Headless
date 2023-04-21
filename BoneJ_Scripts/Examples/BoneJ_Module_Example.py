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

import Thickness 
import Spacing
import Area_VolumeFraction
import Connectivity 
import Anisotropy 
import Ellipsoid_Factor

 if __name__ == "__main__":    
  Thickness_result = Thickness(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
  Spacing_result = Spacing(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
  Area_VolumeFraction_result = Area_VolumeFraction(array,voxel_size,fiji_path)
  Connectivity_result = Connectivity(array,voxel_size,fiji_path)
  Anisotropy_result = Anisotropy(array,voxel_size,fiji_path,NDirs = 2000, nLines = 10000, samplingincrement = 1.73, 
  radii = False, eigens = False)
  Ellipsoid_Factor(array, voxel_size, fiji_path,nVectors = 100,vectorIncrement =.435,skipRatio =1,contactSensitivity = 1
  ,maxIterations = 100,maxDrift = .4,runs = 1,seedOnDistanceRidge = True,distanceThreshold = .6,seedOnTopologyPreserving = True
  ,showFlinnPlots = True,showConvergence = True,showSecondaryImages = True)

   
    
    
    
    


    
   
