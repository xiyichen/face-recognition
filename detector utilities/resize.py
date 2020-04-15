import pandas as pd
from PIL import Image
import PIL
from shutil import copy
import numpy as np

sizes = []

df = pd.read_csv('./file_list.csv')
for path in df['FILENAME']:
	img = Image.open(path)
	t = 4
	x, y = img.size
	img = img.resize((t*x, t*y), resample=PIL.Image.BILINEAR)
	arr = path.split('/')
	newname = arr[-2] + '-' + arr[-1]
	img.save('./queries/' + newname)
