import sys
cols = ["FILENAME", "TEMPLATE_ID", "SUBJECT_ID", "SIGHTING_ID", "FACE_X", "FACE_Y", "FACE_WIDTH", "FACE_HEIGHT"]
with open(sys.argv[1]) as f:
	with open(sys.argv[2], 'w') as fout:
		lst = f.readlines()
		header = lst[0]
		fout.write(','.join(cols)+'\n')
		i = 0
		for item in lst[1:]:
			vals = item.strip().split(',')
			d = {}
			for (x,y) in zip(header.split(','), vals):
				d[x] = y
			for x in cols:
				if x in d:
					if x in ['FACE_X', 'FACE_Y', 'FACE_WIDTH', 'FACE_HEIGHT']:
						fout.write('{i}'.format(i=int(round(float(d[x])))))
					else:
						fout.write('{i}'.format(i=d[x]))
				else:
					fout.write('{i}'.format(i=i))
				if x=='FACE_HEIGHT':
					fout.write('\n')
				else:
					fout.write(',')
			i = i + 1
