#!/usr/bin/env python3

import sqlite3
import json
import sys
sys.path.append("..") 
import python3_examples.commonFunctions as cfs

CONFIG = json.load(open('config.json'))
TEST_CONFIG = json.load(open('config-agent_test.json'))
INITIAL_MONEY = 0

def getValue(date, name):
    conn = cfs.create_sqlitle3_connection(CONFIG["SQLITLE_LOCATION"])
    cur = conn.cursor()
    sql = " SELECT * FROM historical WHERE date <= '"+date+"' AND name='"+name+"' ORDER BY date DESC LIMIT 3 "
    rows = ""
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    
    return rows

def react(rows, margin):
    currentStatus = rows[1][2] - rows[2][2]

    if currentStatus > margin: # If value increase
        print("BUY")
    elif currentStatus < margin: # If value decrease
        print("SELL")

if __name__ == '__main__':
    VARIABLE_NAME = ""
    INITIAL_MONEY = INITIAL_MONEY + TEST_CONFIG["INITIAL_MONEY"]

    if len(sys.argv) != 2:
        print("Erroneous parameter number.")
        exit(1)
    else:
        VARIABLE_NAME=sys.argv[1]

    print(("2021-03-01 "+VARIABLE_NAME))
    rows = getValue("2022-03-01",VARIABLE_NAME)
    print(str(len(rows)))

    for row in rows:
        print(row)
    
