
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Team Project (edge blur/smoothing)
	Author(s):      Steve Chen, chen3626@purdue.edu
                    Eric Mesina, emesina@purdue.edu
                    Danny Mcnulty, mcnulty1@purdue.edu
                    Kyle Nematz, knematz@purdue.edu
	Team ID:        LC4-09
	

===============================================================================
'''

import numpy as np

''' function that will smooth image'''
def blur(image):
    '''create empty numpy array with same shape as the image we are processing'''
    result = np.empty(image.shape)
    
    '''create the matrix that we will use to weight each value in a 5x5 window'''
    gauss_matrix = np.array([[1,   4,   6,   4,  1],
                             [4,  16,  24,  16,  4],
                             [6,  24,  36,  24,  6],
                             [4,  16,  24,  16,  4],
                             [1,   4,   6,   4,  1]])
    '''iterate through the array with 5x5 window and perform thw gaussian smoothing average'''
    for i in range(3, len(image[0]) - 3):
        for j in range(3, len(image) - 3):
            result[j][i] = np.average(image[j-2:j+3, i-2:i+3], weights=gauss_matrix, axis=(0, 1))
            
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
