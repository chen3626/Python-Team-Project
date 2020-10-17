
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Team Project (grayscale)
	Author(s):      Steve Chen, chen3626@purdue.edu
                    Eric Mesina, emesina@purdue.edu
                    Danny Mcnulty, mcnulty1@purdue.edu
                    Kyle Nematz, knematz@purdue.edu
	Team ID:        LC4-09
	

===============================================================================
'''
'''.2126R+.7152G+.0722B'''

import numpy as np

'''takes input for numpy array and converts to grayscale copy'''
def Grayscale(x):    
    return np.dot(x[...,:3], [.2126, .7152, .0722])

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
