#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:14:57 2022

@author: sriharsha.marupudi
"""

from skimage import measure
from skimage import filters
import trimesh 
import matplotlib.pyplot as plt
import numpy as np
import nrrd 
import pyvista as pv 
from glob import glob
import os 

voxelSize = (0.05, 0.05, 0.05) # mm
plattenThicknessVoxels = 10 # voxels
plattenThicknessMM = plattenThicknessVoxels * voxelSize[0] # mm
cubeShape = (202, 202, 202)





def cropCubeFromCenter(img,length):
    
    x0,y0,z0 = np.array(img.shape)//2
    R = length//2
    
    return img[slice(x0-R,x0+R+1),
               slice(y0-R,y0+R+1),
               slice(z0-R,z0+R+1)]

def filter_connected_volume(volume):
    # filter out components unconnected to the main bone structure
    # performs connected component analysis and preserves only the largest connected component
    
    labels = measure.label(volume,connectivity=1)
    values = np.unique(labels) # get all labels
    values.sort()
    values = values[1:] # discard zeros (background)
    num_voxels = [np.sum(labels==x) for x in values]
    largest_component_label = values[np.argmax(num_voxels)]
    
    vmin = np.min(volume)
    vmax = np.max(volume)
    
    volume_out = np.ones(volume.shape,dtype=volume.dtype) * vmin
    volume_out[labels==largest_component_label] = vmax
    
    return volume_out

def filter_connected_mesh(faces):
    # filter out components unconnected to the main bone structure
    pass

def addPlatten(volume, plattenThicknessVoxels, plattenValue=None, airValue=None, trimVoxels=0):
    # adds compression plates in Z
    # leaves a single-voxel space at the edge of volume (for isosurface)
    
    vmax = np.max(volume)
    vmin = np.min(volume)
    
    if plattenValue == None:
        plattenValue = vmax
        
    if airValue == None:
        airValue = vmin
    
    # Leaves single-voxel space at edge of volume for isosurface ops
    volume[:,:,0] = airValue
    volume[:,:,-1] = airValue
    
    # Define platten
    volume[(1+trimVoxels):(-1-trimVoxels),(1+trimVoxels):(-1-trimVoxels),1:plattenThicknessVoxels] = plattenValue
    volume[(1+trimVoxels):(-1-trimVoxels),(1+trimVoxels):(-1-trimVoxels),-plattenThicknessVoxels:-1] = plattenValue

    return volume

def set_volume_bounds(volume, airValue=None, bounds = 1):
    
    if airValue is None:
        airValue = np.min(volume)
        
    volume[0,:,:] = airValue
    volume[-1,:,:] = airValue
    volume[:,0,:] = airValue
    volume[:,-1,:] = airValue
    volume[:,:,0] = airValue
    volume[:,:,-1] = airValue
    
    return volume




def Voxel2SurfMesh(volume, voxelSize=(1,1,1), origin=None, level=None, step_size=1, allow_degenerate=False):
    # Convert voxel image to surface
    
    if level == None:
        level = (np.max(volume))/2
    
    # vertices, faces, normals, values = \
    #     measure.marching_cubes_lewiner(volume = volume, level = level, spacing = voxelSize, \
    #                                    step_size = step_size, allow_degenerate = allow_degenerate)
    vertices, faces, normals, values = \
        measure.marching_cubes(volume = volume, level = level, spacing = voxelSize, \
                               step_size = step_size, allow_degenerate = allow_degenerate)
            
    return vertices, faces, normals, values 

def saveSurfaceMesh(filename, vertices, faces):
    # Save surface mesh (tested on .STL only)
    mesh = trimesh.Trimesh(vertices=vertices.copy(), faces=faces.copy())
    mesh.export(filename)
    
def isWatertight(vertices, faces):
    # Check if mesh is watertight
    mesh = trimesh.Trimesh(vertices = vertices, faces = faces)
    return mesh.is_watertight

def smoothSurfMesh(vertices, faces, **trimeshkwargs):
    # smooths surface mesh using Mutable Diffusion Laplacian method
    
    mesh = trimesh.Trimesh(vertices = vertices, faces = faces)
    trimesh.smoothing.filter_mut_dif_laplacian(mesh, **trimeshkwargs)
    
    return mesh.vertices, mesh.faces

def simplifySurfMeshACVD(vertices, faces, target_fraction=0.25):
    # simplify surface mesh, use pyacvd
    import pyacvd
    
    Nfaces = faces.shape[0]
    target_count = round(Nfaces*target_fraction)
    
    mesh = trimesh.Trimesh(vertices = vertices, faces = faces)
    mesh = pv.wrap(mesh)
    
    clus = pyacvd.Clustering(mesh)
    clus.cluster(target_count)
    
    mesh = clus.create_mesh()
    
    # https://github.com/pyvista/pyvista/discussions/2268
    faces_as_array = mesh.faces.reshape((mesh.n_faces, 4))[:, 1:]
    tmesh = trimesh.Trimesh(vertices = mesh.points, faces = faces_as_array)
    
    return tmesh.vertices, tmesh.faces

def repairSurfMesh(vertices, faces):
    import pymeshfix
    vclean, fclean = pymeshfix.clean_from_arrays(vertices, faces)
    return vclean, fclean
    




ROIDir = "/gpfs_projects/sriharsha.marupudi/Segmentations_Otsu/"
files = glob(ROIDir+"*.nrrd")

for txt in files:
    NAME = os.path.basename(txt).replace("Segmentation-grayscale","").replace(".nrrd","")
    print(f"Previewing ROI{NAME}.")
    
    
    img,header = nrrd.read(f"/gpfs_projects/sriharsha.marupudi/Segmentations_Otsu/Segmentation-grayscale{NAME}.nrrd")
    volume = cropCubeFromCenter(img,cubeShape[0]) #Crop ROI to 200
    volume = addPlatten(volume, plattenThicknessVoxels) #Add platten to top and bottom 
    volume = set_volume_bounds(volume, airValue=None,bounds=2)
    volume = filter_connected_volume(volume) #Filter continous connected volumes of bone 
    vertices, faces, normals, values = Voxel2SurfMesh(volume, voxelSize=(0.05,0.05,0.05), step_size=1)
    vertices,faces = smoothSurfMesh(vertices,faces,iterations=15)
    vertices,faces = simplifySurfMeshACVD(vertices, faces, target_fraction = 0.15)
    
    
    filenameNRRD = volume
    filenameSTL = f"/gpfs_projects/sriharsha.marupudi/Bone_STL/ROI{NAME}.stl"
    #filenameVTK = "../../data/output/isodata_04216_roi_4.vtk"
    
    
    saveSurfaceMesh(filenameSTL, vertices, faces)
    print("Is watertight? " + str(isWatertight(vertices, faces)))
    
    if not isWatertight(vertices, faces):
                  vertices, faces = repairSurfMesh(vertices, faces)    
                  print("Surface Mesh Repaired")
                  print("Is watertight? " + str(isWatertight(vertices, faces)))
                  saveSurfaceMesh(filenameSTL, vertices, faces)

                
                
                
                
                
               
                
                
