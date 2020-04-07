import os
import fnmatch



def recglob(directory,ext):
    l = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, ext):
            l.append(os.path.join(root, filename))
    return l


lst = recglob('C:\\Users\\xiyi\\Documents\\cfp-dataset', '*.jpg')

with open('file_list.csv', 'w') as fout:
	fout.write('FILENAME\n')
	for filename in lst:
		s = filename.split('\\')[5:]
		if s[-2] == 'frontal':
			fout.write('/'.join(s)+'\n')