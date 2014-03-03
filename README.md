ecmwf-getmeteo
==============

Подпрограмма для закачки данных реанализа с сервера ecmwf

Идентификаторы метеорологичеких величин ECMWF


| Parameter Name            |            ECMWF ID |
|:------------------------- | -------------------:|
|Cloud Cover                |            248.128  |
|Geopotential               |            129.128  |
|Ozone Mass Mixing Ratio    |            203.128  |
|Potential Vorticity        |             60.128  |
|Relative Humidity          |            157.128  |
|U-wind (along latitude, X) |            131.128  |
|V-wind (along longitude Y) |            132.128  |
|Relative Vorticity         |            138.128  |


params = {

	'dataset' : "interim",
 
	'levelist': “/11/111/1111”, # уровни высот
	'stream'  : "oper",

	'levtype' : "pl",
  # вертикальная сетка – изобарические поверхности
	
	'param'   : "129.128/203.128/131.128/132.128/157.128/138.128/60.128",
 #необходимые параметы
	
	'step'    : "0",

	'grid'    : "0.75/0.75",
 # сетка
	
	'time'    : "00/06/12/18",
 #временные отсчеты
	
	'date'    : "2012-03-22/2012-03-21/2012-02-15/2011-01-27",
 #временной интервал
	
	'type'    : "an",

	'class'   : "ei",

	'area'    : "80/60/0/160",
 #N/W/S/E

	'format'  : "netcdf",
 # тип выходных данных (по умолчанию - grib)

	'target'  : "excange_events.nc",
 #имя файла для сохранения данных
 
}

