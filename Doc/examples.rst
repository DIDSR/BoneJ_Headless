.. _bonej-examples-label:
=================
Examples
=================
------------------------------------
BoneJ Module
------------------------------------
.. code-block:: python
    :linenos:
    
    import numpy as np 
    import nrrd
    import os
    import subprocess
    import tempfile
    import sys
    import matplotlib.pyplot as plt
    import tifffile as tiff
    from contextlib import contextmanager
    import sys, os

    from BoneJ_Module import Thickness
    from BoneJ_Module import Separation
    from BoneJ_Module import Area_VolumeFraction
    from BoneJ_Module import Connectivity
    from BoneJ_Module import Anisotropy
    from BoneJ_Module import Ellipsoid_Factor

    array,array1header = nrrd.read(volume)
    voxel_size = [51.29980, 51.29980, 51.29980] #microns 
    fiji_path = "~/Fiji.app/ImageJ-linux64"

    if __name__ == "__main__":
         Thickness_result = Thickness(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
         Separation_result = Separation(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
         Area_VolumeFraction_result = Area_VolumeFraction(array,voxel_size,fiji_path)
         Connectivity_result = Connectivity(array,voxel_size,fiji_path)
         Anisotropy_result = Anisotropy(array,voxel_size,fiji_path,NDirs = 2000, nLines = 10000, samplingincrement = 1.73,
         radii = False, eigens = False)
         Ellipsoid_Factor_result = Ellipsoid_Factor(array, voxel_size, fiji_path,nVectors = 100,vectorIncrement =.435,skipRatio =1,contactSensitivity = 1
         ,maxIterations = 100,maxDrift = .4,runs = 1,seedOnDistanceRidge = True,distanceThreshold = .6,seedOnTopologyPreserving = True
         ,showFlinnPlots = True,showConvergence = True,showSecondaryImages = True,showMaps = True)

------------------------------------
BoneJ Module Example Batch 
------------------------------------
.. code-block:: python
    :linenos:
    
    import numpy as np
    import nrrd
    import os
    import subprocess
    import tempfile
    import sys
    import matplotlib.pyplot as plt
    import tifffile as tiff
    from contextlib import contextmanager
    import sys, os
    from glob import glob
    import csv 
    # sys.path.append('/gpfs_projects/sriharsha.marupudi/BoneJ_Headless-main/BoneJ_Scripts/')
    from BoneJ_Module import Thickness
    from BoneJ_Module import Separation
    from BoneJ_Module import Area_VolumeFraction
    from BoneJ_Module import Connectivity
    from BoneJ_Module import Anisotropy
    from BoneJ_Module import Ellipsoid_Factor
    
    filepath = "/gpfs_projects/sriharsha.marupudi/BoneJ_Headless-main/ROIs/"
    voxel_size = [25,25,25] #microns 
    fiji_path = "~/Fiji.app/ImageJ-linux64"
    outdir = "/gpfs_projects/sriharsha.marupudi/BoneJ_Headless-main/ROIs/"
    csv_path = outdir + "output_metrics.csv"
    
    with open(csv_path, 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(["ROI Name", "Tb.Th Mean (µm)", "Tb.Sp Mean (µm)", "DA", "BV/TV", "Conn.D (µm⁻³)", "Median EF"])
    if __name__ == "__main__":
        Dir = glob(filepath+"*.nrrd")
        for file in Dir:
            
            NAME = os.path.basename(file).replace(".nrrd","")
            array,array1header = nrrd.read(filepath+NAME+".nrrd") 
            Thickness_result = Thickness(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
            Separation_result = Separation(array,voxel_size,fiji_path,showMaps = True, maskArtefacts = True)
            Area_VolumeFraction_result = Area_VolumeFraction(array,voxel_size,fiji_path)
            Connectivity_result = Connectivity(array,voxel_size,fiji_path)
            Anisotropy_result = Anisotropy(array,voxel_size,fiji_path,NDirs = 2000, nLines = 10000, samplingincrement = 1.73,
            radii = False, eigens = False)
            Ellipsoid_Factor_result = Ellipsoid_Factor(array, voxel_size, fiji_path,nVectors = 100,vectorIncrement =.435,skipRatio =1,contactSensitivity = 1
            ,maxIterations = 100,maxDrift = .4,runs = 1,seedOnDistanceRidge = True,distanceThreshold = .6,seedOnTopologyPreserving = True
            ,showFlinnPlots = True,showConvergence = True,showSecondaryImages = True,showMaps = True) 
            print(f"ROI-{NAME} Complete")
        
            # write results to csv
            csv_results = [f"{NAME}",
                          Thickness_result[0]['Tb.Th Mean (µm)'],Separation_result[0]['Tb.Sp Mean (µm)'],Anisotropy_result['DA'],
                          Area_VolumeFraction_result['BV/TV'],
                          Connectivity_result['Conn.D (µm⁻³)'],Ellipsoid_Factor_result[0]['Median EF']]
            
            with open(csv_path, 'a', newline='') as csv_file:
                csvwriter = csv.writer(csv_file)
                csvwriter.writerow(csv_results)
------------------------------------
BoneJ Secondary Module
------------------------------------
.. code-block:: python
    :linenos: 
    
    import numpy as np
    import nrrd
    import csv 
    import os
    import subprocess 
    from glob import glob
    import tempfile 
    import sys 
    import matplotlib.pyplot as plt 
    import tifffile as tiff 
    from contextlib import contextmanager
    import sys, os

    from BoneJ_Module import Fractal_Dimension  
    from BoneJ_Module import Surface_Area 
    from BoneJ_Module import Analyze_Skeleton 
    from BoneJ_Module import Intertrabecular_Angles 
    from BoneJ_Module import Skeletonise 
    
    array,array1header = nrrd.read(volume)
    voxel_size = [51.29980, 51.29980, 51.29980] #microns 
    fiji_path = "~/Fiji.app/ImageJ-linux64"
     
    if __name__ == "__main__":   
        Fractal_Dimension_Results = Fractal_Dimension(array,voxel_size,fiji_path,startBoxSize=48,smallestBoxSize=6,scaleFactor=1.2,autoParam=False)
        Surface_Area_Result= Surface_Area(array,voxel_size,fiji_path)
        Analzye_Skeleton_Result = Analyze_Skeleton(array,voxel_size,fiji_path,pruneCycleMethod=None,pruneEnds=True,excludeRoi=False,calculateShortestPaths=True,verbose=True,displaySkeletons=True)
        Intertrabecular_Angles_Result =                 Intertrabecular_Angles(array,voxel_size,fiji_path,minimumValence=3,maximumValence=50,marginCutOff=10,minimumTrabecularLength=0,iteratePruning=False,printCentroids=False,useClusters=False,printCulledEdgePercentages=False)
        Skeletonise_Result=Skeletonise(array,voxel_size,fiji_path)
    

------------------------------------
Anisotropy Parameter Convergence
------------------------------------
.. code-block:: python
    :linenos:
    
    
    import numpy as np
    import nrrd
    import csv 
    import os
    import subprocess 
    from glob import glob
    import tempfile 
    import sys 
    import matplotlib.pyplot as plt 
    from contextlib import contextmanager
    import sys, os


    array,array1header = nrrd.read(volume)  # should be a numpy array
    voxel_size = [51.29980, 51.29980, 51.29980] #microns 
    fiji_path = "~/Fiji.app/ImageJ-linux64"


    # feed in numpy array

    nLines_list = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]
    NDirs_list = [16,32,64,128,256,512,1024,2048,4096,8192]
    csv_dir = "/BoneJ_Headless/Anisotropy_Convergence_Test.csv" #location of csv file storing anisotropy convergence measurements 
    from Anisotropy_Parameter_Convergence import Anisotropy_Convergence

    if __name__ == "__main__":   
      Anisotropy_convergence_result=Anisotropy_Convergence(array,voxel_size,fiji_path,NDirs=NDirs_list, nLines=nLines_list, samplingincrement=1.73, radii=False, eigens=False,csv_dir=csv_dir)

   



------------------------------------
Ellipsoid Factor Convergence
------------------------------------
.. code-block:: python
    :linenos:
    
    
    import numpy as np
    import nrrd
    import csv 
    import os
    import subprocess 
    from glob import glob
    import tempfile 
    import sys 
    import matplotlib.pyplot as plt 
    from contextlib import contextmanager
    import sys, os


    array,array1header = nrrd.read(volume)  # should be a numpy array
    voxel_size = [51.29980, 51.29980, 51.29980] #microns 
    fiji_path = "~/Fiji.app/ImageJ-linux64"


    # feed in numpy array

    nLines_list = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]
    NDirs_list = [16,32,64,128,256,512,1024,2048,4096,8192]
    csv_dir = "/BoneJ_Headless/Ellipsoid_Factor_Convergence_Test.csv" #location of csv file storing anisotropy convergence measurements 
   
    from Ellipsoid_Factor_Convergence import Ellipsoid_Factor_Convergence 

    if __name__ == "__main__":  
        Ellipsoid_Factor_result = Ellipsoid_Factor_Convergence(array,voxel_size,fiji_path,csv_dir=csv_dir,nVectors = nVectors_list,
        vectorIncrement = VectorIncrement_list,
        skipRatio = skipRatio_list,
        contactSensitivity = contactSensitivity_list,
        maxIterations = maxIterations_list,
        maxDrift = maxDrift_list,
        runs = 1,
        seedOnDistanceRidge = True,
        distanceThreshold = .8,
        seedOnTopologyPreserving = True,
        showFlinnPlots = False,
        showConvergence = False)
