.. _bonej-secondaryplugins-label:

=================
Secondary Plugins
=================

This section contians definitions and user instructions for the following plugins

* Surface Area
* Skeletonization 
* Analyze Skeleton 
* Intertrabecular Angles
* Fractal Dimension 



All  the plugins require 3D 8 bit binary images, the files are written and read as numpy arrays. 



------------------------------------
Surface Area
------------------------------------

Estimates surface area of mesh
    
Function = ``def SurfaceArea(array, voxel_size, fiji_path, showMaps, maskArtefacts:``
    
array = Numpy array of the image

voxel_size = Size of the voxels in the image, ex. [51.2,51.2,51.2]. Thickness module assumes microns. 

fiji_path = Path to the users local Fiji installation 

Results
+++++++++++++++++++++++
Surface Area = surface area of resultant mesh 



------------------------------------
Skeletonization 
------------------------------------

Results
+++++++++++++++++++++++





------------------------------------
Analzye Skeleton
------------------------------------


Results
+++++++++++++++++++++++





------------------------------------
Fractal Dimension 
------------------------------------

Results
+++++++++++++++++++++++

