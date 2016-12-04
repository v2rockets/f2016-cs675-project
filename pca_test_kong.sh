#!/bin/bash

#$ -N pca_test
#$ -M kag29@njit.edu
#$ -m ae
#$ -cwd
#$ -j y
#$ -q short

module load python2
module load R-Project

COUNTER=0

for FILE in `ls condensed_train*` do
    python2 pca_test_kong.py ../cs675_project/traindata pca.out.${COUNTER}
    Rscript pca.out.${COUNTER}
    COUNTER=`expr $COUNTER + 1`
done
