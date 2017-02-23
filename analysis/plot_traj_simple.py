import netCDF4 as nc 
import matplotlib.pylab as plt

def read_nc(file_ariane,variable):
	fid = nc.Dataset(file_ariane,'r')
	data = fid.variables[variable][:]
	fid.close()
	return data

def plot_traj_simple(datadir):
	traj_lon = read_nc(datadir + '/' + 'ariane_trajectories_qualitative.nc','traj_lon')
	traj_lat = read_nc(datadir + '/' + 'ariane_trajectories_qualitative.nc','traj_lat')
	traj_time = read_nc(datadir + '/' + 'ariane_trajectories_qualitative.nc','traj_time')

	plt.figure()
	plt.scatter(traj_lon,traj_lat,c=traj_time)
	plt.show()


plot_traj_simple('../runs/run_forward_quali_01')
