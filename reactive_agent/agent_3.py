#!/usr/bin/env python3

import sys
from Bank1 import Bank1

    
if __name__ == '__main__':
    if len(sys.argv) != 6:
        print(sys.argv)
        print("Erroneous parameter number.")
        exit(1)
    else:
        myBank = Bank1(sys.argv[1], sys.argv[2],float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]))
        myBank.buyAllCoins()
        
        print(myBank)

        sentence = "SELECT * FROM coinlayer_historical WHERE date <= '2022-03-10' AND name='BTC'"

        print(Bank1.getValues(sentence))
        
    
