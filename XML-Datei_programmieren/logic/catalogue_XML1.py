__author__ = 'nico'
from xml.sax.saxutils import escape
import sys


f = open(sys.argv[1], 'r')
output = open('../output/catalogue.xml', 'w')
write = output.write
write('<catalog_entry>')
write('\n')

for i in range(75):
    line = f.readline()
    z = line.find('=')
    v = line.find('"')
    x = line[0:z]

    if v >=0:
        y = len(line)-2
        w = z+2
    else:
        y = len(line)
        w = z+1


    if z >=0:
        write('   ')
        write('<'+x.lower()+'>')
        write(escape(line[w:y].strip()))
        write('</'+x.lower()+'>\n')
    elif z < 0:
        pass


write('</catalog_entry>')
f.close()