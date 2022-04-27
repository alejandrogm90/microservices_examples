#!/bin/bash

# VARIABLES AND FUNCTIONS
DIR_HOME=$(cd `dirname $0` && pwd)
source "ssh-examples/scripts/commonFunctions.sh"
SCRIPT_NAME=`getJustStriptName $0`
export LOG_FILE=${DIR_HOME}"/"${SCRIPT_NAME}"_"`date +%F`".log"
SCRIPT_1="./coinlayer/get_day.py"

declare -A script_info
export script_info=(
	[name]="${SCRIPT_NAME}" 
	[location]="${DIR_HOME}" 
	[description]="A simple monthly scrit to get al data of one month" 
	[calling]="./`getStriptName $0`"
)

showScriptInfo

echo "" > $LOG_FILE

reactive_agent/agent_1.py ABC