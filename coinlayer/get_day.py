#!/usr/bin/env python3
#
#
#       Copyright 2022 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
    URL1 = HOST_URL+"/"+SELECTED_DATE+"?access_key="+ACCESS_KEY
    URL_MONGODB = config["URL_MONGODB"]
    
    payload = {}
    headers = {}

    response = requests.request("GET", URL1, headers=headers, data=payload)
    data = response.json()

    finalData = {
        "_id": SELECTED_DATE,
        "version": "1",
        "timestamp": data["timestamp"],
        "target": data["target"],
        "rates": data["rates"]
    }

    myClient = pymongo.MongoClient(URL_MONGODB)
    myDataBase = myClient["coinlayer"]
    myCollection = myDataBase["historical"]

    MY_QUERY_TEXT = { "_id": SELECTED_DATE }
    if myCollection.count_documents(MY_QUERY_TEXT) > 0:
        x = myCollection.replace_one(MY_QUERY_TEXT,finalData)
    else:
        x = myCollection.insert_one(finalData)
