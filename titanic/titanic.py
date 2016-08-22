#-------------------------- Import Statements ----------------------------------
import numpy as np
import pandas
import csv
import sys
import os
#--------------------------- Named Constants -----------------------------------
TRAINING_FILENAME = 'train.csv'
TESTING_FILENAME = 'test.csv'
header_idx = {  
    "survived" : 1,  
    "pclass" : 2,
    "sex" : 4,
    "age" : 5,
    "sibsp" : 6,
    "parch" : 7,
    "ticket" : 8,
    "price group": 9,
    "fare" : 10,
    "cabin" : 11,
    "embarked" : 12 
}

#---------------------- Resource Handling Functions ----------------------------
def top_level_path() :
    path_with_dir = os.path.dirname(os.path.realpath(__file__))
    top_path, discarded_dir = os.path.split(path_with_dir)
    return "/" + top_path

def data_dir_path() :
    return os.path.join(top_level_path(), 'data')

def get_training_data(file_name) :
    try :
        #Attempt to open the file
        infile = open(
            os.path.join(data_dir_path(), file_name), 'rb')
    except IOError as e :
        print e # file not found
        sys.exit(1)
    else :
        csv_reader = csv.reader(infile) # create csv reader obj for easy access
        header = csv_reader.next()      # discard of header row
        # copy the contents of the cvs file into an array
        data = []
        for row in csv_reader :        
            data.append(row)
        return np.array(data)

def get_column_data(col_name) :
    return data[:,header_idx[col_name]]

data =  get_training_data(TRAINING_FILENAME)

passengers_total = np.size(get_column_data('survived').astype(np.float))
print "Total number of passengers: {0}".format(passengers_total)
survived_total = np.sum(get_column_data('survived').astype(np.float))
print "Total number of survivors: {0}".format(survived_total)
proportion_survivors = survived_total / passengers_total
print "Proportion of passengers who survived: {0:.2f}%".format(
    proportion_survivors)

male_only_stats = data[:,header_idx['sex']] == "male"
female_only_stats =  data[:,header_idx['sex']] == "female"



