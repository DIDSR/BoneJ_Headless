# @CommandService cs
#@ DatasetIOService io
#@ UIService ui
# @Context ctxt


#@ String image
#@ String table_csv
#@ String NAME
#@ String startBoxSize 
#@ String smallestBoxSize
#@ String scaleFactor
#@ String autoParam



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
input_dir = "/gpfs_projects_old/sriharsha.marupudi/Segmentations_Otsu/"
outputdir = "/gpfs_projects_old/sriharsha.marupudi/Fractal_Dimension_Measurements/"
#IJ.run("Clear BoneJ results");
#open input image as I21-style image to be compatabile with wrapper "startBoxSize",48,"smallestBoxSize",6,"scaleFactor",1.2,"autoParam",True
input_image = IJ.openImage(image)
output = ImagePlusAdapter.wrapImgPlus(input_image) 
wrapper = cs.run("org.bonej.wrapperPlugins.FractalDimensionWrapper", False, ["inputImage",output,"startBoxSize",48,"smallestBoxSize",6,"scaleFactor",1.2,"autoParam",True])
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
			


