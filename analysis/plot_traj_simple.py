import netCDF4 as nc 
import matplotlib.pylab as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

def read_nc(file_ariane,variable):
	fid = nc.Dataset(file_ariane,'r')
	data = fid.variables[variable][:]
	fid.close()
	return data

def plot_traj_simple(datadir):
	traj_lon = read_nc(datadir + '/' + 'ariane_trajectories_qualitative.nc','traj_lon')
	traj_lat = read_nc(datadir + '/' + 'ariane_trajectories_qualitative.nc','traj_lat')
	traj_time = read_nc(datadir + '/' + 'ariane_trajectories_qualitative.nc','traj_time')

	lon_rho = read_nc('/Volumes/P1/ROMS-Inputs/CCS1/grid/CCS_7k_0-360_fred_grd.nc','lon_rho')
	lat_rho = read_nc('/Volumes/P1/ROMS-Inputs/CCS1/grid/CCS_7k_0-360_fred_grd.nc','lat_rho')

	plt.figure()
	bmap = Basemap(projection='cyl',llcrnrlat=18,urcrnrlat=51,\
                       llcrnrlon=219,urcrnrlon=251,resolution='l')
        parallels = np.arange(20.,60.,10.)
        bmap.drawparallels(parallels,labels=[True,False,False,True])
        meridians = np.arange(220.,260.,10.)
        bmap.drawmeridians(meridians,labels=[True,False,False,True])
	bmap.drawcoastlines()
        bmap.fillcontinents(color='grey',lake_color='white')
	bmap.plot(lon_rho[-1,:],lat_rho[-1,:],'k--')
	bmap.plot(lon_rho[0,:],lat_rho[0,:],'k--')
	bmap.plot(lon_rho[:,-1],lat_rho[:,-1],'k--')
	bmap.plot(lon_rho[:,0],lat_rho[:,0],'k--')
	bmap.scatter(traj_lon,traj_lat,c=traj_time)
	plt.show()


#plot_traj_simple('../runs/run_forward_quali_01')
plot_traj_simple('../runs/run_backward_quali_02')
