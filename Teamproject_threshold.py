
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Team Project (threshold)
	Author(s):      Steve Chen, chen3626@purdue.edu
                    Eric Mesina, emesina@purdue.edu
                    Danny Mcnulty, mcnulty1@purdue.edu
                    Kyle Nematz, knematz@purdue.edu
	Team ID:        LC4-09
	

===============================================================================
'''
import numpy as np

'''function to threshold the inputted png array'''
def Threshold(image):
    '''create empty array with same shape as inputted array'''
    result = np.empty(image.shape)
    '''find average value of the array in order to figure out value to determine if an array value should be transformed to white or black'''
    average = np.average(image)
    '''loop that iterates through each value in array to perform thresholding'''
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] >= average:
                result[i][j] += 0
            else:
                result[i][j] += 255
    return result
    
    
    
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
