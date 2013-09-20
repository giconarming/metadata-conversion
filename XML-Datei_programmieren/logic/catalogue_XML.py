__author__ = 'nico'

f = open('../input/ATS_TOA_1PRBCM20030102_113342_000000482012_00337_04399_0003.N1', 'r')

for i in range(16):
      line = f.readline()


      a = 'PRODUCT='
      if line.startswith(a):
          print(line)

      b = 'ACQUISITION_STATION='
      if line.startswith(b):
          print(line)

      c = 'PROC_CENTER='
      if line.startswith(c):
          print(line)

      d = 'PROC_TIME='
      if line.startswith(d):
          print(line)

      e = 'SOFTWARE_VER='
      if line.startswith(e):
          print(line)

      j = 'SENSING_START='
      if line.startswith(j):
          print(line)

      g = 'SENSING_STOP='
      if line.startswith(g):
          print(line)

      h = 'ABS_ORBIT='
      if line.startswith(h):
          print(line)



f.close()