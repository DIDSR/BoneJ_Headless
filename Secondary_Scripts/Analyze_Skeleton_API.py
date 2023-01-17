# @CommandService cs
#@ DatasetIOService io
#@ UIService ui
# @Context ctxt

#@ String NAME 
#@ String image
#@ String skeleton_nrrd
#@ String table_csv
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
# input_dir = "/gpfs_projects/sriharsha.marupudi/extract_rois_output/"
# input_image_path = input_dir+"ROI-1_67960.nrrd"
# outputdir = "/gpfs_projects/sriharsha.marupudi/Analyze_Skeleton_Measurements/"
outputdir

#open input image as IJ1-style image to be compatabile with wrapper  
IJ.run("Clear BoneJ results");
IJ.open(image)
input_Image = IJ.getImage() # BoneJ2 Thickness wrapper requires IJ1 image data, ImagePlus
input_image_ij1 = IJ.run(input_Image,"Multiply...", "value=255 stack"); 


#Run Trabecular Thickness Plugin specifying parameters 
#"minimumvalence=3 maximumvalence=3 minimumtrabecularlength=0 margincutoff=0 iteratepruning=true useclusters=true printcentroids=false printcullededgepercentages=false")
wrapper = cs.run("org.bonej.wrapperPlugins.AnalyseSkeletonWrapper", False, ["inputImage",input_Image])
wrapperInstance = wrapper.get()
#Call skeleton and save
skeleton = wrapperInstance.getOutput("skeleton")

IJ.save(skeleton, outputdir+ "ROI-"+NAME+"-skeleton.tif")

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
			
