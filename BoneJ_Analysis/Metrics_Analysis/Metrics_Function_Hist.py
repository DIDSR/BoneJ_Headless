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
    data=pd.read_csv("/..csv)
    data.plot(kind='hist',bins=12)
    plt.title("Thickness")
    plt.xlabel("Thickness (microns)")
    plt.ylabel("Number of ROIs")
    plt.show()

def Separation(): 
    data=pd.read_csv("/..csv)
    data.plot(kind='hist',bins=12)
    plt.title("Separation")
    plt.xlabel("Separation (microns)")
    # plt.ylim([0,20])
    plt.ylabel("Number of ROIs")
    plt.show()
    
def BVTV():     
    data=pd.read_csv("/..csv")
    data.plot(kind='hist',bins=12)
    plt.title("BV/TV")
    plt.xlabel("BV/TV")
    # plt.ylim([0,20])
    plt.ylabel("Number of ROIs")
    plt.show()
    
def Anisotropy():   
    data=pd.read_csv("/..csv")
    data.plot(kind='hist',bins=12)
    plt.title("Anisotropy")
    plt.xlabel("DA")
    # plt.ylim([0,20])
    plt.ylabel("Number of ROIs")
    plt.show()
    
def Connectivity():
         
    data=pd.read_csv("/..csv")
    data.plot(kind='hist',bins=12)
    data2.plot(kind='hist',bins=12)
    plt.title("Connectivity")
    plt.xlabel("Connectivity Density ($1/microns^3$)")
    plt.ylabel("Number of ROIs")
    plt.show()
    
def EF():
    data=pd.read_csv("/..csv")
    data.plot(kind='hist',bins=12) 
    plt.title("Ellipsoid Factor")
    plt.xlabel("Ellipsoid Factor")
    plt.ylabel("Number of ROIs")
    plt.show()
    
    
Thickness()
Separation()
BVTV()
Anisotropy()
Connectivity()
EF()


