
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Team Project (Edge filtering)
	Author(s):      Steve Chen, chen3626@purdue.edu
                    Eric Mesina, emesina@purdue.edu
                    Danny Mcnulty, mcnulty1@purdue.edu
                    Kyle Nematz, knematz@purdue.edu
	Team ID:        LC4-09
	

===============================================================================
'''


import numpy as np

'''perform x direction sobel'''
def sobel_x(image):
    result = np.empty(image.shape)
    '''compute window operation with given kernel'''
    kernel = np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]])
    '''iterates through the array with a window and performs kernel operation'''
    for j in range(1, len(image) - 1):
        for i in range(1, len(image[0]) - 1):
            result[j][i] = np.sum(image[j-1:j+2, i-1:i+2] * kernel)
            
    return result

'''perform y direction sobel'''
def sobel_y(image):
    result = np.empty(image.shape)
    '''compute window operation with given kernal'''
    kernel = np.array([[-1, -2, -1],
                       [ 0,  0,  0],
                       [ 1,  2,  1]])
    '''iterates through array with a window and performs kernel operation'''
    for j in range(1, len(image) - 1):
        for i in range(1, len(image[0]) - 1):
            result[j][i] = np.sum(image[j-1:j+2, i-1:i+2] * kernel)
            
    return result

'''perform both sobel operations with inputted array'''
def sobel_all(image):
    x = sobel_x(image)
    y = sobel_y(image)
    
    return np.sqrt(np.power(x, 2) + np.power(y, 2))


'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
