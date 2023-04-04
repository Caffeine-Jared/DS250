import sqlite3
import pandas as pd


# GQ 1 
# Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. The new 
# table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each 
# salary. Order the table by salary (highest to lowest) and print out the table in your report.
con = sqlite3.connect('Project_3\lahmansbaseballdb.sqlite')

query1 = """
SELECT DISTINCT cp.playerid, cp.schoolid, s.salary, s.yearid, s.teamid
FROM collegeplaying cp
INNER JOIN salaries s on cp.playerid = s.playerid
WHERE schoolid = 'idbyuid'
ORDER BY salary DESC;
"""

q1_df = pd.read_sql_query(query1, con)
print(q1_df)

# GQ 2
# This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)

    # GQ 2a
    # Write an SQL query that provides playerID, yearID, and batting average for players with at least 1 at bat that year. 
    # Sort the table from highest batting average to lowest, and then by playerid alphabetically. Show the top 5 results in your report.
q2a_query = """
SELECT playerID, yearID, ROUND(CAST(H AS FLOAT) / CAST(AB AS FLOAT), 3) AS AVG
FROM batting
WHERE AB > 0
ORDER BY AVG DESC, playerID
LIMIT 5;
"""
q2a_df = pd.read_sql_query(q2a_query, con)
print(q2a_df)

    # GQ 2b
    # Use the same query as above, but only include players with at least 10 at bats that year. Print the top 5 results.
q2b_query = """
SELECT playerID, yearID, ROUND(CAST(H AS FLOAT) / CAST(AB AS FLOAT), 3) AS AVG
FROM batting
WHERE AB >= 10
ORDER BY AVG DESC, playerID
LIMIT 5;

"""
q2b_df = pd.read_sql_query(q2b_query, con)
print(q2b_df)

    # GQ 2c
    # Now calculate the batting average for players over their entire careers (all years combined). Only include players with at least 100 at bats, and print the top 5 results.
g2c_query = """
SELECT playerID, ROUND(CAST(SUM(H) AS FLOAT) / CAST(SUM(AB) AS FLOAT), 3) AS career_batting_average
FROM batting
HAVING SUM(AB) >= 100
GROUP BY playerID
ORDER BY career_batting_average DESC
LIMIT 5;
"""
q2c_df = pd.read_sql_query(g2c_query, con)
print(q2c_df)
# GQ 3
# Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc). 
# Write an SQL query to get the data you need, then make a graph in Altair to visualize the comparison. What do you learn?
q3_query = """
SELECT teams.teamID, SUM(batting.HR) AS total_home_runs, SUM(teams.W) AS total_wins
FROM batting
JOIN teams ON batting.yearID = teams.yearID AND batting.teamID = teams.teamID
WHERE batting.yearID = 2019 AND batting.teamID IN ('NYA', 'BOS')
GROUP BY teams.teamID;
"""
q3_df = pd.read_sql_query(q3_query, con)
print(q3_df)

query = 'SELECT * FROM batting LIMIT 2'
qr = pd.read_sql_query(query, con)

print(qr)


