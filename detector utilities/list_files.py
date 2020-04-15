import os
import fnmatch



def recglob(directory,ext):
    l = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, ext):
            l.append(os.path.join(root, filename))
    return l

os.mkdir('./templates')
lst = recglob('C:\\Users\\xiyi\\Documents\\query_imgs_550_cfpw_low_res\\query_imgs_550_cfpw_40x40', '*.jpg')

with open('file_list.csv', 'w') as fout:
	fout.write('FILENAME\n')
	for filename in lst:
		s = filename.split('\\')
		fout.write('/'.join(s)+'\n')