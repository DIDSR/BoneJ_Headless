#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:56:26 2022

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
figDir = ".../{NAME}.png"
outDir = ".../{NAME}.nrrd"
sigma = .6
volume = "...nrrd"
img1,header = nrrd.read(volume)

val_marrow = 2e3
img1[img1<val_marrow] = val_marrow


img = filters.gaussian(img1, sigma)

img_ad = filter.smoothing.anisotropic_diffusion(img, niter=10, kappa=100, gamma=0.1, voxelspacing=None, option=2)

def filter_otsu(img):
    thresh =filters.threshold_otsu(img)
    return img > thresh
img_otsu =filter_otsu(img_ad)

nrrd.write(outDir,img_otsu.astype(np.uint8)

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
