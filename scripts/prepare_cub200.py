from tqdm import tqdm as tqdm
import numpy as np
import shutil
import os

from config import DATA_PATH
from few_shot.utils import mkdir, rmdir


# Clean up folders
rmdir(DATA_PATH + '/CUB200/images_background')
rmdir(DATA_PATH + '/CUB200/images_evaluation')
mkdir(DATA_PATH + '/CUB200/images_background')
mkdir(DATA_PATH + '/CUB200/images_evaluation')

# Find class identities
classes = os.listdir(DATA_PATH + '/CUB200/images/')

# Train/test split
np.random.seed(0)
np.random.shuffle(classes)
background_classes, evaluation_classes = classes[:80], classes[80:]

# Move images to correct location
for classname in os.listdir(DATA_PATH + '/CUB200/images/'):
    subset_folder = 'images_evaluation' if classname in evaluation_classes else 'images_background'
    src = DATA_PATH + f'/CUB200/images/{classname}'
    dst = DATA_PATH + f'/CUB200/{subset_folder}/{classname}'
    shutil.copytree(src, dst)
