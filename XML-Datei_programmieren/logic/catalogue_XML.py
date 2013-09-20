__author__ = 'nico'

f = open('../input/ATS_TOA_1PRBCM20030102_113342_000000482012_00337_04399_0003.N1', 'r')
output = open('../output/catalogue_xml.xml', 'w')

for i in range(16):
      line = f.readline()
      write = output.write

      a = 'PRODUCT='
      if line.startswith(a):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])

      b = 'ACQUISITION_STATION='
      if line.startswith(b):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])

      c = 'PROC_CENTER='
      if line.startswith(c):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])

      d = 'PROC_TIME='
      if line.startswith(d):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])

      e = 'SOFTWARE_VER='
      if line.startswith(e):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])

      j = 'SENSING_START='
      if line.startswith(j):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])

      g = 'SENSING_STOP='
      if line.startswith(g):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          write(line[startIndex:endIndex])

      h = 'ABS_ORBIT='
      if line.startswith(h):
          startIndex = line.index('=')+1
          endIndex = len(line)-1
          write(line[startIndex:endIndex])





f.close()