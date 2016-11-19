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
c1 		= 'TransactionDate'		# column name
c1_type = 'DATETIME'				# data/column type
c2 		= 'Product'
c2_type = 'CHAR(8)'
c3		= 'Price'
c3_type = 'INT'
c4		= 'PaymentType'
c4_type = 'VARCHAR(10)'
c5 		= 'Name'
c5_type = 'VARCHAR(30)'
c6		= 'City'
c6_type = 'VARCHAR(30)'
c7		= 'State'
c7_type = 'VARCHAR(30)'
c8		= 'Country'
c8_type	= 'VARCHAR(30)'
c9		= 'AccountCreated'
c9_type	= 'DATETIME'
c10		= 'LastLogin'
c10_type= 'DATETIME'

# create table and first column as unique ID
try:
    c.execute('CREATE TABLE {tn} ( ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT )'.format(tn=table))
    db.commit()
    print('Table creation successful')
except MySQLdb.Error as err:
    db.rollback()
    print('Error creating table: {}'.format(err))

# create all other columns
sql = 'ALTER TABLE {0} ADD COLUMN {1} {2},' \
        'ADD COLUMN {3} {4}, ADD COLUMN {5} {6}, ADD COLUMN {7} {8}, ' \
        'ADD COLUMN {9} {10}, ADD COLUMN {11} {12}, ADD COLUMN {13} {14}, ' \
        'ADD COLUMN {15} {16}, ADD COLUMN {17} {18}, ADD COLUMN {19} {20}'.format(table, c1, c1_type, c2, c2_type, c3, c3_type, c4, c4_type, c5, c5_type, c6, c6_type, c7, c7_type, c8, c8_type, c9, c9_type, c10, c10_type)
try:
    c.execute(sql)
    db.commit()
    print('Column creation successful')
except MySQLdb.Error as err:
    db.rollback()
    print('Error creating columns: {}'.format(err))


# set up empty containers for each row/entry
entries = []


with open(file, 'rU') as f:
    reader = csv.reader(f)




# === cleanup 
db.commit()
c.close()
db.close()