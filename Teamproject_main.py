"""Main"""
#C:\Users\skcst\Desktop\Python_Team\PNG\Purdue_Arch.png
import Teamproject_PNG_input as png
import Teamproject_grayscale as gray

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Acquire PNG input from user
image_matrix = png.PNG_Input()
'''
image_matrix is a matrix of the pixels from png
check to see if code works by clicking on 'plots' in spyder ide
image_matrix[a][b]
a ----> specific matrix from array
b ----> specific line from array
'''

'''convert to grayscale'''
gray_image = gray.Grayscale(image_matrix)










'''plotting all the images'''
f, axarr = plt.subplots(2,2)
axarr[0,0].imshow(image_matrix)
axarr[0,1].imshow(gray_image)
#axarr[1,0].imshow()
#axarr[1,1].imshow()
