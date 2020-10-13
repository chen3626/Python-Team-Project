"""Edge blurring/noise smoothing on image function"""

import numpy as np

def blur(image):
    result = np.empty(image.shape)
    
    gauss_matrix = np.array([[1,   4,   6,   4,  1],
                             [4,  16,  24,  16,  4],
                             [6,  24,  36,  24,  6],
                             [4,  16,  24,  16,  4],
                             [1,   4,   6,   4,  1]])
    
    for i in range(3, len(image[0]) - 3):
        for j in range(3, len(image) - 3):
            result[j][i] = np.average(image[j-2:j+3, i-2:i+3], weights=gauss_matrix, axis=(0, 1))
            
    return result
