"""Taking PNG input"""
#make sure all the py files are in the same folder or destination in your computer

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
'''function that asks,takes,converts user inputted PNG image'''

def PNG_Input():
    print('Enter the destination of the PNG:')
    png_destination = input()    
    img = mpimg.imread(png_destination)
    
    return img







