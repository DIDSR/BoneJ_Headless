#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 13:51:03 2022

@author: sriharsha.marupudi
"""

import numpy as np 
import numpy.ma as ma
import matplotlib.pyplot as plt
import nrrd 
from skimage import filters 
from skimage import measure
from skimage import exposure
from medpy import filter
from glob import glob
import os 

def triplanar_plot_save(image, figName):
    fig, axs = plt.subplots(1,3,figsize=(12,6))
    axs[0].imshow(image[150,:,:], interpolation="nearest", cmap="gray", vmin = 1e3, vmax=10e3); axs[0].axis("off")
    axs[1].imshow(image[:,150,:], interpolation="nearest", cmap="gray", vmin = 1e3, vmax=10e3); axs[1].axis("off")
    axs[2].imshow(image[:,:,150], interpolation="nearest", cmap="gray", vmin = 1e3, vmax=10e3); axs[2].axis("off")
    plt.savefig(figName)
    plt.close("all")

plt.ioff()


ROIDir = "/gpfs_projects_old/sriharsha.marupudi/Extract_ROI_Segs_L1/"
figDir = "/gpfs_projects_old/sriharsha.marupudi/roi_L1_figs_Segmentations_triplanar/"
sigma = .6
ROINRRD = glob(ROIDir+"ROI_*.nrrd")


for txt in ROINRRD:
    
    NAME = os.path.basename(txt).replace("ROI_","").replace(".nrrd","")
    
    print(f"Previewing normal sample {NAME}.")
    
    img1,header = nrrd.read(f"/gpfs_projects_old/sriharsha.marupudi/Extract_ROI_Segs_L1/ROI_{NAME}.nrrd")
     
    val_marrow = 2e3
    img1[img1<val_marrow] = val_marrow
    
    img = filters.gaussian(img1, sigma)
    image_slice = img[:,:,100]
    
    
    
    img_ad = filter.smoothing.anisotropic_diffusion(img, niter=10, kappa=100, gamma=0.1, voxelspacing=None, option=2)
    
    def filter_otsu(img):
        thresh =filters.threshold_otsu(img)
        return img > thresh
    
    img_otsu0 =filter_otsu(img)
    
    img_otsu =filter_otsu(img_ad)
    
    img_ad1 = img[:,:,100] > img_ad
    img_otsu1 = img_ad1 > img_otsu

    
    def plotall(img1,img2,img3,img4):
        plt.figure(figsize=(9, 4))
        plt.subplot(141)
        plt.imshow(img1[:,:,100], cmap='gray', interpolation='nearest')
        plt.axis('off')
        plt.subplot(142)
        plt.imshow(img2[:,:,100], cmap='gray', interpolation='nearest')
        plt.axis('off')
        plt.subplot(143)
        plt.imshow(img3[:,:,100], cmap='gray', interpolation='nearest')
        plt.axis('off')
        plt.subplot(144)
        plt.imshow(img4[:,:,100], cmap='gray', interpolation='nearest')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(figDir+f"{NAME}-Segmentation")
        plt.close()
        
     
    plotall(img, img_otsu0, img1, img_otsu)
   
    nrrd.write(f"/gpfs_projects_old/sriharsha.marupudi/ROI_Segmentations_grayscales_L1/Segmentation-{NAME}.nrrd",img_otsu.astype(np.uint8))

    # triplanar_plot_save(plotall, figDir+f"fig_{NAME}")
  
    # plt.figure(figsize=(9, 3.5))
    # plt.subplot(131)
    # plt.imshow(image_slice, cmap='gray')
    # plt.axis('off')
    # plt.subplot(132)
    # plt.imshow(img[:,:,100], cmap='jet')
    # plt.axis('off')
    # plt.subplot(133)
    # plt.imshow(img_threshold[:,:,100], cmap='jet')
    # plt.axis('off')
    # plt.show()
    
    # # read one of the grayscale roi files (replace the path with your own folder)
    # ind = 0
    # fig = plt.figure()
    # plt.imshow(img1[:,:,100],cmap="gray")
    # plt.contour(img_otsu[:,:,100],level=0.5,linewidths=0.5)
    # plt.axis("off")
    # # plt.savefig(figDir+f"{NAME}-Overlay")
    # # triplanar_plot_save(fig,figDir+f"fig_{NAME}-Overlay")
    # plt.close()
    
    
    plt.figure(figsize=(9, 3.5))
    plt.subplot(131)
    plt.imshow(img1[:,:,100],cmap="gray")
    plt.contour(img_otsu[:,:,100],level=0.5,linewidths=0.5)
    plt.axis('off')
    plt.subplot(132)
    plt.imshow(img1[:,100,:],cmap="gray")
    plt.contour(img_otsu[:,100,:],level=0.5,linewidths=0.5)
    plt.axis('off')
    plt.subplot(133)
    plt.imshow(img1[100,:,:],cmap="gray")
    plt.contour(img_otsu[100,:,:],level=0.5,linewidths=0.5)
    plt.axis('off')
    plt.savefig(figDir+f"{NAME}-Overlay")
    
    
    