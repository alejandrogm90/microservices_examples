#!/bin/bash

DIR_HOME=$(cd `dirname $0` && pwd)

if [ -f "${DIR_HOME}/ssh_examples/scripts/commonFunctions.sh" ] ; then
    git submodule sync
    git submodule update --init --recursive
    git pull --recurse-submodules
else 
    git submodule sync
    git submodule update --init --recursive
fi
