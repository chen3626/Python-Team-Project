"""Edge blurring/noise smoothing on image function"""

def blur(image):
    result = image.copy()
    
    for i in range(1, len(image[0]) - 1):
        for j in range(1, len(image) - 1):
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x != 0 and y != 0:
                        result[j][i] += image[j + y][i + x]
            
            result[j][i] /= 9
            
    return result
