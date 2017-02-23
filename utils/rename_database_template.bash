#!/bin/bash

# this script assumes your model outputs are stored under ROOTDIR/CONFCASE/year/

ROOTDIR=/Volumes/P7/ROMS/CCS1
CONFCASE=CCS1-RD.NVOcobalt23R
FYEAR=1996
LYEAR=1998

#---------------------------------------------------------

if [ ! -d inputs ] ; then mkdir inputs ; fi

ct=1
for year in $( seq $FYEAR $LYEAR ) ; do
    filelist=$( ls $ROOTDIR/$CONFCASE/$year | grep avg )
    for file in $filelist ; do
        ct5=$( printf %05g $ct )
        fileout=${CONFCASE}_${ct5}_avg.nc
        ln -s $ROOTDIR/$CONFCASE/$year/$file ./inputs/$fileout
        ct=$(( $ct + 1 ))
    done
done
