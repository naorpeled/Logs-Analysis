# About
In this repository you will find my solution to the *Logs Analysis* project from Udacity's Full Stack Nanodegree.
This project explores basic concepts regarding Python, Relational Databases, Queries and Views by analyzing a fictional 
news website database.

# The questions that my queries answer
* 1. What are the most popular three articles of all time?
* 2. Who are the most popular article authors of all time?
* 3. On which days did more than 1% of requests lead to errors? 

## Setup
### How to get/install Python version 2 or 3
Download link: https://www.python.org/downloads/

### How to get/install VirtualBox
Download link: https://www.virtualbox.org/wiki/Downloads

### How to get/install and setup Vagrant
*Step One* - Download and install vagrant from https://www.vagrantup.com/downloads.html

*Step Two* - ```cd``` into the *_vagrant_* directory with your shell(windows - Git Bash, Linux/Mac OS- Terminal) 

*Step Three* - run the command ```vagrant up``` with your shell in order to turn on the virtual machine
and then run ```vagrant ssh``` in order to get into the virtual machine shell 

### How to get and set up the PostgreSQL API on your virtual machine
Follow the detailed instructions on PostgreSQL's website on the following link:
https://www.postgresql.org/download/linux/ubuntu/

### How to get and set up the news database
*Step One* - Download the database file from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

*Step Two* - Unzip the file and place *_newsdata.sql_* into the *_vagrant_* directory on your local machine

*Step Three* - ```cd``` into the *_vagrant_* directory with your shell(windows - Git Bash, Linux/Mac OS- Terminal) 
and run the command ```psql -d news -f newsdata.sql```

### Views used in the project
#### View for showing the articles that each author wrote(used in the second query):
* CREATE VIEW article_authors as SELECT articles.slug ,authors.name FROM authors, articles WHERE articles.author =authors .id;

#### View for showing the amount of entries with errors for each date in the log table(used in the third query)
* CREATE VIEW as failed_entries SELECT date(time),count(log.status) FROM log WHERE log.status NOT LIKE '%200%' group by date(time) ORDER BY date(time) DESC;

#### View for showing the amount of entries in total for each date in the log table(used in the third query)
* CREATE VIEW all_entries as SELECT date(time),count(log.status) FROM log group by date(time) ORDER BY date(time) DESC;

## Functions
*first_query()* - _The solution for the first query in the project_

*second_query()* - _The solution for the second query in the project_

*third_query()* - _The solution for the third query in the project_
