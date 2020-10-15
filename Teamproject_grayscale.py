"""Grayscale Function"""
'''.2126R+.7152G+.0722B'''

import numpy as np


def Grayscale(x):   
    return np.dot(x[...,:3], [.2126, .7152, .0722])

