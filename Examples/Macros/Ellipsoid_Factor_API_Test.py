#@ CommandService cs
#@ DatasetIOService io
#@ UIService ui
#@ Context ctxt


#@ String image
#@ String table_csv
#@ String img_ef_tif
#@ String img_volume_tif
#@ String img_id_tif
#@ String img_b_tif
#@ String img_c_tif
#@ String img_ab_tif
#@ String img_bc_tif
#@ String img_seed_points_tif
#@ String img_flinn_peak_plot_tif
#@ String img_unweighted_flinn_plot_tif
#@ String nVectors 
#@ String vectorIncrement
#@ String skipRatio
#@ String contactSensitivity
#@ String maxIterations
#@ String maxDrift
#@ String runs
#@ String distanceThreshold
#@ String seedOnDistanceRidge
#@ String seedOnTopologyPreserving
#@ String showFlinnPlots 
#@ String showConvergence 
#@ String showSecondaryImages
#@ String outputdir


from ij import IJ
from net.imglib2.img import ImagePlusAdapter
import csv

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
from net.imglib2.img.display.imagej import ImageJFunctions
 
outputdir
IJ.run("Clear BoneJ results");
input_image = IJ.openImage(image)
output = ImagePlusAdapter.wrapImgPlus(input_image) 
 
 
wrapper = cs.run("org.bonej.wrapperPlugins.EllipsoidFactorWrapper", False, ["inputImage",output,"nVectors",nVectors,"vectorIncrement",vectorIncrement,"skipRatio",skipRatio,"contactSensitivity",contactSensitivity,"maxIterations",maxIterations,"maxDrift",maxDrift,"runs",runs,"seedOnDistanceRidge",seedOnDistanceRidge,"distanceThreshold",distanceThreshold,"seedOnTopologyPreserving",seedOnTopologyPreserving,"showFlinnPlots",showFlinnPlots,"showConvergence",showConvergence,"showSecondaryImages",showSecondaryImages])
wrapperInstance = wrapper.get()
outputs = wrapperInstance.getOutput("ellipsoidFactorOutputImages")

EF = outputs.get(0)
d = DefaultDataset(ctxt,EF)
d = ImageJFunctions.wrap(d, "img_ef")
IJ.save(d, outputdir +"img_ef.tif")


V = outputs.get(1)
v = DefaultDataset(ctxt,V)
v = ImageJFunctions.wrap(v, "img_volume")
IJ.save(v, outputdir+"img_volume.tif")

 
AB = outputs.get(6)
AB = DefaultDataset(ctxt,AB)
AB = ImageJFunctions.wrap(AB, "img_ab")
IJ.save(AB, outputdir+"img_ab.tif")

BC = outputs.get(7)
BC = DefaultDataset(ctxt,BC)
BC = ImageJFunctions.wrap(BC, "img_bc")
IJ.save(BC, outputdir+"img_bc.tif")


B = outputs.get(4)
B = DefaultDataset(ctxt,B)
B = ImageJFunctions.wrap(B, "img_b")
IJ.save(d, outputdir+"img_b.tif")

C = outputs.get(5)
C = DefaultDataset(ctxt,C)
C = ImageJFunctions.wrap(C, "img_c")
IJ.save(C, outputdir+"img_c.tif")

FlinnPlots = outputs.get(9)
FlinnPlots = DefaultDataset(ctxt,FlinnPlots)
FlinnPlots = ImageJFunctions.wrap(FlinnPlots, "img_flinn_peak_plot")
IJ.save(FlinnPlots, outputdir+"img_flinn_peak_plot.tif")

table =SharedTable.getTable()

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
			
print(table)
