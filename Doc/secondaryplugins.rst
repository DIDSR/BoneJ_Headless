.. _bonej-secondaryplugins-label:

=================
Secondary Plugins
=================

This section contians definitions and user instructions for the following plugins

* Surface Area
* Skeletonise
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
Skeletonise
------------------------------------
Computes topological skeleton of input image. Noise in the image should be reduced. 

Function = ``def Skeletonise(array, voxel_size, fiji_path):``


Results
+++++++++++++++++++++++
Returns skeleton of binary image as a tiff file. 


------------------------------------
Analzye Skeleton
------------------------------------
Measure the number of branches and junctiuons of a skeletonized image. 

Function = ``def Analyze_Skeleton(array,voxel_size,fiji_path,pruneCycleMethod,pruneEnds,
excludeRoi,calculateShortestPaths,verbose=True,displaySkeletons):``

array = Numpy array of the image

voxel_size = Size of the voxels in the image, ex. [51.2,51.2,51.2]. Module assumes microns. 

fiji_path = Path to the users local Fiji installation 

pruneCycleMethod = Prune loops in the skeleton. Options are None, Shortest branch, Lowest intensity voxel, or Lowest intensity branch. None indicates no pruning. 
Shortest branch indicates the middle point of the shortest branch will be cut. Lowest intensity voxel indicates the darkest voxel will be set to 0. 
Lowest intensity branch indicates the darkest average branch of the loop branches will be cut in the darkest voxel.

pruneEnds = If True, the ends of branches with endpoints will be cut. 

excludeRoi = If True, if an ROI is selected it will be excluded from pruning. 

calculateShortestPath = If True, the shortest path of the skeleton will be computed and displayed in the skeleton. 

verbose = If True, the following information is displayed. skeleton ID,calibrated branch length,3D coordinates of the extremes of the branch, 
and the Euclidean distance between the extreme points. 

displaySkeletons= If True, the skeleton of the image will be displayed as a tiff image. 


Results
+++++++++++++++++++++++

Image stack of labelled branches and junctions 

If show trees is selected, an image stack of labelled tree is saved. Each individual tree will appear in red. 

Table will display: 

Image= Name of image 

Tree= Identifier

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
This plugin uses the box-counting algorithm to estimate the fractal dimension of a binary image. Boxes of decreasing size are scanned over the image. The number of bones that contain bone are denoted foreground and counted. A fractural structure is where the proportion fo boxes with foreground voxels increases as the box size in turn decreases.

Function = ``def Fractal_Dimension(array,voxel_size,fiji_path,startBoxSize=48,smallestBoxSize=6,scaleFactor=1.2,autoParam=True):``

array = Numpy array of the image

voxel_size = Size of the voxels in the image, ex. [51.2,51.2,51.2]. Module assumes microns. 

fiji_path = Path to the users local Fiji installation 

startBoxSize = The size  in pixels of the box in the sampling grid in the first iteration of the plugin. Default = 48.  

smallestBoxSize = The minimum size in pixels of a box in the grid. If the box size becomes smaller than this value, the plugin will iterate one final time, and then cease. Default = 6. 

scaleFactor =  The value used to divide the box after each iteration of the plugin. A value of 2.0 will decrease the box by half after each step. Default = 1.2. 

autoParam = If True, default parameters will be used. 

Results
+++++++++++++++++++++++
A plot display box count and box size is genreated. The plot is on a log scale. 


Fractal Dimension = Represented as the slope from linear regression fit to box size vs box count. 


$r^2$ = The goodness of fit for the regression line ofthe box size vs box count plot. Values closer to 1 are considered stronger. 

------------------------------------
Intertrabecular Angles
------------------------------------

This plugin computes the angles between trabeculae in bone images. The input image is skeletonised. A graph of the largest skeleton by number of nodes is generated. THe skeleton is composed of nodes(vertices) and connecting edges(branches).The edges correspond to trabeculae with the nodes corresponding to where the trabeculae meet in the bone. 

Function = ``Intertrabecular_Angles(array,voxel_size,fiji_path,minimumValence,maximumValence,marginCutOff
,minimumTrabecularLength,iteratePruning,printCentroids,useClusters,printCulledEdgePercentages):``

minimumValence = The minimum number of branches for a node to be analyzed.  

maximumValence = The maximum number of branches for a node to be analyzed. 

minimumTrabecularLength = The minimum length to retain a branch following pruning. The length is in the units of image calibration, microns, mm, etc. 

marginCutOff = The minimum distance of a node from from the image edge to be analyzed. Too many nodes close to the edges can result in decreasing accuracy. 

iteratePruning = If True, the skeleton will be prunted until there are no more short branches. 

useClusters = If True, results are pruned independently of graph transversal order. 

printCentroids = If True, the centroids of the node pairs on the ends of each edge in the skeleton will be displayed. .

PrintCulledEdgePercentages = If True, statistics of the pruned edges will be displayed. 

Results
+++++++++++++++++++++++
Intertrabecular angles = The angles in radians between each branch of each node that was analyzed by the plugin. The results are sorted into columns based on the number of branches per individual node. 

Centroids = If printCentroids is True, the table of the center coordinates of the node pairs at the ends of each edge.

Culled edge percentages =  If PrintCulledEdgePercentages is True, percentages of the different types of pruned edges is displayed. 

