#About
In this repository you will find my solution to the *Logs Analysis* project from Udacity's Full Sstack Nanodegree.
_The code is written with Python v2.7 and it uses the PostgreSQL api_

##Functions
*first_query()* - _The solution for the first query in the project_
*second_query()* - _The solution for the second query in the project_
*third_query()* - _The solution for the third query in the project_
  
##Views used in the project
###View for showing the articles that each author wrote(used in the second query):
* CREATE VIEW article_authors as SELECT articles.slug ,authors.name FROM authors, articles WHERE articles.author =authors .id;

###View for showing the amount of entries with errors for each date in the log table(used in the third query)
* CREATE VIEW as failed_entries SELECT date(time),count(log.status) FROM log WHERE log.status NOT LIKE '%200%' group by date(time) ORDER BY date(time) DESC;

###View for showing the amount of entries in total for each date in the log table(used in the third query)
* CREATE VIEW all_entries as SELECT date(time),count(log.status) FROM log group by date(time) ORDER BY date(time) DESC;
