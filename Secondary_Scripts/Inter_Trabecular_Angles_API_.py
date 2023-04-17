#@ CommandService cs
#@ DatasetIOService io
#@ UIService ui
#@ Context ctxt

#@ String image
#@ String skeleton_nrrd
#@ String table_csv
#@ String NAME
#@ String outputdir
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
#"minimumvalence=3 maximumvalence=3 minimumtrabecularlength=0 margincutoff=0 iteratepruning=true useclusters=true printcentroids=false printcullededgepercentages=false")
wrapper = cs.run("org.bonej.wrapperPlugins.IntertrabecularAngleWrapper", False, ["inputImage",input_Image,"iteratePruning",False,"useClusters", False, "printCentroids", False,"printCulledEdgePercentages", False,"showSkeleton",False
,"minimumValence",3,"maximumValence",50,"minimumTrabecularLength",0,"marginCutOff",10])

#Need to confirm largest skeleton is being processed 
wrapperInstance = wrapper.get()
#skeleton= wrapper.getOutput("skeletonImage")
#IJ.save(skeleton_tif, outputdir+"skeleton.tif")


table = SharedTable.getTable()
print(table)

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
			

