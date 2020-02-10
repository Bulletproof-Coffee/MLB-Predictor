# A model for predicting batter performance based on pitch physics.

from sklearn import linear_model
import pandas as pd
from app.model.datastore import MySqlDao


class RegressionResult:

    def __init__(self, probability, rsquare):
        self.probabiliy = probability
        self.rsquare = rsquare


# Returns a linear model for this batter based on his history against all pitches ever
def get_batter_model(batter_name):
    df = MySqlDao.get_batter_history(batter_name)
    target = pd.DataFrame(data=df, columns=["hit"])
    return linear_model.LinearRegression().fit(X=df, y=target["hit"])


# Returns a data frame
def get_pitcher_averages(batter_name, pitcher_name):
    return MySqlDao.get_pitcher_averages(batter_name, pitcher_name)


# Returns a number indicating the hit likelihood and the r^2
def determine_hit_likelihood(batter_name, pitcher_name):
    batter_model = get_batter_model(batter_name)
    pitcher_averages = get_pitcher_averages(batter_name, pitcher_name)
    # pitcher avg may need to be converted to an array
    result = batter_name.predict(pitcher_averages)
    return RegressionResult(result, batter_model.score)


