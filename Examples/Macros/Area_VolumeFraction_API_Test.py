# @CommandService cs
#@ DatasetIOService io
#@ UIService ui
#@ ConvertService convertService
# @Context ctxt

#@ String image
#@ String table_csv
#@ String outputdir

from ij import IJ
from net.imagej import Dataset
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
outputdir
IJ.run("Clear BoneJ results");
# Current BoneJ2 (7.2.2) renamed ElementFractionWrapper's input from `inputImage`
# (ImagePlus) to `inputDataset` (net.imagej.Dataset). It must be run with
# process=True: the parameter's validater is what assigns it, and process=False
# skips parameter processing, so run() fails with a NullPointerException.
#
# The image is opened with IJ.open(), which reads the NRRD voxel calibration, and
# converted with ConvertService, which keeps it. Opening it with io.open()
# (DatasetIOService) drops the calibration, so BV and TV come back in voxels
# rather than calibrated units (BV/TV itself is unaffected).
IJ.open(image)
imp = IJ.getImage()
dataset = convertService.convert(imp, Dataset)
wrapperBV = cs.run("org.bonej.wrapperPlugins.ElementFractionWrapper", True, ["inputDataset",dataset])
wrapperBVInstance = wrapperBV.get()

#Save results to csv file 
table =SharedTable.getTable()
# print(table)
f = open(outputdir+"table.csv", 'wb')
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


			

			
