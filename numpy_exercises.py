import numpy as np
import math



a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print(a)

# 1. How many negative numbers are there?
print(a[a<0])
a_neg = a[a<0]


print(a_neg.shape)
# There are four




# 2. How many positive numbers are there?

a_pos = a[a>0]
print(a_pos.shape)
# There are four


# 3. How many even positive numbers are there?

a_pos_even = [i for i in a if (i % 2 == 0) and i > 0]
print(a_pos_even)


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

a3 = (a + 3)
a3_pos = a[a3 > 0]
print(a3_pos)

print(a3_pos.shape)



# 5. If you squared each number, what would the new mean and standard deviation be?
# std is 144.0243 and mean is 74

n = a**2

print(n.mean())

n.std()

print(n.std())




# 6. A common statistical operation on a dataset is centering. This means to adjust the 
# data such that the mean of the data is 0. This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.

# The mean is 3 so we subtract from array to center it.

print(a.mean())

centered_a = a - 3

print(centered_a)



# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# z = (x - mean) / stddev

# a_mean = 

z = (a - a.mean()) / a.std()

print(z)



### MORE PRACTICE




# Life w/o numpy to life with numpy





## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a)



# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(min_of_a)




# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a)




# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
length_of_a = len(a)
mean_of_a = sum_of_a / length_of_a
print(mean_of_a)

# or
# mean_of_a = np.mean(a)
# print(mean_of_a)




# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the 
# numbers in the above list together
# The answer is 3628800

product_of_a = 1
for i in a:
    product_of_a = product_of_a * i

print(product_of_a)

# print(np.prod(a))


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared 
# like [1, 4, 9, 16, 25...]
squares_of_a = []
for i in a:
    squares_of_a.append(i ** 2)

print(squares_of_a)



# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = []
for i in a:
    if i % 2 == 1:
        odds_in_a.append(i)
print(odds_in_a)




# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = []
for i in a:
    if i % 2 == 0:
        evens_in_a.append(i)
print(evens_in_a)


# odds_in_a = [num for num in a if num % 2 == 1]







## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and 
# list of squares for this list of two lists.


b = [
    [3, 4, 5],
    [6, 7, 8]
]

b = np.array ([
    [3, 4, 5],
    [6, 7, 8]
])



# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)


sum_of_b = np.sum(b)
print(sum_of_b) # sum is 33
print(type(b))



# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])


# print(np.min(b))


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

print(np.max(b))




# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

print(np.mean(b))



# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number


print(np.prod(b))




# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

np.square(b)



# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

b[b % 2 == 1]


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

b[b % 2 == 0]

            

# Exercise 9 - print out the shape of the array b.
np.shape(b)


# Exercise 10 - transpose the array b.
np.transpose(b)



# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
np.reshape(b, (1, 6))
## give us array([[3, 4, 5, 6, 7, 8]])



# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
np.reshape(b, (6, 1))
# gives us 
# array([[3],
#        [4],
#        [5],
#        [6],
#        [7],
#        [8]])




## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to 
# using numpy array methods.
type(c) # a list

# make an array
c = np.array ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

# Exercise 1 - Find the min, max, sum, and product of c.
np.min(c) # 1
np.max(c) # 9
np.sum(c) # 45

# Exercise 2 - Determine the standard deviation of c.
np.std(c) # 2.582

# Exercise 3 - Determine the variance of c.
np.var(c) # 6.666

# Exercise 4 - Print out the shape of the array c
np.shape(c)
# (3, 3)

# Exercise 5 - Transpose c and print out transposed result.
np.transpose(c)
# array([[1, 4, 7],
#        [2, 5, 8],
#        [3, 6, 9]])

# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c, c)
# array([[ 30,  36,  42],
#        [ 66,  81,  96],
#        [102, 126, 150]])

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. 
# Answer should be 261
c_transposed = np.transpose(c)
np.sum(c * c_transposed)

 # or c.T to transpose

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. 
# Answer should be 131681894400.
c_transposed = np.transpose(c)
np.prod(c * c_transposed)

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# turn to array
d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
# array([[ 0.89399666, -0.98803162,  0.85090352,  0.        ,  0.58061118,
#         -0.80115264],
#        [ 0.85090352, -0.89399666,  0.98803162, -0.17604595,  0.89399666,
#          0.        ],
#        [-0.30481062,  0.85090352, -0.85090352,  0.89399666, -0.85090352,
#         -0.80115264]])

# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
# array([[-0.44807362,  0.15425145,  0.52532199,  1.        ,  0.81418097,
#         -0.59846007],
#        [ 0.52532199, -0.44807362,  0.15425145,  0.98438195, -0.44807362,
#          1.        ],
#        [-0.95241298,  0.52532199,  0.52532199, -0.44807362,  0.52532199,
#         -0.59846007]])

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
# array([[-1.99520041, -6.4053312 ,  1.61977519,  0.        ,  0.71312301,
#          1.33869021],
#        [ 1.61977519,  1.99520041,  6.4053312 , -0.17883906, -1.99520041,
#          0.        ],
#        [ 0.32004039,  1.61977519, -1.61977519, -1.99520041, -1.61977519,
#          1.33869021]])

# Exercise 4 - Find all the negative numbers in d
d[d<0]
# array([-90, -30, -45, -45])

# Exercise 5 - Find all the positive numbers in d
d[d>0]
# array([ 90,  30,  45, 120, 180,  45, 270,  90,  60,  45,  90, 180])

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)
# array([-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])

# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))
# 11

# Exercise 8 - Print out the shape of d.
np.shape(d)
# (3, 6)
d.shape
# (3, 6)

# Exercise 9 - Transpose and then print out the shape of d.
print(d.T.shape)

# Exercise 10 - Reshape d into an array of 9 x 2
np.reshape(d, (9, 2))
# array([[ 90,  30],
#        [ 45,   0],
#        [120, 180],
#        [ 45, -90],
#        [-30, 270],
#        [ 90,   0],
#        [ 60,  45],
#        [-45,  90],
#        [-45, 180]])
