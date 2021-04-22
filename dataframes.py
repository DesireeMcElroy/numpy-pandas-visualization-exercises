# Exercises


import pandas as pd
import numpy as np
from pydataset import data

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)



# Copy the code from the lesson to create a dataframe full of student grades.



# 1a. Create a column named passing_english that indicates whether each 
# student has a passing grade in english.
df['passing_english'] = df.english >= 70


# 1b. Sort the english grades by the passing_english column. 
# How are duplicates handled?
df.sort_values(by='passing_english')


# 1c. Sort the english grades first by passing_english and then by 
# student name. 

# All the students that are failing english should be first, and within 
# the students that are failing english they should be ordered alphabetically. 

# The same should be true for the students passing english. 
# (Hint: you can pass a list to the .sort_values method)
df.sort_values(by=['passing_english', 'name'], ascending=[True, True])




# 1d. Sort the english grades first by passing_english, and then by 
# the actual english grade, similar to how we did in the last step.
df.sort_values(by=['passing_english', 'english'], ascending=[True, True])





# 1e. Calculate each students overall grade and add it as a column on 
# the dataframe. The overall grade is the average of the math, english, 
# and reading grades.
df['overall_grd'] = ((df.math + df.english + df.reading) / 3)






# 2. Load the mpg dataset. Read the documentation for the dataset and use it 
# for the following questions:
mpg = data('mpg')


# How many rows and columns are there?
mpg.shape
#234 rows x 11 columns


# What are the data types of each column?
mpg.dtypes


# Summarize the dataframe with .info and .describe
mpg.info()
mpg.describe()


# Rename the cty column to city.
mpg.rename(columns={'city': 'city'})


# Rename the hwy column to highway.
mpg.rename(columns={'hwy': 'highway'})



# Do any cars have better city mileage than highway mileage?
(mpg.cty > mpg.hwy).any()




# Create a column named mileage_difference this column should contain the 
# difference between highway and city mileage for each car.
mpg['mileage_difference'] = (mpg.hwy - mpg.cty)



# Which car (or cars) has the highest mileage difference?
mpg.mileage_difference.max()



# Which compact class car has the lowest highway mileage? 
mpg[mpg['class'] == 'compact'].sort_values(by='hwy', ascending = True).head(1)

# The best?
mpg[mpg['class'] == 'compact'].sort_values(by='hwy', ascending = False).head(1)



# Create a column named average_mileage that is the mean of the city 
# and highway mileage.
mpg['average_mileage'] = (mpg.hwy + mpg.cty)/2


# Which dodge car has the best average mileage? The worst?
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by="average_mileage", ascending = False).head(1)






# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mammals_df = data('Mammals')

# How many rows and columns are there?
mammals_df.shape
# (107, 4)


# What are the data types?
mammals_df.dtypes
# weight      float64
# speed       float64
# hoppers        bool
# specials       bool


# Summarize the dataframe with .info and .describe
mammals_df.info()
mammals_df.describe()


# What is the the weight of the fastest animal?
mammals_df[mammals_df.speed == mammals_df.speed.max()]


# What is the overal percentage of specials?
total_true = mammals_df['specials'][mammals_df['specials']==True].count()
total_specials = mammals_df['specials'].count()

percent_of_specials = total_true / total_specials
# 0.0935


# How many animals are hoppers that are above the median speed? 
# What percentage is this?
mammals_speed_median = mammals_df.speed.median()
# 48
mammals_df.speed == 48 # only one has median speed of 48

fast_hoppers = (mammals_df.speed > mammals_speed_median) & (mammals_df.hoppers==True)
fast_hoppers = mammals_df[fast_hoppers]
len(fast_hoppers)

total = mammals_df.speed.count() # 107 total

percentage_of_fast_hoppers = (len(fast_hoppers) / total) * 100
# 6.54% of animals are hoppers with speed above the median.