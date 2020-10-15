"""Edge enhancement-high pass filtering"""

import numpy as np

def sobel_x(image):
    result = np.empty(image.shape)
    
    kernel = np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]])
    
    for j in range(1, len(image) - 1):
        for i in range(1, len(image[0]) - 1):
            result[j][i] = np.sum(image[j-1:j+2, i-1:i+2] * kernel)
            
    return result
    
def sobel_y(image):
    result = np.empty(image.shape)
    
    kernel = np.array([[-1, -2, -1],
                       [ 0,  0,  0],
                       [ 1,  2,  1]])
    
    for j in range(1, len(image) - 1):
        for i in range(1, len(image[0]) - 1):
            result[j][i] = np.sum(image[j-1:j+2, i-1:i+2] * kernel)
            
    return result

def sobel_all(image):
    x = sobel_x(image)
    y = sobel_y(image)
    
    return np.sqrt(np.power(x, 2) + np.power(y, 2))