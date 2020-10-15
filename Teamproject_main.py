"""Main"""
#C:\Users\skcst\Desktop\Python_Team\PNG\Purdue_Arch.png
import Teamproject_PNG_input as png
import Teamproject_grayscale as gray
import Teamproject_edgeblurnoise as blur
import Teamproject_edgehighpassfiltering as edge

import matplotlib.pyplot as plt

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

blur_image = blur.blur(gray_image)

sobel_all = edge.sobel_all(blur_image)


#print(image_matrix)
#print(gray_image)



'''plotting all the images'''
f, axarr = plt.subplots(2,2)
axarr[0,0].imshow(image_matrix)
axarr[0,1].imshow(blur_image, cmap="gray")
axarr[1,0].imshow(sobel_all, cmap="gray")
#axarr[1,1].imshow(sobel_y_image, cmap="gray")