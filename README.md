# titanicprediction_proj
A solution for the infamous "Titanic" machine learning problem from Kaggle competitions.

### Goal of Project
Given a set of passenger data from people aboard the Titanic, predict whether
or not they will survive.

### Obtain the Data
We are provided a set of data, one for training and one for predicting. These
are given as *train.csv* and *test.csv* respectively. We downloaded them and 
placed them in a */data* folder that lays directly beneath the project folder.

### How Data is Used
We must find **patterns** within the training data to use in predicting
whether another set of passengers will survive. The *train.csv* contains data
for 891 passengers including whether or not they survived. The data for another
418 passengers is located in *test.csv* but the data lacks survival statistics
so we must fill these in the best we can.

We will build better and better predictive models in order to improve our
accuracy. The methods involved in order are:
* Using excel to observe patterns and make predictions
* Using Python to automate this process
* Using Python with Pandas for more efficient data extraction 

#### Excel Method (Very Simplistic)
First we're going to make the assumption that mainly women and children survived
since that is who they tried to save first. We will use excel to look into
this further using the training data.

From our data we find that 75 % of females in our training data survived while
only 19% of the men in our data survive so this is a good place to start. So
what we did was create a new column in the *test.csv* file named *Survived*.
We then created a function that would place a 1 in each passengers cell who
was a female and a 0 in the cell if they were a male.