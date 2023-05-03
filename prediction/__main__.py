import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from ydata_profiling import ProfileReport

import matplotlib.pyplot as plt


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


def preprocess():
    df = pd.read_excel("data/blaze_double.xlsx")
    # get_profile_report(df)
    df = df[['Cor', 'Número']]
    number = df['Número'] #.dropna(axis=0, how="all")
    dummies = pd.get_dummies(df['Cor'], columns=df['Cor'])
    dummies = dummies.drop('White', axis=1)
    df = pd.concat([number, dummies], axis=1)
    # df = df.drop_duplicates()

    print(len(df))
    # get_profile_report(df, 'data/clean.html')
    df.to_csv('data/blaze_double_clean.csv', index=False)
    return df


def main():
    df = preprocess()
    # df = pd.read_csv("data/blaze_double_clean.csv")
   
    X = df['Número']
    Y = df.drop(columns=['Número'], axis=1)

    X = df.iloc[:, 0].values
    Y = df.iloc[:, 1].values
    X = X.reshape(-1,1)

    x_train, x_test, y_train, y_test = train_test_split(X, Y)
    
    model = LinearRegression() #DecisionTreeRegressor() #
    model.fit(x_train, y_train)

    prediction = model.predict(x_test)
    # print(prediction)
    # display_stats(y_test/10000, prediction/10000)
    validate(x_test, prediction)
    

if __name__ == "__main__":
    main()
