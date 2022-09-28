from PIL import Image 
import numpy as np

# open cleffa.png
cleffa = Image.open(r"cleffa.png")

# show cleffa
#cleffa.show()

print(cleffa.format)
# PNG

print(cleffa.size)
# (28, 29)

print(cleffa.mode)
# RGB

print(type(cleffa))
# <class 'PIL.PngImagePlugin.PngImageFile'>

# convert cleffa to grayscale
cleffa_grayscale = cleffa.convert("L") # L stands for grayscale

print(cleffa_grayscale.mode)
# L

# show cleffa_grayscale
#cleffa_grayscale.show()

# save cleffa_grayscale
cleffa_grayscale.save("cleffa_grayscale.png")

# convert cleffa_grayscale to numpy array
cleffa_grayscale_array = np.asarray(cleffa_grayscale)

print(np.shape(cleffa_grayscale_array))
# (29, 28)

# convert cleffa to numpy array
cleffa_array = np.asarray(cleffa)

print(np.shape(cleffa_array))
# (29, 28, 3)