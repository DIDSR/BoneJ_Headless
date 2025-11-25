.. _bonej-plugins-label:

=================
Primary Plugins
=================

This section contians definitions and user instructions for the following plugins

* Thickness
* Separation
* Anisotropy
* Connectivity
* Bone Volume Fraction
* Ellipsoid Factor


All  the plugins require 3D 8 bit binary images, the files are written and read as numpy arrays. 



------------------------------------
Thickness
------------------------------------

Fits spheres into every foreground voxel of a segmented image to determine the thickness of the trabecular microstructure. The diameter of the largest sphere that is able to fit inside the foreground voxel and contains the point for each point is measured by the plugin. The plugin outputs the mean thickness of the sample, standard deviation of the sample, and the max thickness value. 

    
Function = ``def Thickness(array, voxel_size, fiji_path, showMaps, maskArtefacts:``
    
array = Numpy array of the image

voxel_size = Size of the voxels in the image, ex. [51.2,51.2,51.2]. Thickness module assumes microns and that the voxels are isotropic (same spacing in x, y and z directions). 

fiji_path = Path to the user's local Fiji installation 

showMaps = True will generate a thickness map which is saved as optional_dict. False will generate no thickness map. 

maskArtefacts = True will remove foreground voxels that are not present in the original image from the final thickness map. Always recommended to select True, the artifacts can cause bias and distortions in the image. 

Results
+++++++++++++++++++++++


Mean Tb.Th = The mean trabecular thickness value of the image. 

Std Tb.Th = The standard deviation of the trabecular thickness values. 

Max Tb.Th = The max trabecular thickness value of the image. 


------------------------------------
Separation
------------------------------------

Fits spheres into every background voxel of a segmented image to determine the thickness of the of the marrow space between trabeculae. The diameter of the largest sphere that is able to fit inside the background voxel and contains the point for each point is measured by the plugin.

Function = ``def Separation(array, voxel_size, fiji_path, showMaps = True , maskArtefacts = False)``: 

array = Numpy array of the image

voxel_size = Size of the voxels in the image, ex. [51.2,51.2,51.2]. Separation module assumes microns and that voxels are isotropic (same spacing in x, y, and z directions). 

fiji_path = Path to the user's local Fiji installation 

showMaps = True will generate a separation map which is saved as optional_dict. False will generate no separation map. 

maskArtefacts = True will remove background voxels that are not present in the original image from the final separation map. Always recommended to select True, the artifacts can cause bias and distortions in the image. 

Results
+++++++++++++++++++++++


Mean Tb.Sp = The mean trabecular separation value of the image. 

Std Tb.Sp = The standard deviation of the trabecular separation values. 

Max Tb.Sp = The max trabecular separation value of the image. 


------------------------------------
Anisotropy
------------------------------------

Assigns a numerical value on a scale of 0-1 to quantify trabecular bone’s directionality. Degree of anisotropy is representative of the microstructure’s orientation. The closer to 0 the more isotropic a bone, the closer to 1 the more anisotropic a bone. 

Plugin uses mean intercept length vectors to calculate the degree of anisotropy. Vectors of equal length all emanating from the same random point within the image are drawn throughout. As the vectors change from the foreground to the background this is counted as an intercept for that specific vector. The vector length divided by the number of boundary hits (when foreground changes from background) gives the mean intercept length. A point cloud is generated which is representative of the vectors multiplied by the mean intercept length. The equation of an ellipsoid is solved that fits this point cloud. This gives eigenvalues related to the lengths of the axis of the ellipsoid along with eigenvectors that give the orientation of the ellipsoid axes. The Degree of Anisotropy is 1-(smallest eigenvalue)/(largest eigvenvalue). 

Plugin finds mean intercept length vectors from n directions where points change from the background to the foreground. Parallel lines over an input image are drawn where each line segment in an image sample points from background to foreground. The MIL vectors are then plotted into a point cloud around the origin. The equation of an ellipsoid is solved that fits the point cloud. The Degree of Anisotropy is measured based on the ellipsoid radii. 

Function = ``def Anisotropy(array, voxel_size, fiji_path, NDirs = 2000, nLines = 10000, samplingincrement = 1.73, radii = False, 
eigens = False, MILvectors = False):``  

Directions = Number of times the sampling is performed from various directions. Min value is 9. Recommended value is 2000. 

Lines per direction = The number of parallel lines drawn in each direction. Recommended value 10000. 

Sampling Increment = The distance between sampling points along a line. Minimum, default, and recommended value is 1.73. 

radii = True of False. If True is input the radii of the fitted ellipsoid results are output. 

eigens = True or False. If True is input the eigenvectors and values of the fitted ellipsoid is output 

It is best to run a convergence analysis to determine the best parameters for Anisotropy. Recommended parameters may not give stable results in a reasonable amount of time. An ImageJ macro has been included for this. 

Results
+++++++++++++++++++++++

Degree of anisotropy = Quantitative value representing the directionality of trabecular bone sample. 0 is isotropic, 1 is anisotropic. The higher the value the more orientation in the microstructure of the bone. 

Radii of fitted ellipsoid = Radii lengths, a<b<c of the ellipsoid fit to the point cloud. Used to calculate degree of anisotropy. DA=1/c^2 -1/a^2 . Only output if radii is set to True. 

Eigenvectors and values = Values of the x,y,,z components of the three eigvenctors of the ellipsoid fit to the point cloud (m00,m01,m02..). Eigenvalues are listed as D1,D2,D3  which correspond 1/c^2 ,1/b^2 ,1/a^2 , a,b,c are the radii of the ellipsoid fit to the point cloud vector. 


------------------------------------
Connectivity 
------------------------------------

Plugin determines the number of connected structures in the image. The connected structures are representative of trabeculae in a trabecular network. Connectivity is determined from measuring the Euler characteristic denoted χ. The Euler characteristic is a topologically invariant value meant to describe a shape or structure regardless of how it is bent. It is defined as χ = objects – handles + cavities. A handle is analogous to a hole through an object, while a cavity hole enclosed inside of an object. 

Before Connectivity is run the plugin Purify is run within the script. Purify is a preprocessing step that filters an image by removing all particles but the largest foreground and background particles. Once purify is run there is a single connected bone phase and a single connected marrow phase. From there the Euler characteristic is calculated for every bone voxel in the image. The intersection of voxels and stack edges is checked to calculate the bone’s contribution to the Euler characteristic of the bone it is connected to. Connectivity is 1- Δχ, connectivity density is defined as Connectivity/stack volume. 

Function = ``def Connectivity(array,voxel_size,fiji_path):`` 

array = Numpy array of the image

voxel_size = Size of the voxels in the image, ex. [51.2,51.2,51.2]. Assumes microns

fiji_path = Path to the users local Fiji installation 

Results
+++++++++++++++++++++++


Euler characteristic =  Euler characteristic of the sample if it were floating in space

Corrected Euler = The contribution of the bone sample to the Euler characteristic of the bone to which it is connected

Connectivity = Connectivity of the image described as the number of trabeculae 

Connectivity Density = The number of trabeculae per unit volume


------------------------------------
Bone Volume Fraction 
------------------------------------
Calculates Bone Volume/Total Volume, the volume of mineralized bone per unit volume of the sample. Foreground voxels which represent trabecular bone are divided by the total number of voxels in the image. 

Function = ``def Area_VolumeFraction(array,voxel_size,fiji_path):`` 

array = Numpy array of the image

voxel_size = Size of the voxels in the image, ex. [51.2,51.2,51.2]. Module assumes microns. 

fiji_path = Path to the users local Fiji installation 

Results
+++++++++++++++++++++++

Bone volume: Volume of bone voxels 

Total volume: Volume of entire image

BV/TV: Ratio of Bone volume to total volume of the image 

------------------------------------
Ellipsoid Factor
------------------------------------
Quantifies the rod and plate geometry of trabecular microstructures. Ellipsoid Factor is evaluated on a scale of -1 to +1, with -1 corresponding to an oblate plate like geometry, and +1 corresponding to a prolate rod like geometry. Ellipsoids are iteratively fit into foreground voxels in the image. TProlate, oblate, and intermediate ellipsoid axis lengths are used to quantify how rod-like or plate-like the structure is at a specific point. 

Function = ``def Ellipsoid Factor(array,voxel_size,fiji_path):`` 

array = Numpy array of the image

voxel_size = Size of the voxels in the image, ex. [51.2,51.2,51.2]. Module assumes microns. 

fiji_path = Path to the users local Fiji installation 

nVectors: The number of vectors that is sampled at each seed point of the ROI. Default 100. 

vectorIncrement: The distance between the sampling points for each vector of the ROI. Default 0.435. 

skipRatio: The density of sampling within the ROI. Set to 1 indicates that ellipsoid is sampled at every seed point in the ROI. Default 50. 

contactSensitivity: How many sampled vectors touch the background of the image prior to stopping dilation.  Default 1. 

maxIterations: How many attempts will be made to find larger ellipsoids for fitting into seed points. Default 100. 

maxDrift: How far centroid of ellipsoid is displaced from seed point within ROI. Default 1.73. 

runs: Number of time Ellipsoid Factor is run, results are averaged. Default 1. 

distanceThreshold: Threshold for distance ridge, default 0.60. 

seedonDistanceEdge: Uses distance ridge to determine the centroids for fit ellipsoids. Default True. 

seedOnTopologyPreserving: Medial axis thinning is used to determine starting point for fit ellipsoids. Default True. 

showFlinnPlots: Generate plots showing the ratio between ellipsod axes. Ratio of axes a/b and b/a will be shown on Cartesian axes. Default True 

showConvergence: Displays convergence of Ellipsoid Factor algorithim. Default True. 

showSecondaryImages: Generate image stacks showing the following plots: seed points, ellipsoid axis ratios, a/b and b/c., ellipsoid axis lengths, a, b, c,, ellipsoid ID, ellipsoid volume. Default False. 

showMaps: Indicate if the user wants to output all the images genearted by Ellipsoid Factor. Default True. 

Results
+++++++++++++++++++++++
Median EF: Average EF value for the sample. On a scale of -1 to +1. Values closer to -1, indicate the structures in the sample have an oblate plate-like geometry. Values closer to +1, indicate the structures have a javeline rod-like geometry. 

Max EF: Largest EF value for a sample. 

Min EF: Lowest EF value for a sample. 

Filling Percentage: The percentage of voxels that are successfully fit with ellipsoids. This value must be greater then 90% for EF values to be accurate. 

Number of Ellipoids Found in Total: Total number of ellipsoids fit into the foreground. 


Image Results
+++++++++++++++++++++++

EF image: Image stack containing EF values

Short-Mid image: Image stack containing the a/b ratios from iteratively fit ellipsoid 

Mid-Long image: Image stack contining the b/c ratios from iteratively fit ellipsoid 

Volume image: Image stack containing ellipsoid volumes 

Max id image: Image stack containing the ID of the largest ellipsoid at each point in the ROI. ID = 0 is the largest ellipsoid fit to the ROI. -1 is foreground while a large negative number corresponds to a negative background. 

Flinn diagram: Image plot of a/b versus b/c values in the ROI 

Weighted Flinn plot: Flinn diagram with peaks of intensity proportional to volume occupied by each (a/b, b/c) ratio





