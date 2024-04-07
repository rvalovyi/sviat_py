#!/bin/bash

MYPATH=/home/pi/Adeept_AWR/sviat
FILE=$MYPATH/$1
trap ctrl_c INT

ctrl_c() {
    echo "*** Ctrl+C happened"
    ssh raspberry "ps -ef | grep 'sudo python3 $FILE' | grep -v grep | awk '{print \$2}' | xargs sudo kill -2"
}

if [ "$#" -ne 1 ]; then
    echo "You must enter your script name: start.sh <script name>"
else
    scp $1 raspberry:$MYPATH/
    echo "*** Started."
    ssh raspberry "cd $MYPATH && ./run.sh $1"
    echo "*** Finished."
fi
