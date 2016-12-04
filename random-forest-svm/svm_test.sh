#!/bin/bash

#$ -N random_forest_test
#$ -M kag29@njit.edu
#$ -m ae
#$ -cwd
#$ -j y
#$ -q short

module unload python3
module load python2

COUNTER=0

for FILE in `ls ../training_labels/split.70.30*`
do
    python svm_test.py $HOME/cs675_project/traindata $FILE svm.out.${COUNTER}
    COUNTER=`expr $COUNTER + 1`
    #echo "BALANCED ERROR"
    python GorskiK_balancederr.py rf.svm.out.${COUNTER} $HOME/cs675_project/trueclass
    #echo
done
