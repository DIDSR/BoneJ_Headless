#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:43:52 2022

@author: sriharsha.marupudi
"""

import os
import glob
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import statistics as stats


def Thickness():
    out_dir1 = "/gpfs_projects/sriharsha.marupudi/Thickness_Measurements_Print"
    os.makedirs(out_dir1, exist_ok=True)
     
    data2=pd.read_csv("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print/Thickness_results.csv",usecols=['rowname','img.nrrd'])
    data2.plot(kind='hist',bins=12)
    plt.title("Thickness")
    plt.xlabel("Thickness (microns)")
    # plt.ylim([0,20])
    plt.ylabel("Number of ROIs")
    plt.text(0.82, 0.2, 'Mean = {:.2f}'.format(365.15), transform=plt.gca().transAxes)
    plt.text(0.82, 0.3, 'SD = {:.2f}'.format(51.90), transform=plt.gca().transAxes)
    plt.show()
    plt.savefig("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print_Thickness_Histogram.png")

def Spacing():
    out_dir2 = "/gpfs_projects/sriharsha.marupudi/Spacing_Measurements_Print"
    os.makedirs(out_dir2, exist_ok=True)      
    data2=pd.read_csv("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print/Spacing_results.csv",usecols=['rowname','img.nrrd'])
    data2.plot(kind='hist',bins=12)
    plt.title("Spacing")
    plt.xlabel("Spacing (microns)")
    # plt.ylim([0,20])
    plt.ylabel("Number of ROIs")
    plt.text(0.82, 0.2, 'Mean = {:.2f}'.format(1186.82), transform=plt.gca().transAxes)
    plt.text(0.82, 0.3, 'SD = {:.2f}'.format(185.651), transform=plt.gca().transAxes)
    plt.show()
    plt.savefig("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print_Spacing_Histogram.png")
    
def BVTV(): 
    
     
    data2=pd.read_csv("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print/Area_VolumeFraction_results.csv",usecols=['rowname','img.nrrd'])
    data2.plot(kind='hist',bins=12)
    plt.title("BV/TV")
    plt.xlabel("BV/TV")
    # plt.ylim([0,20])
    plt.ylabel("Number of ROIs")
    plt.text(0.82, 0.2, 'Mean = {:.2f}'.format(.18), transform=plt.gca().transAxes)
    plt.text(0.82, 0.3, 'SD = {:.2f}'.format(.05), transform=plt.gca().transAxes)
    plt.show()
    plt.savefig("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print_Area_VolumeFraction_Histogram.png")
    
def Anisotropy():
    out_dir1 = "/gpfs_projects/sriharsha.marupudi/Anisotropy_Measurements_Print"
    os.makedirs(out_dir1, exist_ok=True)
          
    data2=pd.read_csv("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print/Anisotropy_results.csv",usecols=['rowname','img.nrrd'])
    data2.plot(kind='hist',bins=12)
    plt.title("Anisotropy")
    plt.xlabel("DA")
    # plt.ylim([0,20])
    plt.ylabel("Number of ROIs")
    plt.text(0.82, 0.2, 'Mean = {:.2f}'.format(.43), transform=plt.gca().transAxes)
    plt.text(0.82, 0.3, 'SD = {:.2f}'.format(.11), transform=plt.gca().transAxes)
    plt.show()
    plt.savefig("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print_Anisotropy_Histogram.png")
    
def Connectivity():
    out_dir1 = "/gpfs_projects/sriharsha.marupudi/Connectivity_Measurements_Print"
    os.makedirs(out_dir1, exist_ok=True)
            
    data2=pd.read_csv("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print/Connectivity_results.csv",usecols=['rowname','img.nrrd'])
    data=pd.read_csv("/gpfs_projects/sriharsha.marupudi/BoneJ_Metrics_Printed_Volumes.csv",usecols=['Thickness'])
    data2.plot(kind='hist',bins=12)
    plt.title("Connectivity")
    plt.xlabel("Connectivity Density ($1/microns^3$)")
    # plt.ylim([0,20])
    plt.ylabel("Number of ROIs")
    mean = 1.93E09
    sd = 1.75E09
    plt.text(0.82, 0.2, 'Mean = {0:0.2e}'.format(mean), transform=plt.gca().transAxes)
    plt.text(0.82, 0.3, 'SD = {0:0.2e}'.format(sd), transform=plt.gca().transAxes)
    plt.show()
    plt.savefig("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print_Connectivity_Histogram.png")
    
def EF():
    out_dir1 = "/gpfs_projects/sriharsha.marupudi/Ellipsoid_Factor_Measurements_Print"
    os.makedirs(out_dir1, exist_ok=True)     
    data2=pd.read_csv("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print/Ellipsoid_Factor_results.csv",usecols=['rowname','img.nrrd'])

    data2.plot(kind='hist',bins=12)
    plt.title("Ellipsoid Factor")
    plt.xlabel("Ellipsoid Factor")
    # plt.ylim([0,20])
    plt.ylabel("Number of ROIs")
    plt.text(0.82, 0.2, 'Mean = {:.2f}'.format(.11), transform=plt.gca().transAxes)
    plt.text(0.82, 0.3, 'SD = {:.2f}'.format(.07), transform=plt.gca().transAxes)
    plt.show()
    plt.savefig("/gpfs_projects/sriharsha.marupudi/BoneJ_Results_Print_EF_Histogram.png")   
    
    
# Thickness()
# Spacing()
# BVTV()
# Anisotropy()
Connectivity()
# EF()


