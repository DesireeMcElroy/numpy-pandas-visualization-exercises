import pandas as pd
import numpy as np


# Create a function named get_db_url. It should accept a username, 
# hostname, password, and database name and return a url connection 
# string formatted like in the example at the start of this lesson.


def get_db_url(host, user, password):
    url = f'mysql+pymysql://{user}:{password}@{host}/employees'
    return url


from env import host, user, password
url = get_db_url(host, user, password)


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
titles_df.value_counts()

titles_df['titles'].value_counts



# 8. What is the oldest date in the to_date column?
titles_df.to_date.sort_values().head(1)


# 9. What is the most recent date in the to_date column?
titles_df.to_date.sort_values(ascending=False)
