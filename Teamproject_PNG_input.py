
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Team Project (PNG input/error)
	Author(s):      Steve Chen, chen3626@purdue.edu
                    Eric Mesina, emesina@purdue.edu
                    Danny Mcnulty, mcnulty1@purdue.edu
                    Kyle Nematz, knematz@purdue.edu
	Team ID:        LC4-09
	

===============================================================================
'''
#make sure all the py files are in the same folder or destination in your computer

'''import relevant modules'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys


'''function that asks,takes,converts user inputted PNG image'''
def PNG_Input():
    '''take user input for file name'''
    print('Enter the destination of the PNG:')
    png_destination = input()    
   
    '''perform error handling(allows one screw up)'''
    while True:
        try:
            img = mpimg.imread(png_destination)
            break
        except FileNotFoundError:
            try:
                img = mpimg.imread(input('Please re-enter the destination of PNG:'))
                break
            except FileNotFoundError:
                sys.exit('No file found')
    
    print('Patience you must have, my young padawan. \n -Yoda')
    return img





'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''




