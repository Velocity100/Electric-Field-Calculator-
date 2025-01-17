# Electric Field Calculator
Uses Coloumb's law to calculate the electric field components and magnitude for arbitrary charge contributions and user-defined coordinates, for both 2D and 3D, for electrostatic systems. Any version of numpy is needed.

# Usage
The ElibV3.py file is the main Python file with the 3D and 2D functions. 

The x, y, (and z) positions of the charges must be inputted as lists or arrays, and then the corresponding charges must also be a list or array. 

A coordinate point (x,y) or (x,y,z) is then defined to evaluate the electric field components and magnitude. For singular points, no list/array is necessary and can just be inputted as an int or float, but multiple points must be inputted as lists or arrays, separate for each dimension. 

See the Examples_3D and Examples_2D folders for further details. 

For example, looking at the Concentric_SpheresV2 file, we can simulate concentric spheres of opposite charge and radii with a ratio of 1:2. Using the Plotly library (Plotly not required), the electric vector field and electric field magnitude along the x-axis are plotted:


![newplot (2)](https://github.com/user-attachments/assets/673b9ec3-d4d5-4196-8cac-2fa778cf08b7)
![newplot (3)](https://github.com/user-attachments/assets/e0dbb71c-c8cf-4807-84ae-86979ffebe53)

The plots give the general shape and direction of the electric field expected for such a charge configuration.
