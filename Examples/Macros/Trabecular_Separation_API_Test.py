# @CommandService cs
#@ DatasetIOService io
#@ UIService ui
#@ ConvertService convertService
# @Context ctxt

#@ String image
#@ String separation_tif
#@ String mapChoice
#@ String table_csv
#@ String showMaps
#@ String maskArtefacts
#@String outputdir
from ij import IJ

import os


from net.imagej import ImgPlus
from net.imagej import Dataset
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
outputdir

# Current BoneJ2's ThicknessWrapper (used for both thickness and separation)
# takes `inputDataset` (net.imagej.Dataset) rather than `inputImage`, and must be
# run with process=True so that the parameter's validater runs and assigns it.
# The image is opened with IJ.open(), which reads the NRRD voxel calibration, and
# converted with ConvertService, which keeps it; opening with io.open() drops it.
IJ.run("Clear BoneJ results");
IJ.open(image)
imp = IJ.getImage()
dataset = convertService.convert(imp, Dataset)

wrapper = cs.run("org.bonej.wrapperPlugins.ThicknessWrapper", True,
    ["inputDataset", dataset, "mapChoice", mapChoice, "showMaps", showMaps == "True", "maskArtefacts", maskArtefacts == "True"])
wrapperInstance = wrapper.get()
# separationMap is a Dataset, so it is saved with DatasetIOService (io.save);
# the legacy IJ.save expects an ImagePlus.
separation_tif = wrapperInstance.getOutput("separationMap")
if separation_tif is not None:
    io.save(separation_tif, outputdir + "separation.tif")

table = SharedTable.getTable()
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
			
