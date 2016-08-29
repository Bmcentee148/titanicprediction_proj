"""This is a script that evaluates the training data for the titanic project."""

#----------------------------- Import Statements -------------------------------
import os
import csv
import numpy as np
from paths import top_level_path

#----------------------------- Main Script -------------------------------------
def main() :
    #Open csv file and import the data it contains
    data = []
    header = []
    try :
        training_file = open (
            os.path.join(top_level_path(), 'data', 'train.csv'), 'rb')
    except IOError as e :
        print e
        sys.exit(1)
    else :
        train_reader = csv.reader(training_file)
        header = train_reader.next()
        for row in train_reader :
            data.append(row)
        training_file.close()

    data = np.array(data) # convert data to numpy array type
    
    passengers_total = np.size(data[:,1].astype(np.float))
    print "Total number of passengers: {0:.0f}".format(passengers_total)
    num_survivors = np.sum(data[:,1].astype(np.float))
    print "Number of passengers who survived: {0:.0f}".format(num_survivors)
    pct_survived = (num_survivors / passengers_total) * 100
    print "Percentage of passengers who survived: {0:.0f}%".format(pct_survived)

    print "=" * 80 # divider for output, below is analysis on males only

    male_mask = data[:,4] == 'male'
    male_data = data[male_mask, :]
    
    males_total = np.size(male_data[:,1].astype(float))
    print "Total number of male passengers: {0:.0f}".format(males_total)
    num_male_survivors = np.sum(male_data[:,1].astype(float))
    print "Number of male passengers who survived: {0:.0f}".format (
        num_male_survivors)
    pct_male_survivors = (num_male_survivors / males_total) * 100
    print "Percentage of male passengers who survived: {0:.0f}%".format (
        pct_male_survivors)

    print "=" * 80 # divider for output, below is analysis for females only

    female_mask = data[:,4] == 'female'
    female_data = data[female_mask, :]

    females_total = np.size(female_data[:,1].astype(float))
    print "Total number of female passengers: {0:.0f}".format(females_total)
    num_female_survivors = np.sum(female_data[:,1].astype(float))
    print "Number of female passengers who survived: {0:.0f}".format (
        num_female_survivors)
    pct_female_survivors = (num_female_survivors / females_total) * 100
    print "Percentage of female passengers who survived: {0:.0f}%".format (
        pct_female_survivors)



if __name__ == '__main__' :
    main() # run the script
