#@ CommandService cs
#@ DatasetIOService io
#@ UIService ui
#@ Context ctxt
#@ String image
#@ String skeleton_nrrd
#@ String table_csv
#@ String outputdir
#@ String iteratePruning
#@ String minimumValence
#@ String maximumValence
#@ String minimumTrabecularLength
#@ String marginCutOff
#@ String useClusters
#@ String printCentroids
#@ String printCulledEdgePercentages
# String showSkeleton
#@ String skeleton_tif

from ij import IJ
import csv
from math import floor
import os
import org.scijava.ui.UIService;
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


#Run Intertrabecular Angles Plugin specifying parameters 
wrapper = cs.run("org.bonej.wrapperPlugins.IntertrabecularAngleWrapper", False, ["inputImage",input_Image,"iteratePruning",iteratePruning,"useClusters", useClusters, "printCentroids", printCentroids,"printCulledEdgePercentages", printCulledEdgePercentages,"minimumValence",minimumValence,"maximumValence",maximumValence,"minimumTrabecularLength",minimumTrabecularLength,"marginCutOff",marginCutOff])

#Need to confirm largest skeleton is being processed 
wrapperInstance = wrapper.get()
# skeleton_tif = wrapper.getOutput("skeletonImage")
# IJ.save(skeleton_tif, outputdir+"ROI-"+NAME+"-skeleton.tif")


table = SharedTable.getTable()
# print(table)

f = open(outputdir+"ROI-"+NAME+"-table.csv", 'wb')
f.write('\n')
f.write("rowname,")

for j in range(0,len(table[0])):
	f.write(table.getRowHeader(j)+",")
		
f.write('\n')

for i in range(0,len(table)):
	f.write(table.getColumnHeader(i)+",")
	for j in range(0,len(table[i])):
		f.write(str(table[i][j])+",")
	f.write('\n')
f.close()
			

