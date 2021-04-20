### Pandas Series

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# 1. Determine the number of elements in fruits.
fruits.size
# 17


# 2. Output only the index from fruits.
fruits.index
# RangeIndex(start=0, stop=17, step=1)


# 3. Output only the values from fruits.
fruits.values
# array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
#        'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',
#        'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',
#        'papaya'], dtype=object)


# 4. Confirm the data type of the values in fruits.
fruits.values.dtype
# dtype('O')


# 5. Output only the first five values from fruits. Output the last 
# three values. Output two random values from fruits.
fruits.head(5)
# 0          kiwi
# 1         mango
# 2    strawberry
# 3     pineapple
# 4    gala apple
# dtype: object

fruits.tail(3)
# 14    blackberry
# 15    gooseberry
# 16        papaya
# dtype: object

fruits.sample(2)
# 16        papaya
# 2     strawberry


# 6. Run the .describe() on fruits to see what information it 
# returns when called on a Series with string values.
fruits.describe()
# count       17
# unique      13
# top       kiwi
# freq         4
# dtype: object



# 7. Run the code necessary to produce only the unique string values from fruits.
fruits.unique()
# array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
#        'honeycrisp apple', 'tomato', 'watermelon', 'honeydew',
#        'blueberry', 'blackberry', 'gooseberry', 'papaya'], dtype=object)


# 8. Determine how many times each unique string value occurs in fruits.
fruits.value_counts()
# kiwi                4
# mango               2
# honeycrisp apple    1
# pineapple           1
# honeydew            1
# gooseberry          1
# watermelon          1
# strawberry          1
# gala apple          1
# blueberry           1
# papaya              1
# tomato              1
# blackberry          1
# dtype: int64



# 9. Determine the string value that occurs most frequently in fruits.
fruits.value_counts().sort_values(ascending=False)
# kiwi                4

# or
fruits.value_counts().head(1)


# 10. Determine the string value that occurs least frequently in fruits.
fruits.value_counts().nsmallest(keep='all') 
# honeycrisp apple    1
# pineapple           1
# honeydew            1
# gooseberry          1
# watermelon          1
# strawberry          1
# gala apple          1
# blueberry           1
# papaya              1
# tomato              1
# blackberry          1

# Exercises Part II


# 1. Capitalize all the string values in fruits.
fruits.str.title()
# 0                 Kiwi
# 1                Mango
# 2           Strawberry
# 3            Pineapple
# 4           Gala Apple
# 5     Honeycrisp Apple
# 6               Tomato
# 7           Watermelon
# 8             Honeydew
# 9                 Kiwi
# 10                Kiwi
# 11                Kiwi
# 12               Mango
# 13           Blueberry
# 14          Blackberry
# 15          Gooseberry
# 16              Papaya

# 2. Count the letter "a" in all the string values (use string vectorization).
sum(fruits.str.count('a'))
# or
fruits.str.count('a').sum()
# 14 total 'a'


# 3. Output the number of vowels in each and every string value.
fruits.str.count('[aeiou]')
# or
fruits.str.count('[aeiou]').sum()
# 49


# 4. Write the code to get the longest string value from fruits.
fruits[fruits.str.len().idxmax()]
# or
max(fruits, key=len)


# 5. Write the code to get the string values with 5 or more letters in the name.
fruits.str.len() >= 5

# 6. Use the .apply method with a lambda function to find the fruit(s) containing 
# the letter "o" two or more times.
fruits[fruits.apply(lambda string: True if string.count('o') >= 2 else False)]
# also
fruits[fruits.apply(lambda string: string.count('o') >= 2)]

# also
fruits[fruits.apply(lambda fruit: fruit.count('o') > 1)]


# 7. Write the code to get only the string values containing the substring "berry".
fruits.str.contains('berry')
# mask it
fruits[fruits.str.contains('berry')]

# 8. Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]

# 9. Which string value contains the most vowels?
fruits[max(fruits.str.count('[aeiou]'))]


# Exercises Part III

let = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
letters = pd.Series(let)

# 1. Which letter occurs the most frequently in the letters Series?
letters.value_counts().head(1)


# 2. Which letter occurs the Least frequently?
letters.value_counts().tail(1)




# 3. How many vowels are in the Series?
vowels = list('aeiou')
# then
letters.isin(vowels).sum()
# 34 vowels



# 4. How many consonants are in the Series?
len(letters[~letters.isin(vowels)])
# or
letters[~letters.isin(vowels)].str.len().sum()



# 5. Create a Series that has all of the same letters but uppercased.
upper_letters = letters.str.upper()


# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.
# letters.value_counts().head(6).plot.bar(rot=0)
# plt.show()



### Use pandas to create a Series named numbers from the following list:

numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])


# 1. What is the data type of the numbers Series?
numbers.dtype
# dtype('O')

# 2. How many elements are in the number Series?
numbers.size
# 20

# 3. Perform the necessary manipulations by accessing Series attributes and 
# methods to convert the numbers Series to a numeric data type.
numbers=numbers.str.replace('$', '').str.replace(',', '').astype('float')


# 4. Run the code to discover the maximum value from the Series.
numbers.max()
# 4789988.17


# 5. Run the code to discover the minimum value from the Series.
numbers.min()
# 278.6


# 6. What is the range of the values in the Series?
numbers.max()-numbers.min()
# 4789709.57




# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
numbers.sort_values(ignore_index=True) # Look at data
# 0, 600000, 1800000, 4200000, 4800000

pd.cut(numbers, [0, 600000, 1800000, 4200000, 4800000]).value_counts()




# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
# pd.cut(numbers, [0, 600000, 1800000, 4200000, 4800000]).value_counts().plot.barh(title='Binned Data', rot=0)
# plt.xlabel='x-axis' 
# plt.ylabel='y-axis'
# plt.show()



# Use pandas to create a Series named exam_scores from the following list:
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# 1. How many elements are in the exam_scores Series?
exam_scores.size
# 20


# 2. Run the code to discover the minimum, the maximum, the mean, and the 
# median scores for the exam_scores Series.
exam_scores.describe()
# count    20.000000
# mean     78.150000
# std      11.352139
# min      60.000000
# 25%      70.500000
# 50%      79.000000
# 75%      85.250000
# max      96.000000



# 3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
exam_scores.plot.hist()
plt.title('Exam Scores')
plt.xlabel('Student Index')
plt.ylabel('Exam Score')
plt.show()

# 4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. 
# Add the necessary points to the highest grade to make it 100, and add the same number of points to every 
# other score in the Series as well.
curve = 100 - exam_scores.max()
curved_scores = exam_scores + curve


# 5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical 
# value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. 
# Save this as a Series named letter_grades.
# Define bin edges.
bin_edges = [0, 70, 75, 80, 90, 101]

# Create a list of bin labels; you should have one less than bin edges.
bin_labels = ['F', 'D', 'C', 'B', 'A']

# Use the .cut() function to create 5 bins as defined and label.
letter_grades = pd.cut(curved_scores, bins=bin_edges, labels=bin_labels)
letter_grades


# 6. Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.






