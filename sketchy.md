
# Sketchy tree sytling on QGIS

This article focuses on the symbology of a point layer. The goal is to make the tree point layer look like it has been sketched. This is done using Geometry Generator, SVGs and wave_randomised or triangular_wave_randomised. Only QGIS 3.28.0 or other recent versions can be used for these styles.

Topics Covered:
- Symbol Layers
- Expressions
- Embedded SVGs
- Gradients
- Draw Effects
- Geometry generators

```
**Output:**

```
![App Screenshot](images/sketchy_tree.png)

**Steps:**

1. Create a point layer with a ‘crown_radius_m’ column in QGIS, using EPSG: 4326. 
New Geopackage &rarr; Create a new database or select an existing one &rarr; select Point for Geometry Type &rarr; specify EPSG &rarr; Add new field ‘crown_radius_m’ &rarr; OK. 


![App Screenshot](images/image15.png)

2. Add a few random points and populate the columns.  

![App Screenshot](images/radom_point.png)

3. Under ‘Layer Styling’, select Single Symbol.
Click on ‘Simple Marker’ and Select ‘Geometry Generator’ for ‘Symbol layer type’ and ‘Polygon/MultiPolygon’ for ‘Geometry type’.

![App Screenshot](images/simple_marker.png)

4. To create a buffer that depends on the crown radius value, input the following in the expression:
buffer($geometry, “crown_radius_m”) 🡪 Quotation marks (“”) must be used to refer to columns.

![App Screenshot](images/buffer.png)

Buffer Tool explained:

![App Screenshot](images/buffer_explained.png)

Parameters with square brackets are optional parameters.
However, the user must input geometry and distance for the buffer (in this case, it is given by the crown radius value so the distance for the buffer differs per feature). If you are going to input values for segments, cap, join and miter_limit, you can just input values while emitting the titles but they must then be in the same order as shown in the documentation. However, if the order is not applied rigidly or only some parameters need to be changed, provide the names of the parameters, for example:
buffer($geometry, “crown_radius_m”, cap:=’square’)


Output:

![App Screenshot](images/buffer_output.png)

The output of changing the segments (Note the syntax: ‘segments:=1’):

Segments = 1 

![App Screenshot](images/segments_1.png)

Segments = 2 

![App Screenshot](images/segments_2.png)

Segments:= 8

![App Screenshot](images/segment_8.png)

Therefore, increasting the segments increases the smoothness of the buffer.  

5. Creating the wave effect around the points

Method 1: Using triangular_wave_randomized
Experimenting with the parameters of the tool.

![App Screenshot](images/image1.png)

For the geometry parameter, we input the buffer function since the triangulated waves are created on the buffer created on a point:

triangular_wave_randomized( buffer($geometry, "crown_radius_m"), 1,1,1,1,1)

