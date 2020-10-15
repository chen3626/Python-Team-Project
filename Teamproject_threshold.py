"""Threshold function"""
import numpy as np

def Threshold(image):
    result = np.empty(image.shape)
    average = np.average(image)
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] >= average:
                result[i][j] += 0
            else:
                result[i][j] += 255
    return result
    
    
    
