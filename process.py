import os
import sys


dirname = sys.argv[1]
email = sys.argv[2]
# extracting features
os.system(
    'java -jar PaDEL-Descriptor.jar -2d -3d -dir ' + 'media/' + dirname + '/ -file ' + 'media/' + dirname + '/res.csv')
# making prediction csv
os.system('python3 1.py ' + dirname)
# making binary-classfication predictions
os.system('Rscript ' + os.getcwd() + '/models/testingNewDataSet.R ' + dirname)
# extracting results
os.system('python3 2.py ' + dirname)
# processing results
os.system('python3 3.py ' + dirname + " " + email)


