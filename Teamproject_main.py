
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Team Project (main)
	Author(s):      Steve Chen, chen3626@purdue.edu
                    Eric Mesina, emesina@purdue.edu
                    Danny Mcnulty, mcnulty1@purdue.edu
                    Kyle Nematz, knematz@purdue.edu
	Team ID:        LC4-09
	

===============================================================================
'''
'''import all modules and files'''
import Teamproject_PNG_input as png
import Teamproject_grayscale as gray
import Teamproject_edgeblurnoise as noise
import Teamproject_edgehighpassfiltering as edge
import Teamproject_threshold as threshold

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

'''Acquire PNG input from user'''
image_matrix = png.PNG_Input()

'''convert to grayscale'''
gray_image = gray.Grayscale(image_matrix)

'''Edge blur/noise smoothing'''
blur_image = noise.blur(gray_image)

'''Edge Enhancement'''
sobel_all = edge.sobel_all(blur_image)

'''Thresholding'''
thresh_image = threshold.Threshold(sobel_all)


'''plotting all the images'''
f, axarr = plt.subplots(2,3)
axarr[0,0].imshow(image_matrix)
axarr[0,1].imshow(gray_image, cmap='gray')
axarr[0,2].imshow(blur_image, cmap='gray')
axarr[1,0].imshow(sobel_all, cmap='gray')
axarr[1,1].imshow(thresh_image, cmap='gray')

'''save images as PNG'''
plt.imsave('original.png', image_matrix)
plt.imsave('grayscale_image.png', gray_image, cmap = 'gray')
plt.imsave('smooth_image.png', blur_image, cmap = 'gray')
plt.imsave('edge_enhanced_image.png', sobel_all, cmap = 'gray')
plt.imsave('threshold_image.png', thresh_image, cmap = 'gray')

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''






