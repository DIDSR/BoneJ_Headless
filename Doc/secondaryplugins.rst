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

Estimates surface area of a 3D volume. 
    
Function = ``def SurfaceArea(array, voxel_size, fiji_path):``
    
array = Numpy array of the image

voxel_size = Size of the voxels in the image, ex. [51.2,51.2,51.2]. Module assumes microns. 

fiji_path = Path to the users local Fiji installation 

Results
+++++++++++++++++++++++
Surface Area = surface area of resultant mesh in units of microns. 


------------------------------------
Skeletonization 
------------------------------------
Computes topological skeleton of input image. Noise in the image should be reduced. 
Function = ``def Skeletonization(array, voxel_size, fiji_path, ):``


Results
+++++++++++++++++++++++
Returns skeleton of binary image. 


------------------------------------
Analzye Skeleton
------------------------------------
Measure the number of branches and junctiuons of a skeletonized image. 
Function = ``def Analyzeskeleton(array, voxel_size, fiji_path,prune_ends=True,show_trees=False):``

Results
+++++++++++++++++++++++
Image stack of labelled branches and junctions 

If show trees is selected, an image stack of labelled tree is saved. Each individual tree will appear in red. 
Table will display: 
Image: Name of image 
Tree: Identifier
Branches: Number of branches
Junctions: Number of junctions
End Points: Number of end points, if pruned this is equal to 0
Junction Voxels: The number of voxels in each junction
Triple Points: Junctions with 3 branches
Slab Voxels: Ordinary branch voxels
Mean Branch Length: Branch average length
Max Branch Length: Longest branch length
Total Branch Length: Branch length sum

------------------------------------
Fractal Dimension 
------------------------------------
This plugin uses the box-counting algorithm to estimate the fractal dimension of a binary image. Boxes of decreasing size are scanned over the image. THe number of bones that contain bone are denoted foreground and counted. A fractural structure is where the proportion fo boxes with foreground voxels increases as the box size in turn decreases.

Function = ``def Fractal_Dimension(array, voxel_size, fiji_path):``

Results
+++++++++++++++++++++++
A plot display box count and box size is genreated. The plot is on a log scale. 
The fractal dimension is represented as the slope from linear regression fit to box size vs box count. 
$r^2$ display the goodness of fit for the regression line ofthe box size vs box count plot. 
