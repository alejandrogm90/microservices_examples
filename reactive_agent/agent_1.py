#!/usr/bin/env python3

import sqlite3
import json
import sys
sys.path.append("..") 
import python3_examples.commonFunctions as cfs

CONFIG = json.load(open('config.json'))
TEST_CONFIG = json.load(open('config-agent_test.json'))

class myAgent:
    def __init__(self, cDate1, coinName1, cash1, coins1):
        self.cDate = cDate1
        self.coinName = coinName1
        self.cash = cash1
        self.coins = coins1
        self.reaction = "NONE"

    def buyCoins(self,amount,price):
        self.coins = amount / price
        self.cash = amount % price
        self.reaction = "BUY"


    def sellCoins(self,amount,price):
        self.cash = amount * price
        self.coins = 0
        self.reaction = "SELL"

    def react(self,rows):
        previousPrice = rows[1][2]
        currentPrice = rows[0][2]
        if currentPrice > previousPrice and self.cash > 0: # If value increase
            self.buyCoins(self.cash, currentPrice)
        elif currentPrice < previousPrice and self.coins > 0: # If value decrease
            self.sellCoins(self.cash, currentPrice)

    def __str__(self) -> str:
        return self.cDate+"|"+self.reaction+"|"+str(self.cash)+"|"+str(self.coins)


def getValue(date, name):
    conn = cfs.create_sqlitle3_connection(CONFIG["SQLITLE_LOCATION"])
    cur = conn.cursor()
    sql = " SELECT * FROM historical WHERE date <= '"+date+"' AND name='"+name+"' ORDER BY date DESC LIMIT 2 "
    rows = ""
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    
    return rows

    
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Erroneous parameter number.")
        exit(1)
    else:
        a1 = myAgent(sys.argv[1], sys.argv[2],float(sys.argv[3]),float(sys.argv[4]))
        a1.react(getValue(sys.argv[1], sys.argv[2]))

        print(a1)
        

        # print(("2021-03-01 "+coinName))
        # rows = getValue("2022-03-01",coinName)
        # print(str(len(rows)))

        # for row in rows:
        #     print(row)
    
