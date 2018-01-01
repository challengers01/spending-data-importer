import sqlite3
import csv
import datetime
import dbutil
import os

csv_data_location = "../data"
archive_data_location = "../data/Archive"
dbutil.create_expenses_database()
dbutil.insert_cateogory_records()

def import_chase_stmt(csvfilepath):
    print "In import_chase_stmt"
    print csvfilepath
    with open(csvfilepath, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        start = -1
        recordList = []
        count = 0
        for row in spamreader:
            if row:
                if start == 0:
                    recordList.append([])
                    date = row[2]
                    desc = row[3]
                    amt = row[4]
                    category = ""
                    src = "Chase"
                    recordList[count].append(date)
                    recordList[count].append(desc)
                    recordList[count].append(amt)
                    recordList[count].append(src)
                    count = count + 1
                if "Type" == row[0]:
                    start = 0
        print recordList
        dbutil.insert_records(recordList)

def import_bofa_stmt(csvfilepath):
    with open(csvfilepath, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        start = -1
        recordList = []
        count = 0
        for row in csvreader:
            if row:
                if start == 0:
                    recordList.append([])
                    date = row[0]
                    desc = row[1]
                    amt = row[2]
                    category = ""
                    src = "BOFA Checking"
                    recordList[count].append(date)
                    recordList[count].append(desc)
                    recordList[count].append(amt)
                    recordList[count].append(src)
                    count = count + 1
                if "Date" == row[0]:
                    start = 0
        print recordList
        dbutil.insert_records(recordList)

def import_bofa_credit_stmt(csvfilepath):
    with open(csvfilepath, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        start = -1
        recordList = []
        count = 0
        for row in csvreader:
            if row:
                if start == 0:
                    recordList.append([])
                    date = row[0]
                    desc = row[2]
                    amt = row[4]
                    category = ""
                    src = "BOFA Credit"
                    recordList[count].append(date)
                    recordList[count].append(desc)
                    recordList[count].append(amt)
                    recordList[count].append(src)
                    count = count + 1
                if "Posted Date" == row[0]:
                    start = 0
        print recordList
        dbutil.insert_records(recordList)

def import_costco_stmt(csvfilepath):
    with open(csvfilepath, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        start = -1
        recordList = []
        count = 0
        for row in csvreader:
            if row:
                if start == 0:
                    recordList.append([])
                    date = row[1]
                    desc = row[2]
                    amt = row[3]
                    category = ""
                    src = "Costco"
                    recordList[count].append(date)
                    recordList[count].append(desc)
                    recordList[count].append(amt)
                    recordList[count].append(src)
                    count = count + 1
                if "Status" == row[0]:
                    start = 0
        print recordList
        dbutil.insert_records(recordList)

for subdir, dirs, files in os.walk(csv_data_location):
    print file
    for file in files:
        if file.lower().endswith(".csv"):
            print file
            filepath = subdir + os.sep + file
            if file.find('Chase') != -1:
                print "Implement Chase: " + filepath
                import_chase_stmt(filepath)
            if file.find('689') != -1:
                print "Implement Costco"
                import_costco_stmt(filepath)
            if file.find('6958') != -1:
                print "Implement BOFA Credit Card"
                import_bofa_credit_stmt(filepath)
            if file == 'stmt.csv':
                print "Implement BOFA Checking Account"
                import_bofa_stmt(filepath)
