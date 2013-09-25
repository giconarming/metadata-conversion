__author__ = 'nico'
from xml.sax.saxutils import escape
import sys


input = sys.stdin
output = sys.stdout
#f = open(sys.argv[1], 'r')
#output = open('../output/catalogue.xml', 'w')
write = output.write

for i in range(80):
    line = input.readline()
    z = line.find('=')
    v = line.find('"')
    x = line[0:z]

    if v >=0:
        y = len(line)-2
        w = z+2
    else:
        y = len(line)-1
        w = z+1


    if z >=0:
        if i == 0:
            write(escape(line[w:y].strip()))
            write('\t')
            write('<catalog_entry>')
        write('<'+x.lower()+'>')
        write(escape(line[w:y].strip()))
        write('</'+x.lower()+'>')
    elif z < 0:
        pass


write('</catalog_entry>')
input.close()