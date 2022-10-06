#@CommandService cs
#@ DatasetIOService io
#@ UIService ui
#@Context ctxt

#@ String image
#@ String thickness_tif
#@ String table_csv
#@ String showMaps
#@ String maskArtefacts
#@ String NAME
#@ String outputdir
from ij import IJ

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
#Prevents unicode error 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#Open image from path 
input_dir = "/gpfs_projects/sriharsha.marupudi/Segmentations_Otsu_L1/"
outputdir
# outputdir = "/gpfs_projects/sriharsha.marupudi/Measurements_Test/"

#open input image as IJ1-style image to be compatabile with wrapper  
#IJ.run("Clear BoneJ results");
IJ.run("Clear BoneJ results");
IJ.open(image)
input_Image = IJ.getImage() # BoneJ2 Thickness wrapper requires IJ1 image data, ImagePlus
input_image_ij1 = IJ.run(input_Image,"Multiply...", "value=255 stack"); 


#Run Trabecular Thickness Plugin specifying parameters 
wrapperThickness = cs.run("org.bonej.wrapperPlugins.ThicknessWrapper", False, ["inputImage",input_Image, "showMaps",showMaps,"maskArtefacts",maskArtefacts])
wrapperThicknessInstance = wrapperThickness.get()
#Call trabecular thickness map and save
thickness_tif = wrapperThicknessInstance.getOutput("trabecularMap")
#trabecular_map.show()
IJ.save(thickness_tif, outputdir +"ROI-"+ NAME +"-thickness.tif")

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
			
