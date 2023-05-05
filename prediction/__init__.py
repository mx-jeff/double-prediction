import logging
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from ydata_profiling import ProfileReport

import matplotlib.pyplot as plt

from database import mongodb_read


def validate(x_test, prediction):
    quadratic_regression_error = mean_squared_error(x_test, prediction)
    print(f"Score erro quadratico: {quadratic_regression_error}")

    r2_regression = r2_score(x_test, prediction)
    print(f"score r2: {r2_regression}") 


def display_stats(x, y):
    plt.scatter(x=x, y=y)
    plt.show()


def get_profile_report(df, filename:str="data/blaze.html"):
    profile = ProfileReport(df)
    profile.to_file(filename)


def preprocess(data, filepath=None):
    if filepath:
        df = pd.read_csv("data/blaze_double.csv", error_bad_lines=False)
    
    else:
        if not data:
            logging.error("No data")
            return
    
    # load and drop mongo id
    df = pd.DataFrame(data)
    df = df.drop("_id", axis=1)
    
    # convert to datetime format
    df['datetime'] = df['date'].str.cat(df['minute'], sep=' ')
    df = df.replace({'Dia:':''}, regex = True)
    df['datetime'] = pd.to_datetime(df.datetime, format=" %d/%m/%Y %H:%M")
    
    # number = df['number'] #.dropna(axis=0, how="all")
    dummies = pd.get_dummies(df['color'], columns=df['color'])
    dummies = dummies.drop('White', axis=1)
    df = pd.concat([df, dummies], axis=1)
    
    # drop list
    df = df.drop(columns=["minute", 'date', 'color', 'seed', 'whitebets', 'redbets', 'blackbets'], axis=1)

    # remove duplicates and missing value
    df = df.dropna(axis=0)
    df = df.drop_duplicates()
    # get_profile_report(df)
    # print(df)
    # print(len(df))
    return df


def prediction():
    no_sql_data = mongodb_read()
    df = preprocess(no_sql_data)
   
    X = df['number']
    Y = df.drop(columns=['number'], axis=1)

    X = df.iloc[:, 0].values
    Y = df.iloc[:, 1].values
    X = X.reshape(-1,1)

    x_train, x_test, y_train, y_test = train_test_split(X, Y)
    
    model =  LinearRegression() #DecisionTreeRegressor() 
    model.fit(x_train, y_train)

    prediction = model.predict(x_test)
    print(prediction)
    # # display_stats(y_test/10000, prediction/10000)
    validate(x_test, prediction)
    