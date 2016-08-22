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
        infile.close()
        return np.array(data)

def get_column_data(col_name) :
    return data[:,header_idx[col_name]]

data =  get_training_data(TRAINING_FILENAME)

#----------------------------- Main Script -------------------------------------
def main() :
    
    # Calculate overall proportion of surviving passengers
    passengers_total = np.size(get_column_data('survived').astype(np.float))
    print "Total number of passengers: {0}".format(passengers_total)
    survived_total = np.sum(get_column_data('survived').astype(np.float))
    print "Total number of survivors: {0}".format(survived_total)
    proportion_survivors = survived_total / passengers_total
    print "Proportion of passengers who survived: {0:.2f}%".format(
        proportion_survivors)

    # Calculate proportion of survivors for females only
    female_only_stats =  get_column_data('sex') == "female"
    women_data = data[female_only_stats,header_idx['survived']].astype(np.float)
    women_survivors = np.sum(women_data)
    women_total = np.size(women_data)
    prop_women_survivors = women_survivors / women_total
    print "Proportion of women that survived: {0:.2f}%".format(
        prop_women_survivors)
    
    # Calculate proportion of survivors for men only
    male_only_stats = get_column_data('sex') == "male"
    men_data = data[male_only_stats,header_idx['survived']].astype(np.float)
    men_survivors = np.sum(men_data)
    men_total = np.size(men_data)
    prop_men_survivors = men_survivors / men_total
    print "Proportion of men that survived: {0:.2f}%".format (
        prop_men_survivors)

    # Open file that contains test data and wrap in csv reader
    test_data_file = open(os.path.join(data_dir_path(), 'test.csv'), 'rb')
    test_data_reader = csv.reader(test_data_file)
    header = test_data_reader.next()

    # Create a new file where we will make out predictions
    prediction_file = open(os.path.join(data_dir_path(), 'pyresults.csv'), 'wb')
    prediction_data_writer = csv.writer(prediction_file)

    # Read in test file row by row and make prediction based on gender
    prediction_data_writer.writerow(['PassengerId', 'Survived'])
    for row in test_data_reader :
        if row[3] == 'female' :
            prediction_data_writer.writerow([row[0], 1])
        elif row[3] == 'male' :
            prediction_data_writer.writerow([row[0], 0])
    test_data_file.close()
    prediction_file.close()

if __name__ == "__main__" :
    main()
