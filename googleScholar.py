import gscholar
import csv
import time

csvFilePath = "./refs.csv"
keys = "reference"
bibFilePath = "gsh.bib"
f = open(bibFilePath,'w',newline='',encoding='utf-8')

with open(csvFilePath, encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf, delimiter=',')
    i, j = 0, 0
    for rows in csvReader:
        i += 1
        try:
            item = gscholar.query(rows[keys])
        except:
            print("Item {} is failed to retrieve.".format(i))
            j += 1
        if not item:
            print("Item {} is failed to retrieve.".format(i))
            j += 1
        else:
            f = open(bibFilePath,'a+',newline='',encoding='utf-8')
            f.write("".join(item))
            print("Item {} succeeded.".format(i))
        time.sleep(3)

print("{} of {} failed.".format(j, i))