import pandas as pd
import numpy as np
from pydataset import data
import matplotlib.pyplot as plt


# Create a function named get_db_url. It should accept a username, 
# hostname, password, and database name and return a url connection 
# string formatted like in the example at the start of this lesson.


def get_db_url(host, user, password, database):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url


from env import host, user, password
url = get_db_url(host, user, password, 'employees')


# 2. Use your function to obtain a connection to the employees database.
pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)


# Once you have successfully run a query:

# a. Intentionally make a typo in the database url. 
# What kind of error message do you see?
# NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:mysql.pymyssql

# b. Intentionally make an error in your SQL query. 
# What does the error message look like?
# ProgrammingError: (pymysql.err.ProgrammingError) (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'OFFSET 50' at line 1")
# [SQL: SELECT * FROM employees LIMIT5 OFFSET 50]
# (Background on this error at: http://sqlalche.me/e/13/f405)



# 4. Read the employees and titles tables into two separate DataFrames.
titles_df = '''
SELECT *
FROM titles
'''

employees_df = '''
SELECT *
FROM employees
'''

titles_df = pd.read_sql(titles_df, url)
employees_df = pd.read_sql(employees_df, url)


# 5. How many rows and columns do you have in each DataFrame? 
# Is that what you expected?
employees_df.shape # 300024, 6
titles_df.shape  # 443308, 4


# 6. Display the summary statistics for each DataFrame.
titles_df.describe()
employees_df.describe()


#7. How many unique titles are in the titles DataFrame?
# titles_df.value_counts()

# titles_df['titles'].value_counts



# 8. What is the oldest date in the to_date column?
titles_df.to_date.sort_values().head(1)


# 9. What is the most recent date in the to_date column?
titles_df.to_date.sort_values(ascending=False)





# Exercises II


# 1. Copy the users and roles DataFrames from the examples above.
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

# 2. What is the result of using a right join on the DataFrames?
(users.merge(roles, 
            left_on='role_id', 
            right_on='id', 
            how='right')
            )
# The same amount of columns are displayed however, 
# roles has only four rows thus the merged table only 
# displays four rows.



# 3. What is the result of using an outer join on the DataFrames?
(users.merge(roles, 
            left_on='role_id', 
            right_on='id', 
            how='outer')
            )
# outer includes everything so the table has a total of six rows.
# It seems it only has as much as the largest table.




# 4. What happens if you drop the foreign keys from the DataFrames and try to merge them?
(users.merge(roles, 
            left_on='role_id', 
            right_on='id', 
            how='outer')
    .drop(columns='role_id')
    .drop(columns='id')
            )
## KeyError: "['id'] not found in axis"




# 5. Load the mpg dataset from PyDataset.
mpg_df = data('mpg')




# 6. Output and read the documentation for the mpg dataset.
data('mpg', show_doc=True)



# 7. How many rows and columns are in the dataset?
mpg_df.shape
# 234 rows and 14 columns




# 8. Check out your column names and perform any cleanup you may want on them.
mpg_df.rename(columns={'displ': 'display', 
                     'cyl': 'cylinder',
                     'trans': 'transmission',
                     'drv': 'drive',
                     'cty': 'city',
                     'hwy': 'highway',
                     'fl': 'fuel'}, inplace=True
            )






# 9. Display the summary statistics for the dataset.
mpg_df.describe()



# 10. How many different manufacturers are there?
len(mpg_df.manufacturer.unique())
# 15

# or

mpg_df.manufacturer.value_counts().count()

# 11. How many different models are there?
len(mpg_df.model.unique())
# 38




# 12. Create a column named mileage_difference like you did in the DataFrames exercises; 
# this column should contain the difference between highway and city mileage for each car.
mpg_df['mileage_difference'] = (mpg_df.highway - mpg_df.city)




# 13. Create a column named average_mileage like you did in the DataFrames exercises; 
# this is the mean of the city and highway mileage.
mpg_df['average_mileage'] = (mpg_df.highway + mpg_df.city)/2





# 14. Create a new column on the mpg dataset named is_automatic that holds boolean 
# values denoting whether the car has an automatic transmission.
mpg_df['is_automatic'] = (mpg_df.transmission.str.contains('auto'))

# or from Faith
# mpg = mpg.assign(mileage_difference = mpg.highway - mpg.city,
#                  average_mileage = (mpg.highway + mpg.city) / 2,
#                  is_automatic = mpg.transmission.str.startswith('a'))


# 15. Using the mpg dataset, find out which which manufacturer has the best miles per 
# gallon on average?
mpg_df.groupby('manufacturer').average_mileage.agg('mean').sort_values(ascending=False).head(1)

# or use nlargest(1)



# 16. Do automatic or manual cars have better miles per gallon?
mpg_df.groupby(np.where(mpg_df['transmission'].str.contains('auto'), 'auto', 'manual')).average_mileage.agg('mean')



# mpg['a or m'] = np.where(mpg['trans'].str.startswith('a') , 'auto', 'manual')
# mpg.groupby('a or m').average_mileage.agg('mean')





# Exercises III



# 1. Use your get_db_url function to help you explore the data from the chipotle database.
url = get_db_url(host, user, password, 'chipotle')
orders_df = pd.read_sql('SELECT * FROM orders', url)

# 2. What is the total price for each order?
# Convert the item_price column into a float
orders_df['item_price'] = orders_df.item_price.str.replace('$', '').astype('float')
orders_df.groupby('order_id').sum('item_price')

# 3. What are the most popular 3 items?
orders_df.groupby('item_name').quantity.agg('sum').sort_values(ascending=False).head(3)
# can also use quantity.sum()

# 4. Which item has produced the most revenue?
orders_df.groupby(['item_name', 'item_price']).quantity.agg('sum')
# best_sellers = orders.groupby('item_name').quantity.sum().nlargest(4)

# 5. Using the titles DataFrame, visualize the number of employees with each title.
titles_df.title.value_counts()
titles_df.title.value_counts().plot.bar()


# 6. Join the employees and titles DataFrames together.
employees_and_titles = employees_df.merge(titles_df, how='inner', on = 'emp_no')


# 7. Visualize how frequently employees change titles.
titles_df.groupby('emp_no').title.count().sample(10)
titles_df.groupby('emp_no').title.count().value_counts()
changes = titles_df.emp_no.value_counts()
changes.value_counts().plot(kind='barh', 
                            color='blueviolet', 
                            ec='black', 
                            width=.8)

plt.title('How Common is it for Employees to Change Titles?')
plt.xlabel('Number of Employees')
plt.ylabel('Number of Title Changes')
plt.yticks(ticks=[0,1,2], labels=['0 Changes', '1 Change', '2 Changes'])

# reorder y-axis of horizontal bar chart
plt.gca().invert_yaxis()

plt.show()


# 8. For each title, find the hire date of the employee that was hired most recently with that title.
employees_and_titles.groupby('title').hire_date.max()

# 9. Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas code to perform the manipulations.)
dept_title_query = '''

                    SELECT t.emp_no, 
                    t.title, 
                    t.from_date, 
                    t.to_date, 
                    d.dept_name 
                    FROM departments AS d 
                    JOIN dept_emp AS de USING(dept_no) 
                    JOIN titles AS t USING(emp_no);

                    '''


dept_titles = pd.read_sql(dept_title_query, get_db_url(host, user, password, 'employees'))
dept_titles.shape
all_titles_crosstab = pd.crosstab(dept_titles.dept_name, dept_titles.title)



