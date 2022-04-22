#!/usr/bin/env python3

import requests
import pymongo
import json
import sys
sys.path.append("..") 
import commonFunctions as cfs

if __name__ == '__main__':

    if len(sys.argv) != 2:
        cfs.myError("Númeero de parámetros erroneo.",1)

    if not cfs.isDate(sys.argv[1]):
        cfs.myError("La fecha introducida es erronea.",2)

    config = json.load(open('../config.json'))

    SELECTED_DATE = str(sys.argv[1])
    HOST_URL = config["HOST_URL"]
    ACCESS_KEY = config["ACCESS_KEY"]
    URL1 = HOST_URL+"/api/list?access_key="+ACCESS_KEY
    URL_MONGODB = config["URL_MONGODB"]
    
    payload = {}
    headers = {}

    response = requests.request("GET", URL1, headers=headers, data=payload)
    data = response.json()

    finalData = {
        "_id": SELECTED_DATE,
        "version": "1",
        "crypto": data["crypto"],
        "fiat": data["fiat"]
    }

    myClient = pymongo.MongoClient(URL_MONGODB)
    myDataBase = myClient["coinlayer"]
    myCollection = myDataBase["list"]

    MY_QUERY_TEXT = { "_id": SELECTED_DATE }
    if myCollection.count_documents(MY_QUERY_TEXT) > 0:
        x = myCollection.replace_one(MY_QUERY_TEXT,finalData)
    else:
        x = myCollection.insert_one(finalData)
