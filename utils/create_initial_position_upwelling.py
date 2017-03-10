import numpy as np
import netCDF4 as nc
import random


def position_from_file(ncfile):
	fid = nc.Dataset(ncfile,'r')
	temp = fid.variables['temp'][0,46:,:,:].squeeze() # take only 4 surface levels
	fid.close()

	temperature_criterion = np.ones(temp.shape)
	temperature_criterion[np.where(temp < 11)] = 0
	temperature_criterion[np.where(temp > 13)] = 0

	j_criterion = np.ones(temp.shape)
	j_criterion[:,:225,:] = 0
	j_criterion[:,400:,:] = 0

	i_criterion = np.ones(temp.shape)
	i_criterion[:,:,:70] = 0

	total_criterion = temperature_criterion * j_criterion * i_criterion

	total_position = np.where(total_criterion == 1)
	npart_possible = len(total_position[0])

	list_part = np.arange(npart_possible)

	nsubset = 100
	subset_part = random.sample(list_part,nsubset)
	print subset_part

	subset_position = np.empty((nsubset,3))
	for kp in np.arange(nsubset):
		subset_position[kp,0] = total_position[0][subset_part[kp]] # k
		subset_position[kp,1] = total_position[1][subset_part[kp]] # j
		subset_position[kp,2] = total_position[2][subset_part[kp]] # i

	# write file
	f = open('initial_position.txt','w')
	for kp in np.arange(nsubset):
		line = str(subset_position[kp,2] + 0.5) + ' ' + str(subset_position[kp,1] + 0.5) + ' ' + str(4 - subset_position[kp,0] ) + ' 776 1.0\n'
		f.write(line)
	f.close()
	#print subset_position




filein='/Volumes/P4/workdir/raphael/ariane-roms-examples/runs/run_backward_quali_02/inputs/' + 'CCS1-RD.NVOcobalt23R_00776_avg.nc'
position_from_file(filein)
