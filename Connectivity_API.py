# @CommandService cs
#@ DatasetIOService io
#@ UIService ui
# @Context ctxt


#@ String image
#@ String table_csv
#@ String NAME
from ij import IJ
from net.imglib2.img import ImagePlusAdapter
import csv

#Prevents unicode error 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from net.imagej import ImgPlus
from net.imagej.axis import Axes
from net.imglib2.img import Img

from net.imagej import DefaultDataset
import ij.ImagePlus;
from io.scif.img import ImgOpener
from org.bonej.utilities import SharedTable
from ij import ImagePlus
import net.imagej.ImgPlus;
from ij.io import FileSaver


#Open image from path 
input_dir = "/gpfs_projects_old/sriharsha.marupudi/Segmentations_Otsu_L1/"
outputdir = "/gpfs_projects_old/sriharsha.marupudi/Connectivity_Measurements_L1/"

IJ.run("Clear BoneJ results");
IJ.open(image)
input_Image = IJ.getImage() # BoneJ2 Thickness wrapper requires IJ1 image data, ImagePlus
input_image_ij1 = IJ.run(input_Image,"Multiply...", "value=255 stack"); 
#Preprocess with purify to locate all particles in 3D and removes all but the largest foreground and background particles as a filtering step to prepare images for Connectivity
input_image_ij2 = IJ.run("Purify");
#open input image as ImagePlus and converts to ImgPlus to be compatabile with wrapper

output = ImagePlusAdapter.wrapImgPlus(input_Image) 
wrapper = cs.run("org.bonej.wrapperPlugins.ConnectivityWrapper", False, ["inputImage",output])
wrapperInstance = wrapper.get()

#Save results to csv file 
table =SharedTable.getTable()
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


			

			