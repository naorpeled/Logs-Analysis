# !/usr/bin/env python
# My code for the logs analysis project

import psycopg2
import platform

# Trying to connect to the database
# If the attempt fails an error is displayed
try:
    db = psycopg2.connect("dbname=news")
except DataError:
    print("Unable to connect to the database")


# This query prints a sorted list of the amount of views that each article has
def first_query():
    print('First query: ')
    cursor = db.cursor()
    cursor.execute(
                   'SELECT path, count(path) ' +
                   'FROM log WHERE path like \'%article%\'' +
                   'AND status like \'%200%\' ' +
                   'group by path order by count(path) DESC limit 3;')
    row = cursor.fetchone()
    for i in range(3):
        print(((row[0])[9:]).replace('-', ' ') +
              " got " + str(row[1]) + " views so far.")
        row = cursor.fetchone()
    cursor.close()


# This query prints a sorted list of authors and their populariy
# (amount of views on their articles)
def second_query():
    cursor = db.cursor()
    print('Second Query: ')
    cursor.execute(
                    'SELECT article_authors.name, count(log.path) ' +
                    'FROM article_authors, log ' +
                    'WHERE log.path = \'/article/\' || article_authors.slug ' +
                    'group by article_authors.name ORDER BY count DESC;')
    row = cursor.fetchone()
    while row is not None:
        print(row[0] + " has " + str(row[1]) + " views in total.")
        row = cursor.fetchone()
    cursor.close()


# This query calculates the percentage of how many errors were in each day
# and prints the date of the days that had 1% or more
def third_query():
    cursor = db.cursor()
    print("Third Query: ")
    cursor.execute(
                    'SELECT ' +
                    'all_entries.date,all_entries.count as all_count ' +
                    ', failed_entries.count as failed_count '
                    'FROM all_entries,failed_entries ' +
                    'WHERE all_entries.date = failed_entries.date ' +
                    'GROUP BY all_entries.date,all_entries.count, ' +
                    'failed_entries.count ' +
                    'ORDER BY all_entries.date DESC;')
    row = cursor.fetchone()
    while row is not None:
        operation = float(row[2]) / float(row[1]) * 100.0
        if(operation > 1.0):
            print(str(row[0]) + ' had ' + str(operation) + '% errors.')
        row = cursor.fetchone()
    cursor.close()


# Main - area of executing the functions defined above
print('This app was built with Python-v'+platform.python_version())
first_query()
second_query()
third_query()
db.close()
