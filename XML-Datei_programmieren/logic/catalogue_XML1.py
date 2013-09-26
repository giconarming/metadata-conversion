__author__ = 'nico'
from xml.sax.saxutils import escape
import sys


f = open(sys.argv[1], 'r')
output = open('../output/catalogue.xml', 'w')
write = output.write
write('<catalog_entry>\n')

try:
    for i in range(75):
        line = f.readline()
        gleich = line.find('=')
        anfuehrungs = line.find('"')
        tag = line[0:gleich]

        if anfuehrungs >=0:
            wertende = len(line)-2
            wertanfang = gleich+2
        else:
            wertende = len(line)-1
            wertanfang = gleich+1


        if gleich >=0:
            write('   ')
            write('<'+tag.lower()+'>')
            write(escape(line[wertanfang:wertende].strip()))
            write('</'+tag.lower()+'>\n')
except Exception as ex:
    print('ERROR\n')
    print('can\'t read the file!\n')

write('</catalog_entry>')
f.close()