import pandas as pd
from PIL import Image
from shutil import copy

sizes = []

df = pd.read_csv('./file_list.csv')
for i in df['FILENAME']:
	img = Image.open('./'+i)
	sizes.append((img.size[0], i))
sizes.sort()
dst = './files/'
for i in range(100):
	path = sizes[i][1]
	src = './' + path
	arr = path.split('/')
	newname = arr[2] + '-' + arr[-1]
	copy(src, dst + newname)