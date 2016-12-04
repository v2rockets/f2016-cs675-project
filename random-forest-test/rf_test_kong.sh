#!/bin/bash

#$ -N random_forest_test
#$ -M kag29@njit.edu
#$ -m ae
#$ -cwd
#$ -j y
#$ -q short

module load python2
module load R-Project

COUNTER=0

for FILE in `ls ../pca_trainlabels/condensed_train*` do
    python2 rf_test.py ../cs675_project/traindata rf.out.${COUNTER}
    Rscript rf.out.${COUNTER}.results
    COUNTER=`expr $COUNTER + 1`
done
