# Test of linear motion blurring with different settings

Based on Pyblur, a Python image blurring routines. Details can be found [here](https://github.com/lospooky/pyblur)
install_requires: 'numpy', 'pillow', 'scikit-image', 'scipy'. 

### Linear Motion Blur
Blurs image using a Line Kernel

	blurred = LinearMotionBlur(img, dim, angle, linetype)

#### Parameters
* `dim` Kernel Size: {3,5,7,9} with any angle, other integers with 0 angle. <br>
* `angle` Angle of the line of motion. \[0,180). Will be floored to the closest one available for the given kernel size. <br>
* `linetype = {left, right, full}` Controls whether half the blur kernel. <br>

Randomized kernel size, angle, and line type

	blurred = LinearMotionBlur_random(img)
