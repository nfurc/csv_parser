#!/usr/bin/env python

import csv
import MySQLdb

# === config === 
file 		= 'SalesJan2009.csv'
database 	= 'testdb'
table 		= "salesjan2009"

# === initialise mysql ===
# open database connection
db = MySQLdb.connect("localhost","nicholas","password", database )

# prepare a cursor object using cursor() method
c = db.cursor()

# === database set up ===
c1 		= 'TransactionDate'				# column name
c1_type = ''							# data/column type
c2 		= 'Product'
c2_type = ''
c3		= 'Price'
c3_type = ''
c4		= 'PaymentType'
c4_type = ''
c5 		= 'Name'
c5_type = ''
c6		= 'City'
c6_type = ''
c7		= 'State'
c7_type = ''
c8		= 'Country'
c8_type	= ''
c9		= 'AccountCreated'
c9_type	= ''
c10		= 'LastLogin'
c10_type= ''



# set up empty containers for each column
trans_dates = []
products = []
prices = []
payment_types = []
names = []
cities = []
states = []
countries = []
acct_created = []
last_login = []

with open(file, 'rU') as f:
    reader = csv.reader(f)

    for row in reader:
    	trans_dates.append(row[0])
    	products.append(row[1])
    	prices.append(row[2])
    	payment_types.append(row[3])
    	names.append(row[4])
    	cities.append(row[5])
    	states.append[row[6]]
        countries.append(row[7])
    	acct_created.append(row[8])
    	last_login.append(row[9])
    	countries.append(row[10])

    ukcount = 0
    for country in countries:
    	if country == "Poland":
    		ukcount += 1

    print ukcount


# === cleanup 
conn.commit()
cursor.close()
conn.close()