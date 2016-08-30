"""Analyzes the training data based on gender, class, and ticket price."""

#------------------------------ Import Statements ------------------------------
import csv
import os
import sys
import numpy as np
from paths import top_level_path

#----------------------- Resource Handling Functions ---------------------------
def get_csv_data(csv_file) :
    data_reader = csv.reader(csv_file)
    header = data_reader.next()
    data_list = []
    for row in data_reader :
        data_list.append(row)
    return np.array(data_list)
#-------------------------------- Main Script ----------------------------------

def main() :
    # First we have to grab the training data from our file
    try :
        train_path = os.path.join(top_level_path(), 'data','train.csv')
        with open(train_path, 'rb') as train_file:
            data = get_csv_data(train_file)
    except IOError as e:
        print e
        sys.exit(1)

    # Now we add a cieling to the ticket prices for equal size bins
    fare_cieling = 40
    fare_mask = data[:,10].astype(np.float) >= fare_cieling
    data[fare_mask, 10] = fare_cieling - 1.0

    # Find number of price brackets and different classes
    fare_bracket_size = 10
    num_price_brackets = fare_cieling / fare_bracket_size
    num_classes = len(np.unique(data[:,2]))

    # Initialize the survival table with all zeros
    survival_table = np.zeros((2,num_classes,num_price_brackets))

    # Loop through each category and find all passengers that are included
    for class_idx in xrange(num_classes) :
        for fare_idx in xrange(num_price_brackets) :

            # Using selector masks for each category, grab the survivor column
            # for the passengers that are in that category so we can calculate
            # the proportion who survived
            women_only_stats = data[
                (data[:,4] == 'female') &
                (data[:,2].astype(np.float) == class_idx + 1 ) &
                (data[:,10].astype(np.float) >= fare_idx * fare_bracket_size) &
                (data[:,10].astype(np.float) < (fare_idx + 1)* fare_bracket_size)
                , 1
            ]

            men_only_stats = data[
                (data[:,4] == 'male') &
                (data[:,2].astype(np.float) == class_idx + 1 ) &
                (data[:,10].astype(np.float) >= fare_idx * fare_bracket_size) &
                (data[:,10].astype(np.float) < (fare_idx + 1)* fare_bracket_size)
                , 1
            ]

            # Update survival table for this particular category. This calcs
            # the proportion of survivors for the category and stores it in 
            # the survivor table
            survival_table[0,class_idx,fare_idx] = np.mean(
                women_only_stats.astype(np.float))
            survival_table[1,class_idx,fare_idx] = np.mean(
                men_only_stats.astype(np.float))

    # Division by 0 results in value of nan, and is present in our table.
    # we can get rid of these by checking where the table is not equal to the
    # table and set these value to 0
    survival_table[survival_table != survival_table] = 0 # set nan vals to 0
    print survival_table


    # Use the survival table to determine which categories will survive and
    # which will not. We decide that if the categories survival rate is less
    # than .5 all members of that category die else they survive
    survival_table[survival_table < .5] = 0
    survival_table[survival_table >= .5] = 1

    print survival_table
if __name__ == "__main__" :
    main()
