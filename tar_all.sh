#!/bin/bash

cd $1/curr_labs

for d in */ ; do
    cd $d
    cp ../../../tarring.sh ./
    pwd
    chmod +x tarring.sh
    bash tarring.sh
    rm tarring.sh
    cd ..
done
