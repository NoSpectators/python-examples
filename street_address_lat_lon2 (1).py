# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 20:11:33 2016

@author: John
"""
import requests
from bs4 import BeautifulSoup
import requests
import re 
import sqlite3
import time 
import csv

def getLatLonGoogle(address):
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=%s' % (address))
    resp_json_payload = response.json()
    return ((resp_json_payload['results'][0]['geometry']['location']),
            (resp_json_payload['results'][0]['address_components'][6]['long_name'])) 
    
#print( getLatLonGoogle("262 56th Pl, Washington D.C, MD"))
#lat_lon_zip = getLatLonGoogle("262 56th Pl, Washington D.C, MD")
#print lat_lon_zip[0]['lat']
#print lat_lon_zip[1]

myFile = open('Blighted_Buildings4.csv','rt')
myReader = csv.reader(myFile)   
blighted =[]
   
for row in myReader:
    if row[0] != 'Street#':        
        street_address = str(row[0]) + " " + str(row[1]) + " " +str(row[2])
        lat_lon_zip = getLatLonGoogle(street_address+", Washington D.C, MD")
        StreetNum=row[0]
        StreetName=row[1]
        StreetType = row[2]
        Quad=row[3]
        Ward =row[4]
        Square=row[5]
        Lot=row[6]
        Lat = lat_lon_zip[0]['lat']
        Lon = lat_lon_zip[0]['lng']
        Zip = lat_lon_zip[1]
        blighted.append((street_address,Quad, Ward, Square, Lot, Lat, Lon, Zip))
        time.sleep(1)       
myFile.close()

vacant=[]
myFile = open('Vacant_3.csv','rt')
myReader = csv.reader(myFile)    
for row in myReader:
    if row[0] != 'Street#':        
        street_address = str(row[0]) + " " + str(row[1]) + " " +str(row[2])
        lat_lon = getLatLonGoogle(street_address+", Washington D.C, MD")
        StreetNum=row[0]
        StreetName=row[1]
        StreetType = row[2]
        Quad=row[3]
        Ward =row[4]
        Square=row[5]
        Lot=row[6]
        Lat = lat_lon_zip[0]['lat']
        Lon = lat_lon_zip[0]['lng']
        Zip = lat_lon_zip[1]
        vacant.append((street_address,Quad, Ward, Square, Lot, Lat, Lon, Zip))
        time.sleep(.5)       

myFile.close()

with open('blighted.csv','wb') as fp:
    a = csv.writer(fp, delimiter=",")
    a.writerow(['Street Address','Quad','Ward','Square','Lot','Lat', 'Lon','Zip'])
    a.writerows(blighted)
     
with open('vacant.csv','wb') as fp:
    a = csv.writer(fp, delimiter=",")
    a.writerow(['Street Address','Quad','Ward','Square','Lot','Lat', 'Lon','Zip'])
    a.writerows(vacant)
    
vacant_lat_lon=[]
for item in vacant:
    lat = item[5]
    lon = item[6]
    vacant_lat_lon.append((lat,lon))
    
with open('vacant_lat_lon.csv', 'wb') as fp:
    a = csv.writer(fp, delimiter=",")
    a.writerows(vacant_lat_lon)
    
blighted_lat_lon = []
for item in blighted:
    lat = item[5]
    lon = item[6]
    blighted_lat_lon.append((lat,lon))
with open('blighted_lat_lon.csv','wb') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(blighted_lat_lon)
    

##test
#print( getLatLonGoogle("262 56th Pl, Washington D.C, MD"))

