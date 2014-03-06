import netCDF4 as nc
import sys


if len(sys.argv)==1:
    sys.exit(-1)
    
for i in range(len(sys.argv)-1):
    f = nc.Dataset(sys.argv[i+1],'r')
    
    Tp = f.variables['time']
    
    T = nc.num2date(Tp, Tp.units)
    
    f.close()
    
    print T[0]

