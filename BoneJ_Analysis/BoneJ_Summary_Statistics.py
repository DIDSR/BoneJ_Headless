#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:25:09 2022

@author: sriharsha.marupudi
"""

import pandas as pd 
import os 
import nrrd 
import numpy as np 
import matplotlib.pyplot as plt 

data=pd.read_csv("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print/Ellipsoid_Factor_results.csv",usecols=['rowname','img.nrrd'])
df = pd.DataFrame(data)
data1 = df.describe()
print (data1)
# data1.to_csv("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print_Summary/Anisotropy_Results_Summary.csv")
