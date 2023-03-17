#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:22:01 2022

@author: sriharsha.marupudi
"""

import pydicom 
ds = pydicom.filereader.dcmread("/gpfs_projects/sriharsha.marupudi/Tensile_Scans/03909/C0003909_02183.DCM")
# ds = pydicom.filereader.dcmread("/gpfs_projects/sriharsha.marupudi/data/data/DICOM intact/1221-07131-L45/C0002220_01086.DCM")
print(ds)
