import numpy as np
import netCDF4 as nc

class segrid_object():

	def __init__(self,roms_gridfile):
		self.mask = self.read_nc(roms_gridfile,'mask_rho')
		self.ny, self.nx = self.mask.shape
		self.segments = np.zeros((self.ny, self.nx),dtype=np.int8)
		return None

	def read_nc(self,ncfile,variable):
		fid = nc.Dataset(ncfile,'r')
		data = fid.variables[variable][:]
		fid.close()
		return data

	def write_segrid_file(self):
		f = open('segrid_base','w')
		for kline in np.arange(self.ny,0,-1):
			line = ''
			for kcol in np.arange(self.nx):
				if self.mask[kline-1,kcol] == 1:
					line = line + '+'
				else:
					line = line + '#'
			line = line + '\n'
			f.write(line)
		f.close()
		return None

	def add_segment_x(self,xmin,xmax,y=0,nsegment=1):
		self.segments[self.ny-y,xmin:xmax] = nsegment
		return None

	def add_segment_y(self,ymin,ymax,x=0,nsegment=1):
		self.segments[self.ny-ymax:self.ny-ymin,x] = nsegment
		return None

	def add_to_segrid_file(self):
		f = open('segrid_base','r')
		lines = f.readlines()
		f.close()

		f = open('segrid','w')
		for kline in np.arange(self.ny):
			print kline
			line = list(lines[kline])
			for kcol in np.arange(self.nx):
				if self.segments[kline,kcol] !=0:
					if line[kcol] != '#':
						line[kcol] = str(self.segments[kline,kcol])
			newline = ''.join(line)
			f.write(newline)
		f.close()
		return None





# main
roms_grd = '/Volumes/P1/ROMS-Inputs/CCS1/grid/CCS_7k_0-360_fred_grd.nc'
ccs = segrid_object(roms_grd)
ccs.write_segrid_file()
ccs.add_segment_x(110,181,y=325,nsegment=1)
ccs.add_segment_x(110,181,y=225,nsegment=1)
ccs.add_segment_y(225,325,x=110,nsegment=1)

ccs.add_segment_x(60,181,y=390,nsegment=2)
ccs.add_segment_x(60,181,y=160,nsegment=3)
ccs.add_segment_y(160,390,x=60,nsegment=4)



ccs.add_to_segrid_file()
