# BoneJ-Headless-Mode-Python-Scripts
Scripts for running BoneJ plugins in headless mode. 
Scripts ending in .API are Fiji scripts written in Jython that use Java APIs, Python, and macro scripting. 
Scripts labeled BoneJ_Demo_Script are Python wrappers to run Jython scripts through invoking commandline to run Fiji in headless mode. 
Scripts are intended to be run with 8 bit 3D nrrd images in Python. 
Certain plugins require ImgPlus files while others require ImagePlus. This repository uses nrrd files which are always loaded as ImagePlus first and then converted into ImgPlus if required. 
Segmentation code for the ROIs are included as well 