Inputting the value 1 for all the compulsory parameters is expected to create triangles around the buffer of equal shape and length (besides the starting and ending point) because that means only wavelength of 1 (since the randomly generated number is between minimum of 1 and maximum of 1, which is 1, and amplitude of 1 is selected. Therefore, this is like using triangulated_wave(buffer($geometry, “crown_radius_m”), 1, 1) instead, since this does not create the triangulated waves based on selecting a value at random from an interval.

Output:

![App Screenshot](images/image29.png)

Increasing the range between the minimum and maximum wavelengths increases the chances of having wider angles between your triangles then increasing the range of amplitudes increases how deeply the triangles can penetrate into the buffer:

 Wavelength of 5           |  Amplitude of 5
:-------------------------:|:-------------------------:
![App Screenshot](images/image9.png)  | ![App Screenshot](images/image18.png)

After trying out different values for wavelengths and amplitude, the following implementation is done:
 triangular_wave_randomized( buffer($geometry, "crown_radius_m"), 2, 5, 0.1, 0.5)

Output:

![App Screenshot](images/out_put_smoth.png)

For the final touch, the ‘smooth’ tool will be used. The triangular ends of the polygon are too defined and not irregular enough to suit the ‘sketchy’ design that is intended. The iterations will be based on the id of the tree features.

![App Screenshot](images/function%20smooth.png)

smooth (triangular_wave_randomized( buffer($geometry, "crown_radius_m"),2, 5,0.1, 0.15,20), @id)

![App Screenshot](images/t_wave_ran.png)

Method 2: Using wave_randomized.

1. We can then apply the wave randomised function to the buffer. It takes in the 6 arguments that are outlined in the image below. We start with all arguments excluding the geometry equal to 1 (initial conditions) and investigate the effect of each argument on the output by keeping all others at 1.

![App Screenshot](images/image25.png)

Initial output:

![App Screenshot](images/image16.png)

First, we look at the minimum wavelength of waves which ranges from 0 to 1. The lowest minimum wavelength yields more “petals” to our flower looking shape. This is because the wavelengths are shortened due to a lower possible minimum. This then fits more waves as the minimum wavelength number approaches zero.

Min=0.1 

![App Screenshot](images/min1.png)

Min=0.5 

![App Screenshot](images/image7.png)

Now, we look at the maximum wavelength of waves which ranges from the minimum wavelength to positive infinity.
Larger maximum wavelengths create more irregular looking shapes due to the greater variation in the wavelengths and thus shapes of the waves created around the buffer boundary of the point. This does not quite apply to the two below where min. wavelength = max. wavelength.

Min = 0.1, Max = 0.1 

![App Screenshot](images/min_max_1.png)

Min = 0.5, Max = 0.5 

![App Screenshot](images/min_max_5.png)

Min = 0.1, Max = 4

![App Screenshot](images/min_max_4.png)

Min = 0.1, Max = 8

![App Screenshot](images/min_max_8.png)

Now, we investigate the minimum and maximum amplitudes of the random waves created.  

With minimum and maximum wavelengths kept at 1,  
Minimum amplitude = 0.1, Maximum amplitude = 1:

![App Screenshot](images/min_max_amp_1.png)

We immediately observe that the wave amplitude affects the distance that the “petals” on the circumference can approach the centre of the point (the centroid). 

Minimum amplitude = 0.1, Maximum amplitude = 0.3:

![App Screenshot](images/min_max_amp_3.png)

And now with the smaller minimum and maximum amplitudes, we get closer to the desired sketchy shape.  

1. We can now duplicate the Marker 
![App Screenshot](images/image8.png)

1. Make the first Marker’s Geometry Generator fill colour Transparent.
![App Screenshot](images/image14.png)

Then click on the green plus sign to Add Symbol Layer. Once added, change the Symbol Layer Type to ‘Outline: Simple Line’ and match the Stroke Widths. Playing around with the stroke widths yields different sketchy outputs.

![App Screenshot](images/add_symbol.png)

You can also continue to duplicate the Geometry Generator layers with different seed values to create more sketch lines.

![App Screenshot](images/dup.png)

8. Once the outlines look sketchy, we can change the Symbol Layer Type to Gradient Fill.
This shows a simple Gradient Fill from the top to the bottom of the symbol.

![App Screenshot](images/symbol_layer_type.png)

The reference point 1 tells us where the light of the gradient should originate. The box below shows the top-left represents (x,y) = (0,0) and the bottom-right is (1,1). As such your gradient direction is determined by the (x,y) values in the first and second reference points.

![App Screenshot](images/xy.png)

Creating the centroid marker.

![App Screenshot](images/centroid_marker.png)

This can be done on Inkscape. Once you have created your own svg in Inkscape, save it.  You can then use your Marker in QGIS under ‘Symbology’ of the third layer of your style, select ‘SVG marker’ and then choose the marker you created in Inkscape This embeds the svg on top of the tree layer.

![App Screenshot](images/image_17.png)

Adding Leafy Texture.

![App Screenshot](images/image_21.png)

NB: Trees have leaves, so they must be given a leafy texture

![App Screenshot](images/image_19.png)

Finally the sketchy trees will have a leafy texture with small ‘svg’ markers on top:

![App Screenshot](images/image_18.png)

10. Radius Feature 
Now we will add the line going from the centre of the point to the circumference of the feature.
1. Duplicate a feature layer and move to the top then change the Geometry Type to ‘LineString/MultiString’.

![App Screenshot](images/image_lend.png)
2. To generate the squiggly line, we will use two new functions: ‘with_variable’ and ‘make_line’.

![App Screenshot](images/function_make_line.png)

In the expression field, input:
 with_variable('poly',buffer($geometry, "crown_radius_m"), 		 smooth(triangular_wave_randomized( make_line( centroid(@poly), start_point(@poly)), 2, 5, 0.1, 0.15, 20), 10)).

 3. Duplicate the layer created in step 2, and input: 
with_variable('poly',buffer($geometry, "crown_radius_m"), smooth(triangular_wave_randomized( make_line( centroid(@poly), start_point(@poly)),  2, 4, 0.1, 0.15, 20), 10))

4. Now that you have sketched a squiggly line from radius to circumference, we need to add an arrow on each end. This is done by duplicating the layer from Steps 2 or 3 and changing the Symbol Layer Type to ‘Marker Line’.  Under the Marker Line Properties, make sure ‘On First vertex’ is ticked and untick ‘Rotate marker’ to follow line direction. Change the size to 6 millimetres.

On the ‘Simple Marker’ layer, scroll to the bottom and select the icon below. Additionally, change the rotation property to 180 degrees,

5. Duplicate the layer created in step 4 but change the selection from ‘On First vertex’ to ‘On last vertex’ and keep the rotation on 0 degrees 

![App Screenshot](images/dup_layer.png)

Label feature
Now that we have a squiggly line with two arrows and a sketchy tree designed, the only thing missing is the label. Similar to the rest of the design, we also want this to look hand-written.

1. Right click on layer > Properties > Label > Single Labels > Set Value to ‘concat(“crown_radius_m”, ‘ m’). This is to show the unit for the radius without having to input ‘m’ in the data record because we need this layer to remain in decimal data type. Therefore, concat combines the numeric value of the radius and adds the suffix ‘m’ to it.

![App Screenshot](images/func_concat.png)

2. Select Bradley Hand ITC for font.
3. Go to Placement &rarr; Change Mode to ‘Offset from Point’ and select the central position.

After all the steps, you should have a symbology that looks hand-sketched, showing a hand-sketched top-view of a tree, a hand-sketched arrow from the centre to circumference and handwritten crown measurement with a unit.