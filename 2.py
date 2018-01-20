import sys
import csv
import os

dirname = sys.argv[1]

header = "model"
tail = "-Testing-Result.csv"


def opencsv(filename):
    for row in csv.DictReader(open(filename, 'r')):
        return row['NewPredicted']


file = open(os.getcwd() + '/media/' + dirname + "/final.csv", 'w')
for i in range(1, 19):
    file.write(str(i) + "," + opencsv(os.getcwd() + '/media/' + dirname + '/' + header + str(i) + tail) + '\n')
