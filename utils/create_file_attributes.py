import netCDF4 as nc

filein = '/Volumes/P1/ROMS-Inputs/CCS1/grid/CCS_7k_0-360_fred_grd.nc'
fileout = 'Grid_vert_CCS1.nc'

#----------- read grid file (or output file if you prefer) -------------
fidin = nc.Dataset(filein,'r')
hc = fidin.variables['hc'][:]
s_w = fidin.variables['s_w'][:]
cs_w = fidin.variables['Cs_w'][:]
fidin.close()

#----------- write file with S-coord param as global attributes --------
fidout = nc.Dataset(fileout,'w',format='NETCDF3_CLASSIC')
fidout.hc = hc
fidout.sc_w = s_w
fidout.Cs_w = cs_w
fidout.close()

