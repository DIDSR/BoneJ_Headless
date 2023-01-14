# @CommandService cs
#@ DatasetIOService io
#@ UIService ui
# @Context ctxt
#@ String NAME


#@ String image
#@ String table_csv
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

IJ.run("Clear BoneJ results");
#Open image from path 
input_dir = "/gpfs_projects_old/sriharsha.marupudi/ROI_Segmentations_otsu_grayscales/"
input_image_path = input_dir+"ROI-1_67960.nrrd"
outputdir = "/gpfs_projects_old/sriharsha.marupudi/Surface_Area_Measurements/"
#IJ.run("Clear BoneJ results");
#open input image as IJ2-style image to be compatabile with wrapper 
input_image = IJ.openImage(image)
output = ImagePlusAdapter.wrapImgPlus(input_image) 
wrapper = cs.run("org.bonej.wrapperPlugins.SurfaceAreaWrapper", False, ["inputImage",output])
wrapperInstance = wrapper.get()


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
			


