#!/bin/bash

#PBS -l walltime=00:01:00,nodes=3:ppn=2
#PBS -N job1
#PBS -q batch

cd "$PBS_O_WORKDIR" || exit 1
mpirun --hostfile "$PBS_NODEFILE" -np 6 ./task_Pi