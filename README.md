# 3D printing system on non-planar surfaces using a robotic arm

<p>The Fused Deposition Modeling is a technique within Additive Manufacturing, in which a part is formed by stacking two-dimensional layers, using a technique known as 2.5 axis, with which there are certain defects such as the staircase effect, the decrease of resistance in the printing direction, the use of supports and limitations such as printing on flat surfaces. In order to reduce these limitations and defects, the design of a 3D printing system on non-planar surfaces using the Dobot Magician robotic arm, to which a 3D printing system is adapted and its degrees of freedom are increased. Additionally, the kinematics calculation is performed through the Denavit-Harterg parameters, and a 3D printing <a href="https://github.com/compas-dev/compas_slicer">slicer</a> for multi-axis machines is selected and configured. Finally, a comparison is made between the parts printed by non-planar printing and traditional printing, obtaining a decrease of the staircase effect and an error of 6.125% in the width of the compared part.</p> 

<div align=center>

<img src="images/3DPrintingSystem.jpeg" width="500" height="350" />

</div>

## Workflow for 3D printing on non-planar surfaces

<p>In the workflow for flat surface printing, there are 5 fundamental processes: CAD, lamination, post-processing, calculation of inverse kinematics and 3D printing. In this sense, initially the digital model of the part or surface to be printed is made, using CAD software such as Solidworks, Blender or other, where the file is saved in STL format. Subsequently, the part is laminated in a traditional 3D printing software, such as Ultimaker Cura, from which a g-code is obtained, with the positions, speeds and extrusion material. After that, the post-processing is performed, in which the coordinates of the g-code must be abstracted and a set of operations must be performed in order to finally calculate the angles of the joints and send them to the robot to perform the 3D printing.</p>

<div align=center>

<img src="images/Worflow_3DPrinting_base.png"/>

</div>

<p>In the workflow for non-planar printing on surfaces, initially the digital model of the surface and the part to be laminated is made, which must be generated as surfaces and the lower part of the part to be laminated must have the cut of the surface on which it will be printed. Then, the lamination process is performed using the script provided in the Compas Slicer Github from which a JSON file is obtained with the vectors and printing points. Subsequently, post-processing is performed in which the information is abstracted from the file and a set of operations are performed. Finally, the angles of each joint are loaded into the robot for 3D printing.</p>

<div align=center>

<img src="images/Worflow_3DPrinting_geom.png"/>

</div>
