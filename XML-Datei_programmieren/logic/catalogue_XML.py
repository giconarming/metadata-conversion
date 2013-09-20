__author__ = 'nico'

f = open('../input/ATS_TOA_1PRBCM20030102_113342_000000482012_00337_04399_0003.N1', 'r')
output = open('../output/catalogue.xml', 'w')

write = output.write
write('<catalog_entry>')
write('\n')

for i in range(16):
      line = f.readline()




      a = 'PRODUCT='
      if line.startswith(a):
          write('     ')
          write('<product>')
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])
          write('</product>')
          write('\n')

      b = 'ACQUISITION_STATION='
      if line.startswith(b):
          write('     ')
          write('<acquisition_station>')
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex].strip())
          write('</acquisition_station>')
          write('\n')

      c = 'PROC_CENTER='
      if line.startswith(c):
          write('     ')
          write('<proc_center>')
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])
          write('</proc_center>')
          write('\n')

      d = 'PROC_TIME='
      if line.startswith(d):
          write('     ')
          write('<proc_time>')
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])
          write('</proc_time>')
          write('\n')

      e = 'SOFTWARE_VER='
      if line.startswith(e):
          write('     ')
          write('<software_ver>')
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex].strip())
          write('</software_ver>')
          write('\n')

      j = 'SENSING_START='
      if line.startswith(j):
          write('     ')
          write('<sensing_start>')
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])
          write('</sensing_start>')
          write('\n')

      g = 'SENSING_STOP='
      if line.startswith(g):
          write('     ')
          write('<sensing_stop>')
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])
          write('</sensing_stop>')
          write('\n')

      h = 'ABS_ORBIT='
      if line.startswith(h):
          write('     ')
          write('<abs_orbit>')
          startIndex = line.index('=')+1
          endIndex = len(line)-1
          write(line[startIndex:endIndex])
          write('</abs_orbit>')
          write('\n')




write('</catalog_entry>')
f.close()