#@CommandService cs
#@ DatasetIOService io
#@ UIService ui
#@Context ctxt


#@ String image
#@ String table_csv
#@ String img_ef_tif
#@ String img_volume_tif
#@ String img_id_tif
#@ String img_a_tif
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
#@ String NAME
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
#Open image from path 
outputdir 
IJ.run("Clear BoneJ results");
#open input image as I2-style image to be compatabile with wrapper
input_image = IJ.openImage(image)
output = ImagePlusAdapter.wrapImgPlus(input_image) 
#"inputImage",output,"nVectors",100,"vectorIncrement",3,"skipRatio",1,"contactSensitivity",1,"maxIterations",50,"maxDrift",1.0,"runs",1,"seedOnDistanceRidge",True,"distanceThreshold",0.8,"seedOnTopologyPreserving",True,"showFlinnPlots",True,"showConvergence",True,"showSecondaryImages",True,"])
#Run Ellipsoid Factor Plugin specifying parameters 
wrapper = cs.run("org.bonej.wrapperPlugins.EllipsoidFactorWrapper", False, ["inputImage",output,"nVectors",nVectors,"vectorIncrement",vectorIncrement,"skipRatio",skipRatio,"contactSensitivity",contactSensitivity,"maxIterations",maxIterations,"maxDrift",maxDrift,"runs",runs,"seedOnDistanceRidge",seedOnDistanceRidge,"distanceThreshold",distanceThreshold,"seedOnTopologyPreserving",seedOnTopologyPreserving,"showFlinnPlots",showFlinnPlots,"showConvergence",showConvergence,"showSecondaryImages",showSecondaryImages])
wrapperInstance = wrapper.get()
outputs = wrapperInstance.getOutput("ellipsoidFactorOutputImages")

EF = outputs.get(0)



table =SharedTable.getTable()


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
			
# print(table)



d = DefaultDataset(ctxt,EF)
io.save(d, outputdir+"/"+"ROI-"+NAME+"-img_ef.tif")

# V = outputs.get(1)

# d = DefaultDataset(ctxt,V)
# io.save(d, outputdir+"/"+"ROI-"+NAME+"-img_volume.tif")

# #ID = outputs.get(2)
# #d = DefaultDataset(ctxt,ID)
# #io.save(d, outputdir+"/"+"ROI-"+NAME+"-img_id2.tif")

# AB = outputs.get(6)
# d = DefaultDataset(ctxt,AB)
# io.save(d, outputdir+"/"+"ROI-"+NAME+"-img_ab.tif")

# BC = outputs.get(7)
# d = DefaultDataset(ctxt,BC)
# io.save(d, outputdir+"/"+"ROI-"+NAME+"-img_bc.tif")

# #A = outputs.get(3)
# #d = DefaultDataset(ctxt,A)
# #io.save(d, outputdir+"/"+"ROI-"+NAME+"-img_a1.tif")

# B = outputs.get(4)
# d = DefaultDataset(ctxt,B)
# io.save(d, outputdir+"/"+"ROI-"+NAME+"-img_b.tif")

# C = outputs.get(5)
# d = DefaultDataset(ctxt,C)
# io.save(d, outputdir+"/"+"ROI-"+NAME+"-img_c.tif")

# FlinnPlots = outputs.get(9)
# d = DefaultDataset(ctxt,FlinnPlots)
# io.save(d, outputdir+"/"+"ROI-"+NAME+"-img_flinn_peak_plot.tif")



	
