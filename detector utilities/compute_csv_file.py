import os
import struct
import sys
import fnmatch


def recglob(directory, ext):
    lst = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, ext):
            lst.append(os.path.join(root, filename))
    return lst


def main():
    ultrafacefile = sys.argv[1]
    directory = sys.argv[2]
    outputcsv = sys.argv[3]

    with open(ultrafacefile) as fin:
        lst = fin.readlines()
        header = lst[0].strip().split(',')
        uff = []
        for item in lst[1:]:
            d = {}
            for h, x in zip(header, item.strip().split(',')):
                d[h] = x
            uff.append(d)

    fout = open(outputcsv, 'w')
    header = ['FILE']
    for i in range(1, 513):
        header.append('DEEPFEATURE_%d' % i)
    fout.write(','.join(header) + '\n')
    lw = []

    for line in uff:
        f = open(os.path.join(directory, line['TEMPLATE_ID']) + '.tmpl', 'rb')
        n = 1024
        lst = list(struct.unpack('f' * n, f.read(4 * n)))
        lres = []
        lres.append(line['FILENAME'])
        for x in lst:
            lres.append(str(x))
        lw.append(','.join(lres[0:513]))
    fout.write('\n'.join(lw))


if __name__ == "__main__":
    main()
