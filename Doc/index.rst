Welcome to BoneJ Headless documentation!
=====================================

The following is a documentation of how to use the BoneJ modules and scripts that have been developed for the Quantitative Bone Texture Project. The BoneJ Module scrips were written in Python with Fiji scripts being written with Jython. To run these scripts there needs to be a working installation of Fiji with BoneJ installed, additionally files must be 3D 8-bit binary files. All functions utilize a macro file that is included with the modules written in Jython that is run within Fiji. 
The scripts rely on invoking Fiji from the system’s command line. Fiji is called in headless mode, thus no GUI will appear. The macro files with Fiji scripts written in Jython are run to return the final results. 

**Citations:**
*Domander R, Felder AA, Doube M. 2021 BoneJ2 - refactoring established research software. Wellcome Open Res. 6. doi:10.12688/wellcomeopenres.16619.1
Doube M, Kłosowski MM, Arganda-Carreras I, Cordeliéres F, Dougherty RP, Jackson J, Schmid B, Hutchinson JR, Shefelbine SJ. BoneJ: free and extensible bone image analysis in ImageJ. Bone 47 1076-1079 (2010). doi: 10.1016/j.bone.2010.08.023

Dougherty R, Kunzelmann K (2007), Computing local thickness of 3D structures with ImageJ, Microsc. Microanal., 13: 1678-1679, <doi:10.1017/S1431927607074430>

Hildebrand T, Rüegsegger P (1997), A new method for the model-independent assessment of thickness in three-dimensional images, J. Microsc., 185: 67-75, <doi:10.1046/j.1365-2818.1997.1340694.x>

Odgaard A (1997), Three-dimensional methods for quantification of cancellous bone architecture, Bone, 20, 315-328, <doi:10.1016/S8756-3282(97)00007-0>

Harrigan TP, Mann RW (1984), Characterization of microstructural anisotropy in orthotropic materials using a second rank tensor, J Mater Sci, 19, 761-767, <doi:10.1007/BF00540446>

Odgaard A, Gundersen HJG (1993), Quantification of connectivity in cancellous bone, with special emphasis on 3-D reconstructions, Bone 14: 173-182, <doi:10.1016/8756-3282(93)90245-6>.

Toriwaki J, Yonekura T (2002), Euler number and connectivity indexes of a three dimensional digital picture, Forma 17: 183-209
Rasband, W.S., ImageJ, U. S. National Institutes of Health, Bethesda, Maryland, USA, https://imagej.nih.gov/ij/, 1997-2018.
BoneJ2 

ImageJ 1.53q *



Table of Contents
-----------------

.. toctree::
   :hidden:

   Home <self>

.. toctree::
   :maxdepth: 2

   installation
   usage
   plugins
   contributing
   developers
   FAQs <faq>
   changes

Plugins
---------------

Currently supports the following pluins:

* Trabecular Thickness 
* Trabecular Spacing 
* Anisotropy
* Area Volume Fraction
* Connectivity


Detailed description on individual plugins is provided in section :ref:`plugins`.

Installation
------------

Fiji can be installed with the following link:

*  ``https://imagej.net/software/fiji/downloads``

For more detailed installation instructions for BoneJ,
see https://imagej.net/plugins/bonej.








