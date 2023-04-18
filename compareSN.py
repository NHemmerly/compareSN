# Program to compare serial numbers from two lists

import csv
import sys

with open(sys.argv[1], 'r') as f0, open(sys.argv[2], 'r') as f1:
    listSN = f0.readlines()
    scanSN = f1.readlines()

for line in scanSN:
    if line in listSN:
        print(line)
