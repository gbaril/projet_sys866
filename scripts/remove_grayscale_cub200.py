from PIL import Image
import os
from config import DATA_PATH
import cv2

def is_grey_scale(img_path):
    img = Image.open(img_path).convert('RGB')
    w,h = img.size
    for i in range(w):
        for j in range(h):
            r,g,b = img.getpixel((i,j))
            if r != g != b: return False
    return True

for i in ['images_evaluation', 'images_background']:
    for filename in os.listdir(DATA_PATH + '/CUB200/' + i):
        file_path = DATA_PATH + '/CUB200/' + i + '/' + filename
        for imagename in os.listdir(file_path):
            img_path = file_path + '/' + imagename
            if is_grey_scale(img_path):
                print(img_path)
                os.remove(img_path) 