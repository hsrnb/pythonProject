import os,random
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image
# %matplotlib inline

def read_random_image():
    folder=r""#地址
    file_path = folder + random.choice(os.listdir(folder))
    pil_im = Image.open(file_path,'r')
    return pil_im