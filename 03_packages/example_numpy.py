import numpy
# Access pi variable from the NumPy module
numpy.pi

# Access pi variable from the NumPy module with alias
import numpy as np
np.pi

# Access pi variable from the NumPy with bad practice
from numpy import *
# Just don´t

import matplotlib.pyplot as plt
#          ^        ^        ^ 
#          |        |        |
#       Package     |        |
#                 Module     |
#                        Function




