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
# fruits.apply(len)nlargest(keep='all')

# or

longest_fruit = fruits.str.len() == fruits.str.len().max
fruits[longest_fruit]

#or

max(fruits, key=len)

# or

fruits[fruits.str.len().idxmax()]

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


