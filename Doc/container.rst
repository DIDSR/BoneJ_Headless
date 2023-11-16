Container Instructions
======================

Using the provided container for BoneJ Headless creates an environment with all of the program requirements.

Creating a Container
--------------------

Running BoneJ Headless in a container requires an Apptainer installation. See the `Apptainer documentation <https://apptainer.org/docs/user/latest/quick_start.html>`_ for installation instructions.

With apptainer installed, the container can be created from the provided definition file (container.def) using the following command:

`` apptainer build container.sif container.def ``

Using a Container
-----------------
 
Once a container has been built, an example can be run using the command:

`` apptainer run --app example container.sif ``