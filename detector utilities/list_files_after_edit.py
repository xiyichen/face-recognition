import os
import fnmatch



def recglob(directory,ext):
    l = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, ext):
            l.append(os.path.join(root, filename))
    return l


lst = recglob('C:\\Users\\xiyi\\Documents\\query_imgs_550_cfpw_low_res\\40x40_x2_bicubic', '*.jpg')

with open('file_list_after_edit.csv', 'w') as fout:
	fout.write('FILENAME\n')
	for filename in lst:
		s = filename.split('\\')[-2:]
		fout.write('/'.join(s)+'\n')