import csv
import sys
import os

dirname = sys.argv[1]


def make_new_csv(filename, columns_names_with_non_null_values):
    outfile = csv.DictWriter(open(os.getcwd() + '/media/' + dirname + '/out.csv', 'w'),
                             fieldnames=columns_names_with_non_null_values)
    outfile.writeheader()
    for row in csv.DictReader(open(filename, 'r')):
        row = {k: row[k] for k in row if k in columns_names_with_non_null_values}
        outfile.writerow(row)


names = ["nS", "nCl", "ATS0m", "AATS3v", "AATS7v", "AATS8v", "AATS5p",
         "AATS8p", "AATS1i", "AATS2i", "AATS5i", "ATSC1m", "ATSC3m", "ATSC4m",
         "ATSC5m", "ATSC6m", "ATSC8m", "ATSC1p", "ATSC5p", "ATSC6p", "ATSC7p",
         "AATSC0m", "AATSC1m", "AATSC2m", "AATSC3m", "AATSC4m", "AATSC8m", "AATSC4p",
         "MATS2c", "MATS5m", "GATS2c", "GATS4m", "GATS5m", "GATS2p", "C3SP2",
         "Mi", "CrippenLogP", "FMF", "MIC2", "ZMIC2", "ZMIC4", "MLogP",
         "VE3_D"]
make_new_csv(os.getcwd() + '/media/' + dirname + '/res.csv', names)
