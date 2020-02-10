# A DAO for interacting with our MsSQL instance.
from pandas import DataFrame

import mysql.conntor

connection = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword"
)

def get_batter_history(batter_name):
    # run a query, return a pandas data frame of all the relevant columns
    #  and every single row
    # SELECT cols FROM table WHERE player
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM AllData WHERE playername = " + batter_name)
    print(connection)
    return DataFrame()


def find_similar_batters(coefs):
    # select batter_name where r^2 above a critical level
    # AND whose coefs are within, idk, 15% of the value of these coefficients provided to this function
    return DataFrame()


def get_pitcher_averages(pitcher_name):
    return DataFrame()