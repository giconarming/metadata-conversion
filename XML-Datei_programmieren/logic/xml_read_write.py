__author__ = 'nico'

f = open('../input/ATS_TOA_1PRBCM20030102_113342_000000482012_00337_04399_0003.N1', 'r')

for i in range(30):
      x = f.readline()
      print(x)


f.close()