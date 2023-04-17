# @CommandService cs
#@ DatasetIOService io
#@ UIService ui
# @Context ctxt

#@ String image
#@ String skeleton_tif
#@ String NAME
#@ String outputdir
from ij import IJ
import csv
from math import floor
import os


from net.imagej import ImgPlus
from net.imagej.axis import Axes
from net.imglib2.img import Img
from net.imagej import DefaultDataset
import ij.ImagePlus;
from io.scif.img import ImgOpener
from org.bonej.utilities import SharedTable
from ij import ImagePlus
from ij.io import FileSaver

#Open image from path 
outputdir

#open input image as IJ1-style image to be compatabile with wrapper  
IJ.run("Clear BoneJ results");
IJ.open(image)
input_Image = IJ.getImage() # BoneJ2 Thickness wrapper requires IJ1 image data, ImagePlus
input_image_ij1 = IJ.run(input_Image,"Multiply...", "value=255 stack"); 


#Run Skeletonise Plugin specifying parameters 
wrapper = cs.run("org.bonej.wrapperPlugins.SkeletoniseWrapper", False, ["inputImage",input_Image])
wrapperInstance = wrapper.get()
#Call skeleton and save
skeleton_tif = wrapperInstance.getOutput("skeleton")
IJ.save(skeleton_tif, outputdir + NAME +"-skeleton.tif")
