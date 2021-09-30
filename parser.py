# 1. Retrieve the log file across the network.
#imports regexp that'' find requests from 1994-1995
import re

#imports csv module that will show results

import csv
#
from collections import Counter

#
import urllib.request
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
urllib.request.urlretrieve(url, './http_access_log.txt') 



#reads log file and searches for all requests from 1994
def reader(filename):
    with open(filename) as f:
        http_access_log = f.read()
        firstyear = re.findall("1994", http_access_log)
        return(firstyear)

#reads log file and searches for all requests from 1995
def reader2(filename):
    with open(filename) as f:
        http_access_log = f.read()
        secondyear = re.findall("1995", http_access_log)
        return(secondyear)

    
def reader3(filename):
    with open(filename) as f:
        http_access_log = f.read()

        month1 = re.findall("May/1995", http_access_log)
        month2 = re.findall("June/1995", http_access_log)
        month3 = re.findall("July/1995", http_access_log)
        month4 = re.findall("Aug/1995", http_access_log)
        month5 = re.findall("Sep/1995", http_access_log)
        month6 = re.findall("Oct/1995", http_access_log)
        past_6_months_total = month1 + month2 + month3 + month4 + month5 + month6

        return(past_6_months_total)

def count(firstyear):
            return Counter(firstyear)
def count2(secondyear):
            return Counter(secondyear)
def count3(after_6_months_total):
            return Counter(after_6_months_total)
def write_csv(counter):
            with open("1994.csv", "w") as csvfile:
                writer = csv.writer(csvfile)
def write_csv(counter):
            with open("1994.csv", "w") as csvfile:
                writer = csv.writer(csvfile)

                header = ["Year", "Requests"]

                writer.writerow(header)

                for item in counter:
                    writer.writerow( (item,counter[item]))
def write_csv2(counter2):
            with open("1995.csv", "w") as csvfile:
                writer = csv.writer(csvfile)        
def write_csv2(counter2):
            with open("1995.csv", "w") as csvfile:
                writer = csv.writer(csvfile)

                header = ["Year", "Requests"]

                writer.writerow(header)

                for item in counter2:
                    writer.writerow( (item,counter2[item]))
def write_csv3(counter3):
            with open("1994.csv", "w") as csvfile:
                writer = csv.writer(csvfile)
def write_csv3(counter3):
     with open("6months.csv", "w") as csvfile:
            writer = csv.writer(csvfile)

            header = ["Past 6 Months", "Requests"]

            writer.writerow(header)

            for item in counter3:
            
                writer.writerow( (item,counter3[item]))            
if __name__ == "__main__":
            write_csv(count(reader("http_access_log.txt")))  
            write_csv2(count2(reader2("http_access_log.txt")))    
            write_csv3(count3(reader3("http_access_log.txt")))          


