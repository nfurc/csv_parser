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

# prepare a cursor object 
c = db.cursor()

# === database set up ===
c1 		= 'TransactionDate'	  # column name
c1_type = 'DATETIME'		  # data/column type
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


# set up empty container for each row/entry
data = []

# read csv file
with open(file, 'rU', delimeter='\t') as f:
    # create file reader
    reader = csv.reader(f, skipinitialspace=True)

    # skip the first line (headers)
    next(reader)

    # gather data in table format (eg. data[x][y] where x = row - 1, y = col)
    for row in reader:
        data.append(row)

# write csv row into database
rno = 0
for row in data:
    if (rno <= len(data)):
        sql = 'INSERT INTO {0} ( {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10} ) ' \
                ' VALUES ( {11}, {12}, {13}, {14}, {15}, "{16}", "{17}", "{18}", {19}, {20}) '
        try:
            c.execute(sql.format( table, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
                              data[rno][0], data[rno][1], data[rno][2], data[rno][3], data[rno][4], 
                              data[rno][5], data[rno][6], data[rno][7], data[rno][8], data[rno][9] ) )
            db.commit()
            print('Row ' + str(row) + ' copied to database')
        except MySQLdb.Error as err:
            db.rollback()
            print(c._last_executed)
            #print('Error copying data: {}'.format(err))

    rno += 1



# === cleanup 
db.commit()
c.close()
db.close()