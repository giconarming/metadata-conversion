__author__ = 'nico'

f = open('../input/ATS_TOA_1PRBCM20030102_113342_000000482012_00337_04399_0003.N1', 'r')

for i in range(16):
      line = f.readline()

      a = 'PRODUCT='
      if line.startswith(a):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          print(line[startIndex:endIndex])


      b = 'ACQUISITION_STATION='
      if line.startswith(b):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          print(line[startIndex:endIndex])

      c = 'PROC_CENTER='
      if line.startswith(c):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          print(line[startIndex:endIndex])

      d = 'PROC_TIME='
      if line.startswith(d):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          print(line[startIndex:endIndex])

      e = 'SOFTWARE_VER='
      if line.startswith(e):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          print(line[startIndex:endIndex])

      j = 'SENSING_START='
      if line.startswith(j):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          print(line[startIndex:endIndex])

      g = 'SENSING_STOP='
      if line.startswith(g):
          startIndex = line.index('\"')+1
          endIndex = len(line)-2
          print(line[startIndex:endIndex])

      h = 'ABS_ORBIT='
      if line.startswith(h):
          startIndex = line.index('=')+1
          endIndex = len(line)-1
          print(line[startIndex:endIndex])





f.close()