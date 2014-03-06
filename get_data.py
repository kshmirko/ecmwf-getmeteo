#!/usr/bin/env python2
# Setup
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

with file('pro-2013.nc.txt') as f:
    dates=f.readline()
    params = {
    	'dataset' : "interim",
    	'levelist': "1/2/3/5/7/10/20/30/50/70/100/125/150/175/200/225/250/300/350/400/450/500/550/600/650/700/750/775/800/825/850/875/900/925/950/975/1000",
    	'stream'  : "oper",
    	'levtype' : "pl",
    	'param'   : "129.128/203.128/131.128/132.128/157.128/138.128/60.128",
    	'step'    : "0",
    	'grid'    : "0.75/0.75",
    	'time'    : "12/18",
    	'date'    : dates,
    	'type'    : "an",
    	'class'   : "ei",
    	'area'    : "80/100/0/160",
    	'format'  : "netcdf",
    	'target'  : "excange2013.nc",
    }


server.retrieve(params)


